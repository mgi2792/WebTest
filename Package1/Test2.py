'''
Test the navigation between websites using driver's back() and forward() functions.
'''

import unittest
from selenium import webdriver
from Package1 import Util
import time


class Test2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Start of {}".format(cls.__name__))
        global driver, path
        driver = webdriver.Chrome(executable_path="C:\\BrowserDrivers\\chromedriver_win32\\chromedriver.exe")
        path = "C:/works/PyCharm/SeleniumPython/Package1/TCdata/TC2.xlsx"  # Test data file

    @classmethod
    def tearDownClass(cls):
        driver.quit()
        print("End of {}".format(cls.__name__))

    @classmethod
    def setUp(self):
        pass

    @classmethod
    def tearDown(self):
        pass

    def test_TC_2_1(self):
        Util.setCellData(path, (3, 3), "")  # Clear result cell prior to starting test
        cell = (3, 5)  # Cell of URL-1
        driver.get(Util.getCellData(path, cell))
        time.sleep(5)
        pageTitle = driver.title
        cell = (3, 7)  # Cell of expected title
        expect = Util.getCellData(path, cell)
        self.assertEqual(expect, pageTitle,\
                         "Page Title Mismatched.\n\tExpected: '{}'\n\tActual:   '{}'".format(expect, pageTitle))

        cell = (3, 6)  # Cell of URL-2
        driver.get(Util.getCellData(path, cell))
        time.sleep(5)
        pageTitle = driver.title
        cell = (3, 8)  # Cell of URL-2
        expect = Util.getCellData(path, cell)
        self.assertEqual(expect, pageTitle,\
                         "Page Title Mismatched.\n\tExpected: '{}'\n\tActual:   '{}'".format(expect, pageTitle))

        driver.back()

        time.sleep(5)
        pageTitle = driver.title
        cell = (3, 7)  # Cell of expected title
        expect = Util.getCellData(path, cell)
        self.assertEqual(expect, pageTitle,\
                         "Page Title Mismatched.\n\tExpected: '{}'\n\tActual:   '{}'".format(expect, pageTitle))

        driver.forward()

        time.sleep(5)
        pageTitle = driver.title
        cell = (3, 8)  # Cell of URL-2
        expect = Util.getCellData(path, cell)
        self.assertEqual(expect, pageTitle,\
                         "Page Title Mismatched.\n\tExpected: '{}'\n\tActual:   '{}'".format(expect, pageTitle))
        if expect == pageTitle:
            Util.setCellData(path, (3, 3), "Passed")
        else:
            Util.setCellData(path, (3, 3), "Failed")

if __name__ == '__main__':
    unittest.main()
