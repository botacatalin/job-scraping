"""Extracting job information from user defined web sites"""

import sys
import time
import datetime
import threading
import webbrowser

from jobs.model.records import Record
from jobs.ui import job_search_ui
from jobs.ui import details_ui
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication
from jobs.services.search_service import Search
from jobs.services.db_service import DB
from sqlite3 import Error as sqlite3Error


class JobSearchApp(QDialog, job_search_ui.Ui_JobSearch):
    db = DB()

    def __init__(self):
        super(JobSearchApp, self).__init__()
        self.setupUi(self)
        self.basic_init()

        self.select_company.currentIndexChanged.connect(self.select_url)
        self.home_btn.clicked.connect(self.display_stack_home)
        self.add_btn.clicked.connect(self.display_stack_add)
        self.remove_btn.clicked.connect(self.display_stack_remove)
        self.info_btn.clicked.connect(self.display_stack_info)
        self.exit_btn.clicked.connect(self.close)
        self.add_record_btn.clicked.connect(self.make_record)
        self.find_jobs.clicked.connect(self.find_jobs_t)
        self.delete_record_btn.clicked.connect(self.remove_record)
        self.open_in_browser.clicked.connect(self.open_browser)
        self.details_btn.clicked.connect(self.details)

    def open_browser(self):
        """Opens selected urls in a  browser"""
        if len(self.search_url_list.selectedItems()) > 0:
            [webbrowser.open(str(x.text())) for x in self.search_url_list.selectedItems()]

    def basic_init(self):
        """Grouping some general initialization functions"""
        self.db.create_table()
        self.stack_widgets.setCurrentIndex(0)
        self.select_company_from_db()

    def details(self):
        if len(self.jobs_list.selectedItems()) > 0:
            dialog = DetailsDialog()
            dialog.job_selected_lbl.setText(self.jobs_list.selectedItems()[0].text())
            dialog.company_selected_lbl.setText(self.select_company.currentText())
            dialog.exec_()

    @staticmethod
    def get_date_stamp():
        """Returning the current date time in a easy to understand format"""
        unix = time.time()
        date_stamp = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        return date_stamp

    def display_stack_home(self):
        """Selecting the home page widget"""
        self.select_company_from_db()
        self.stack_widgets.setCurrentIndex(0)

    def display_stack_add(self):
        """Selecting the add page widget"""
        self.stack_widgets.setCurrentIndex(1)

    def display_stack_remove(self):
        """Selecting the remove page widget"""
        self.stack_widgets.setCurrentIndex(2)
        self.remove_records_list.clear()
        records = self.db.get_all_company_names()
        for company in records.fetchall():
            self.remove_records_list.addItem(company[0])

    def display_stack_info(self):
        """ Selecting the info page widget """
        self.stack_widgets.setCurrentIndex(3)

    def remove_record(self):
        """ Remove a record from a database """
        company_names = [name.text() for name in self.remove_records_list.selectedItems()]
        for name in company_names:
            self.db.remove(str(name))
        self.display_stack_remove()

    def make_record(self):

        gps_lat = self.gps_lat.text()
        gps_long = self.gps_long.text()
        company_name = self.company_name.text()
        search_url = self.company_search_url.text()
        xpath_pattern = self.xpath_pattern.text()
        search_url_bestjobs = self.company_search_url_bestjobs.text()
        xpath_pattern_bestjobs = self.xpath_pattern_bestjobs.text()
        search_url_ejobs = self.company_search_url_ejobs.text()
        xpath_pattern_ejobs = self.xpath_pattern_ejobs.text()
        company_email = self.company_email.text()

        model = Record(gps_lat, gps_long, company_name, search_url,
                       xpath_pattern, company_email)

        # empty string are falsey
        if search_url and xpath_pattern:
            self.add_company_record(model)
            self.add_url_record(model)
        else:
            QMessageBox().information(self, "Information", "Add at least the company url and xpath", QMessageBox.Ok)

        if search_url_bestjobs and xpath_pattern_bestjobs:
            model = Record(gps_lat, gps_long, company_name, search_url_bestjobs,
                           xpath_pattern_bestjobs, company_email)
            self.add_url_record(model)

        if search_url_ejobs and xpath_pattern_ejobs:
            model = Record(gps_lat, gps_long, company_name, search_url_ejobs,
                           xpath_pattern_ejobs, company_email)
            self.add_url_record(model)

    def add_company_record(self, record_model):
        """Adding a company to sqlite3 db"""

        try:
            self.db.insert_company(self.get_date_stamp(), record_model)
            QMessageBox().information(self, "Information", "Record added to database", QMessageBox.Ok)
        except sqlite3Error:
            QMessageBox().warning(self, "Warning", "Could not add company to database", QMessageBox.Ok)

    def add_url_record(self, record_model):
        """Adding a URL to sqlite3 db"""

        try:
            self.db.insert_url(self.get_date_stamp(), record_model)
        except sqlite3Error:
            QMessageBox().warning(self, "Warning", "Could not add URL to database", QMessageBox.Ok)

    def find_jobs_t(self):
        """Starts thread to for searching data from websites"""

        t = threading.Thread(target=self.scrap_website, args=[])
        t.start()

    def scrap_website(self):
        self.find_jobs.setText("Searching ...")
        self.jobs_list.clear()
        # get selected search url links
        selected_items = self.search_url_list.selectedItems()

        if len(selected_items) > 0:
            # get url index
            job_url = selected_items[0].text()
            xpath = self.db.get_url_xpath(job_url)
            s = Search()
            jobs = s.search_jobs(job_url, xpath)
            for job in jobs:
                self.jobs_list.addItem(job)

            self.find_jobs.setText("Find Jobs (" + str(len(jobs)) + ")")

    def select_company_from_db(self):
        self.select_company.clear()
        records = self.db.get_all_company_names()
        for company in records.fetchall():
            self.select_company.addItem(company[0])
        self.select_company.setCurrentIndex(-1)

    def select_url(self):
        """Selects url from database based on company name combobox selection"""

        records = self.db.get_company_search_url(self.select_company.currentText())
        self.clean_search_url_list()
        for url in records:
            self.search_url_list.addItem(url[0])
        self.search_url_list.setCurrentRow(0)

    def clean_search_url_list(self):
        self.search_url_list.clear()


class DetailsDialog(QDialog, details_ui.Ui_Details):
    db = DB()

    def __init__(self):

        super(DetailsDialog, self).__init__()
        self.setupUi(self)
        self.find_similar_jobs.clicked.connect(self.find_companies_with_similar_jobs)
        self.open_in_browser2.clicked.connect(self.open_in_browser)

    def find_companies_with_similar_jobs(self):
        self.details_result_list.clear()
        records_dict = self.db.get_all_company_urls_and_xpath()
        result = Search.search_companies_with_similar_jobs(records_dict, self.job_selected_lbl.text())

        for url in result:
            company = self.db.get_company_name(url)
            self.details_result_list.addItem("[ " + company.upper() + " ] " + url)

    def open_in_browser(self):
        """Opens selected urls in a  browser"""
        if len(self.details_result_list.selectedItems()) > 0:
            [webbrowser.open(str(x.text()).split("]")[1].strip()) for x in self.details_result_list.selectedItems()]


def main():
    app = QApplication(sys.argv)
    dialog = JobSearchApp()
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
