'''
Test the success opening of a website, using its page title, URL and a displayed Search web element
to indicate a successful loaded page.
'''

import unittest
from selenium import webdriver
from Package1 import Util
import time


class Test1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Start of {}".format(cls.__name__))
        global driver, path
        driver = webdriver.Chrome(executable_path="C:\\BrowserDrivers\\chromedriver_win32\\chromedriver.exe")
        path = "C:/works/PyCharm/SeleniumPython/Package1/TCdata/TC1.xlsx"  # Test data file
        cell = (2,5)    # Common URL for all test cases
        driver.get(Util.getCellData(path, cell))
        time.sleep(3)

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

    def test_TC_1_1(self):
        Util.setCellData(path, (3, 3), "")  # Clear result cell prior to starting test
        pageTitle = driver.title
        cell = (3, 6)   # Cell of expected title
        expect = Util.getCellData(path, cell)
#        self.assertEqual(expect, pageTitle,\
#                         "Page Title Mismatched.\n\tExpected: '{}'\n\tActual:   '{}'".format(expect, pageTitle))
        if expect == pageTitle:
            Util.setCellData(path, (3, 3), "Passed")
        else:
            Util.setCellData(path, (3, 3), "Failed")

    def test_TC_1_2(self):
        Util.setCellData(path, (4, 3), "")  # Clear result cell prior to starting test
        pageURL = driver.current_url
        cell = (4, 6)   # Cell of expected url
        expect = Util.getCellData(path, cell)
#        self.assertEqual(expect, pageURL,\
#                         "Page URL Mismatched.\n\tExpected: '{}'\n\tActual:   '{}'".format(expect, pageURL))
        if expect == pageURL:
            Util.setCellData(path, (4, 3), "Passed")
        else:
            Util.setCellData(path, (4, 3), "Failed")

    def test_TC_1_3(self):
        Util.setCellData(path, (5, 3), "")  # Clear result cell prior to starting test
        cell = (5, 6)   # Cell of xpath to 'Search' box
        ele = driver.find_element_by_xpath(Util.getCellData(path, cell))
 #       self.assertTrue(ele.is_displayed())
        if ele:
            Util.setCellData(path, (5, 3), "Passed")
        else:
            Util.setCellData(path, (5, 3), "Failed")


if __name__ == "__main__":
    unittest.main()
