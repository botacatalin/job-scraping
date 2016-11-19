# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JobSearch.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_JobSearch(object):
    def setupUi(self, JobSearch):
        JobSearch.setObjectName("JobSearch")
        JobSearch.resize(642, 530)
        JobSearch.setMinimumSize(QtCore.QSize(642, 530))
        JobSearch.setMaximumSize(QtCore.QSize(642, 530))
        JobSearch.setStyleSheet("")
        JobSearch.setModal(True)
        self.frame = QtWidgets.QFrame(JobSearch)
        self.frame.setGeometry(QtCore.QRect(0, 0, 121, 531))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: rgb(69, 69, 69);\n"
"    border-right:2px solid #dcd;\n"
"}\n"
"QToolButton {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"background-color: rgba(255, 147, 56, 76);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(68, 108, 255);\n"
"color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QLabel {\n"
"color: rgb(250, 250, 250);\n"
"border-right:0px\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 420, 44, 92))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.info_btn = QtWidgets.QToolButton(self.layoutWidget)
        self.info_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info_btn.setIcon(icon)
        self.info_btn.setIconSize(QtCore.QSize(32, 32))
        self.info_btn.setObjectName("info_btn")
        self.verticalLayout_2.addWidget(self.info_btn)
        self.exit_btn = QtWidgets.QToolButton(self.layoutWidget)
        self.exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon1)
        self.exit_btn.setIconSize(QtCore.QSize(32, 32))
        self.exit_btn.setObjectName("exit_btn")
        self.verticalLayout_2.addWidget(self.exit_btn)
        self.logo_lbl = QtWidgets.QLabel(self.frame)
        self.logo_lbl.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(13)
        self.logo_lbl.setFont(font)
        self.logo_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_lbl.setWordWrap(True)
        self.logo_lbl.setObjectName("logo_lbl")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 60, 44, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_btn = QtWidgets.QToolButton(self.layoutWidget1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_btn.setIcon(icon2)
        self.home_btn.setIconSize(QtCore.QSize(32, 32))
        self.home_btn.setCheckable(False)
        self.home_btn.setObjectName("home_btn")
        self.verticalLayout.addWidget(self.home_btn)
        self.add_btn = QtWidgets.QToolButton(self.layoutWidget1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_btn.setIcon(icon3)
        self.add_btn.setIconSize(QtCore.QSize(32, 32))
        self.add_btn.setCheckable(False)
        self.add_btn.setObjectName("add_btn")
        self.verticalLayout.addWidget(self.add_btn)
        self.remove_btn = QtWidgets.QToolButton(self.layoutWidget1)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_btn.setIcon(icon4)
        self.remove_btn.setIconSize(QtCore.QSize(32, 32))
        self.remove_btn.setObjectName("remove_btn")
        self.verticalLayout.addWidget(self.remove_btn)
        self.stack_widgets = QtWidgets.QStackedWidget(JobSearch)
        self.stack_widgets.setEnabled(True)
        self.stack_widgets.setGeometry(QtCore.QRect(120, 0, 521, 531))
        self.stack_widgets.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.stack_widgets.setStyleSheet("QStackedWidget {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.985, y2:1, stop:0 rgba(244, 244, 244, 64), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.stack_widgets.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stack_widgets.setObjectName("stack_widgets")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.details_btn = QtWidgets.QPushButton(self.home_page)
        self.details_btn.setGeometry(QtCore.QRect(10, 455, 84, 32))
        self.details_btn.setAutoDefault(False)
        self.details_btn.setObjectName("details_btn")
        self.open_in_browser = QtWidgets.QPushButton(self.home_page)
        self.open_in_browser.setGeometry(QtCore.QRect(390, 455, 112, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_in_browser.sizePolicy().hasHeightForWidth())
        self.open_in_browser.setSizePolicy(sizePolicy)
        self.open_in_browser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.open_in_browser.setAutoDefault(False)
        self.open_in_browser.setObjectName("open_in_browser")
        self.select_compan_lbl = QtWidgets.QLabel(self.home_page)
        self.select_compan_lbl.setGeometry(QtCore.QRect(12, 12, 98, 16))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        self.select_compan_lbl.setFont(font)
        self.select_compan_lbl.setObjectName("select_compan_lbl")
        self.select_company = QtWidgets.QComboBox(self.home_page)
        self.select_company.setGeometry(QtCore.QRect(9, 33, 501, 26))
        self.select_company.setObjectName("select_company")
        self.search_jobs_url_lbl = QtWidgets.QLabel(self.home_page)
        self.search_jobs_url_lbl.setGeometry(QtCore.QRect(12, 65, 72, 16))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        self.search_jobs_url_lbl.setFont(font)
        self.search_jobs_url_lbl.setObjectName("search_jobs_url_lbl")
        self.search_url_list = QtWidgets.QListWidget(self.home_page)
        self.search_url_list.setGeometry(QtCore.QRect(12, 90, 497, 61))
        self.search_url_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.search_url_list.setObjectName("search_url_list")
        self.find_jobs = QtWidgets.QPushButton(self.home_page)
        self.find_jobs.setGeometry(QtCore.QRect(10, 160, 100, 32))
        self.find_jobs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.find_jobs.setObjectName("find_jobs")
        self.jobs_list = QtWidgets.QListWidget(self.home_page)
        self.jobs_list.setGeometry(QtCore.QRect(12, 194, 497, 251))
        self.jobs_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.jobs_list.setObjectName("jobs_list")
        item = QtWidgets.QListWidgetItem()
        self.jobs_list.addItem(item)
        self.select_compan_lbl.raise_()
        self.select_company.raise_()
        self.search_jobs_url_lbl.raise_()
        self.search_url_list.raise_()
        self.find_jobs.raise_()
        self.jobs_list.raise_()
        self.details_btn.raise_()
        self.open_in_browser.raise_()
        self.stack_widgets.addWidget(self.home_page)
        self.add_page = QtWidgets.QWidget()
        self.add_page.setObjectName("add_page")
        self.company_search_url = QtWidgets.QLineEdit(self.add_page)
        self.company_search_url.setGeometry(QtCore.QRect(110, 70, 298, 21))
        self.company_search_url.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.company_search_url.setObjectName("company_search_url")
        self.company_name = QtWidgets.QLineEdit(self.add_page)
        self.company_name.setGeometry(QtCore.QRect(110, 150, 298, 21))
        self.company_name.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.company_name.setObjectName("company_name")
        self.company_email = QtWidgets.QLineEdit(self.add_page)
        self.company_email.setGeometry(QtCore.QRect(110, 180, 298, 21))
        self.company_email.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.company_email.setText("")
        self.company_email.setObjectName("company_email")
        self.xpath_pattern = QtWidgets.QLineEdit(self.add_page)
        self.xpath_pattern.setGeometry(QtCore.QRect(110, 350, 298, 21))
        self.xpath_pattern.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.xpath_pattern.setText("")
        self.xpath_pattern.setObjectName("xpath_pattern")
        self.layoutWidget2 = QtWidgets.QWidget(self.add_page)
        self.layoutWidget2.setGeometry(QtCore.QRect(110, 40, 298, 32))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_record_lbl = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(13)
        font.setItalic(False)
        self.add_record_lbl.setFont(font)
        self.add_record_lbl.setObjectName("add_record_lbl")
        self.horizontalLayout.addWidget(self.add_record_lbl)
        self.add_record_help_btn = QtWidgets.QPushButton(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_record_help_btn.sizePolicy().hasHeightForWidth())
        self.add_record_help_btn.setSizePolicy(sizePolicy)
        self.add_record_help_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/question.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_record_help_btn.setIcon(icon5)
        self.add_record_help_btn.setIconSize(QtCore.QSize(16, 16))
        self.add_record_help_btn.setAutoDefault(False)
        self.add_record_help_btn.setObjectName("add_record_help_btn")
        self.horizontalLayout.addWidget(self.add_record_help_btn)
        self.layoutWidget3 = QtWidgets.QWidget(self.add_page)
        self.layoutWidget3.setGeometry(QtCore.QRect(110, 230, 298, 32))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gps_location_lbl = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        self.gps_location_lbl.setFont(font)
        self.gps_location_lbl.setObjectName("gps_location_lbl")
        self.horizontalLayout_2.addWidget(self.gps_location_lbl)
        self.gps_location_help_btn = QtWidgets.QPushButton(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gps_location_help_btn.sizePolicy().hasHeightForWidth())
        self.gps_location_help_btn.setSizePolicy(sizePolicy)
        self.gps_location_help_btn.setText("")
        self.gps_location_help_btn.setIcon(icon5)
        self.gps_location_help_btn.setIconSize(QtCore.QSize(16, 16))
        self.gps_location_help_btn.setAutoDefault(False)
        self.gps_location_help_btn.setObjectName("gps_location_help_btn")
        self.horizontalLayout_2.addWidget(self.gps_location_help_btn)
        self.layoutWidget4 = QtWidgets.QWidget(self.add_page)
        self.layoutWidget4.setGeometry(QtCore.QRect(110, 320, 298, 32))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.xpath_help_btn = QtWidgets.QPushButton(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xpath_help_btn.sizePolicy().hasHeightForWidth())
        self.xpath_help_btn.setSizePolicy(sizePolicy)
        self.xpath_help_btn.setText("")
        self.xpath_help_btn.setIcon(icon5)
        self.xpath_help_btn.setIconSize(QtCore.QSize(16, 16))
        self.xpath_help_btn.setObjectName("xpath_help_btn")
        self.horizontalLayout_3.addWidget(self.xpath_help_btn)
        self.add_record_btn = QtWidgets.QPushButton(self.add_page)
        self.add_record_btn.setGeometry(QtCore.QRect(300, 420, 110, 32))
        self.add_record_btn.setObjectName("add_record_btn")
        self.company_search_url_bestjobs = QtWidgets.QLineEdit(self.add_page)
        self.company_search_url_bestjobs.setGeometry(QtCore.QRect(110, 100, 298, 21))
        self.company_search_url_bestjobs.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.company_search_url_bestjobs.setObjectName("company_search_url_bestjobs")
        self.company_search_url_ejobs = QtWidgets.QLineEdit(self.add_page)
        self.company_search_url_ejobs.setGeometry(QtCore.QRect(110, 120, 298, 21))
        self.company_search_url_ejobs.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.company_search_url_ejobs.setObjectName("company_search_url_ejobs")
        self.xpath_pattern_bestjobs = QtWidgets.QLineEdit(self.add_page)
        self.xpath_pattern_bestjobs.setGeometry(QtCore.QRect(110, 370, 298, 21))
        self.xpath_pattern_bestjobs.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.xpath_pattern_bestjobs.setText("")
        self.xpath_pattern_bestjobs.setObjectName("xpath_pattern_bestjobs")
        self.xpath_pattern_ejobs = QtWidgets.QLineEdit(self.add_page)
        self.xpath_pattern_ejobs.setGeometry(QtCore.QRect(110, 390, 298, 21))
        self.xpath_pattern_ejobs.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.xpath_pattern_ejobs.setText("")
        self.xpath_pattern_ejobs.setObjectName("xpath_pattern_ejobs")
        self.layoutWidget5 = QtWidgets.QWidget(self.add_page)
        self.layoutWidget5.setGeometry(QtCore.QRect(110, 260, 291, 23))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gps_lat = QtWidgets.QLineEdit(self.layoutWidget5)
        self.gps_lat.setText("")
        self.gps_lat.setObjectName("gps_lat")
        self.horizontalLayout_5.addWidget(self.gps_lat)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.layoutWidget6 = QtWidgets.QWidget(self.add_page)
        self.layoutWidget6.setGeometry(QtCore.QRect(110, 290, 291, 23))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gps_long = QtWidgets.QLineEdit(self.layoutWidget6)
        self.gps_long.setText("")
        self.gps_long.setObjectName("gps_long")
        self.horizontalLayout_6.addWidget(self.gps_long)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.stack_widgets.addWidget(self.add_page)
        self.remove_page = QtWidgets.QWidget()
        self.remove_page.setObjectName("remove_page")
        self.layoutWidget_2 = QtWidgets.QWidget(self.remove_page)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 50, 501, 33))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(13)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.remove_record_help_btn = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_record_help_btn.sizePolicy().hasHeightForWidth())
        self.remove_record_help_btn.setSizePolicy(sizePolicy)
        self.remove_record_help_btn.setText("")
        self.remove_record_help_btn.setIcon(icon5)
        self.remove_record_help_btn.setIconSize(QtCore.QSize(16, 16))
        self.remove_record_help_btn.setAutoDefault(False)
        self.remove_record_help_btn.setObjectName("remove_record_help_btn")
        self.horizontalLayout_4.addWidget(self.remove_record_help_btn)
        self.remove_records_list = QtWidgets.QListWidget(self.remove_page)
        self.remove_records_list.setGeometry(QtCore.QRect(10, 80, 501, 371))
        self.remove_records_list.setObjectName("remove_records_list")
        self.delete_record_btn = QtWidgets.QPushButton(self.remove_page)
        self.delete_record_btn.setGeometry(QtCore.QRect(400, 450, 113, 32))
        self.delete_record_btn.setObjectName("delete_record_btn")
        self.stack_widgets.addWidget(self.remove_page)
        self.info_page = QtWidgets.QWidget()
        self.info_page.setObjectName("info_page")
        self.version_lbl = QtWidgets.QLabel(self.info_page)
        self.version_lbl.setGeometry(QtCore.QRect(10, 20, 301, 16))
        self.version_lbl.setObjectName("version_lbl")
        self.stack_widgets.addWidget(self.info_page)

        self.retranslateUi(JobSearch)
        self.stack_widgets.setCurrentIndex(1)
        self.search_url_list.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(JobSearch)

    def retranslateUi(self, JobSearch):
        _translate = QtCore.QCoreApplication.translate
        JobSearch.setWindowTitle(_translate("JobSearch", "Job Application Search"))
        self.info_btn.setText(_translate("JobSearch", "..."))
        self.exit_btn.setText(_translate("JobSearch", "..."))
        self.logo_lbl.setText(_translate("JobSearch", "Job Application Search"))
        self.home_btn.setText(_translate("JobSearch", "..."))
        self.add_btn.setText(_translate("JobSearch", "..."))
        self.remove_btn.setText(_translate("JobSearch", "..."))
        self.details_btn.setText(_translate("JobSearch", "Details"))
        self.open_in_browser.setText(_translate("JobSearch", "Browse site"))
        self.select_compan_lbl.setText(_translate("JobSearch", "Select company"))
        self.search_jobs_url_lbl.setText(_translate("JobSearch", "Search jobs"))
        self.find_jobs.setText(_translate("JobSearch", "Find jobs"))
        __sortingEnabled = self.jobs_list.isSortingEnabled()
        self.jobs_list.setSortingEnabled(False)
        self.jobs_list.setSortingEnabled(__sortingEnabled)
        self.company_search_url.setPlaceholderText(_translate("JobSearch", "Search this company careers url"))
        self.company_name.setPlaceholderText(_translate("JobSearch", "Company Name"))
        self.company_email.setPlaceholderText(_translate("JobSearch", "Contact Email"))
        self.xpath_pattern.setPlaceholderText(_translate("JobSearch", "XPath"))
        self.add_record_lbl.setText(_translate("JobSearch", "Add record"))
        self.gps_location_lbl.setText(_translate("JobSearch", "GPS Location"))
        self.label_5.setText(_translate("JobSearch", "XPath"))
        self.add_record_btn.setText(_translate("JobSearch", "Add record"))
        self.company_search_url_bestjobs.setPlaceholderText(_translate("JobSearch", "Include second optional url <bestjobs.ro ?>"))
        self.company_search_url_ejobs.setPlaceholderText(_translate("JobSearch", "Include third optional url <ejobs.ro ?>"))
        self.xpath_pattern_bestjobs.setPlaceholderText(_translate("JobSearch", "XPath bestjobs.ro"))
        self.xpath_pattern_ejobs.setPlaceholderText(_translate("JobSearch", "XPath ejobs.ro"))
        self.gps_lat.setPlaceholderText(_translate("JobSearch", "46.768613"))
        self.label_3.setText(_translate("JobSearch", "latitude"))
        self.gps_long.setPlaceholderText(_translate("JobSearch", "23.584797"))
        self.label_4.setText(_translate("JobSearch", "longitude"))
        self.label_6.setText(_translate("JobSearch", "Remove record"))
        self.delete_record_btn.setText(_translate("JobSearch", "Remove"))
        self.version_lbl.setText(_translate("JobSearch", "Version 1.03072016"))

import jobs.ui.icons_rc