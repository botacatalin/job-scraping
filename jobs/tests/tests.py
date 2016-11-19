"""Test Class"""

import unittest
import sqlite3
import os


class TestDatabase(unittest.TestCase):

    def setUp(self):
        # enable multi thread access
        self.conn = sqlite3.connect("jobs_tests.db", check_same_thread=False)
        self.c = self.conn.cursor()

    def tearDown(self):
        self.c.close()
        self.conn.close()
        try:
            os.remove("jobs_test.db")
        except:
            raise

    def test_test(self):
        """test to see if sqlite3 database is preset"""
        self.db.insert("", self.record)

if __name__ == '__main__':
    unittest.main()
