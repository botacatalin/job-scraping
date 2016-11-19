"""
    Table setup

company
----------------------------------------------------------------------------------------------------------------------
date_stamp (DATE) | company_name(TEXT) | contact_email(TEXT) | gps_lat(REAL) | gpp_long(REAL)
----------------------------------------------------------------------------------------------------------------------

urls
----------------------------------------------------------------------------------------------------------------------
date_stamp (DATE) | company_name(TEXT) | job_url(TEXT) | xpath(TEXT) |

----------------------------------------------------------------------------------------------------------------------

"""


import sqlite3

# TODO check different way to connect to db besides conn.cursor()
class DB:
    # enable multi thread access
    conn = sqlite3.connect("jobs.db", check_same_thread=False)
    c = conn.cursor()

    def create_table(self):
        self.c.execute(
            'CREATE TABLE IF NOT EXISTS '
            'company(date_stamp TEXT, company_name TEXT, '
            'contact_email TEXT, gps_lat REAL, gps_long REAL);')

        self.c.execute(
            'CREATE TABLE IF NOT EXISTS '
            'urls(date_stamp TEXT, company_name TEXT, '
            'job_url TEXT, xpath TEXT);')

    def close_db(self):
        self.conn.close()
        self.c.close()

    def insert_company(self, date_stamp, record):
        try:
            self.c.execute('INSERT INTO company(date_stamp, company_name,'
                           'contact_email, gps_lat, gps_long) VALUES(?,?,?,?,?)',
                           (date_stamp, record.company_name,
                            record.company_email, record.gps_lat, record.gps_long))
            self.conn.commit()

        except sqlite3.Error:
            raise sqlite3.Error

    def insert_url(self, date_stamp, record):
        try:
            self.c.execute('INSERT INTO urls(date_stamp, company_name,'
                           'job_url, xpath) VALUES(?,?,?,?)',
                           (date_stamp, record.company_name,
                            record.search_url, record.xpath_pattern))

            self.conn.commit()

        except sqlite3.Error:
            raise sqlite3.Error

    def remove(self, company_name):
        """ Remove company name from database. If company_name not existent do nothing """
        self.c.execute('DELETE FROM company WHERE company_name=?', (company_name,))
        self.conn.commit()
        self.c.execute('DELETE FROM urls WHERE company_name=?', (company_name,))
        self.conn.commit()

    def get_all_company_names(self):
        records = self.c.execute("SELECT company_name FROM company")
        return records

    def get_company_name(self, job_url):
        records = self.c.execute('SELECT company_name FROM urls WHERE job_url=? LIMIT 1', (job_url,))
        return records.fetchone()[0]

    def get_company_search_url(self, company_name):
        records = self.c.execute('SELECT job_url FROM urls WHERE company_name=?', (company_name,))
        return records

    def get_url_xpath(self, job_url):
        records = self.c.execute('SELECT xpath FROM urls WHERE job_url=? LIMIT 1', (job_url,))
        # returns first position of one element tuple
        return records.fetchone()[0]

    def get_all_company_urls_and_xpath(self):
        records = self.c.execute("SELECT job_url,xpath FROM urls")
        all_records = records.fetchall()
        # returns a dictionary {job_url : xpath }
        return {a[0]: a[1] for a in all_records}
