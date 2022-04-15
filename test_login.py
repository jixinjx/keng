#!/usr/bin/env Python
# coding=utf-8
# -*- coding: utf-8 -*-
import sys
import time
reload( sys )
sys.setdefaultencoding('utf-8')
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.youbianku.com/%E9%A6%96%E9%A1%B5")
        self.assertIn("首页", driver.title,"邮编库 is not in title")
        search_form = driver.find_element_by_id('mySearchInput')
        search_form.send_keys(u"南京市")
        search_form.send_keys(Keys.RETURN)
        time.sleep(10)




    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()