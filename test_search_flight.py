# coding=utf-8
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys
print (sys.path)

class MyTestCase(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()

    def test_something(self):
        driver = self.driver
        driver.get("https://us.ceair.com/zh/flight-result.html")
        self.assertIn(u"中国东方航空", driver.title, "中国东方航空 is not in title")
        Departure=driver.find_element_by_xpath("//*[@id='statusform']")
        Departure.click()
        Departure.send_keys(u"上海")
        list=driver.find_elements_by_xpath("//*[@class='autocomplete-list-box']/div[@class='search-menu-container']/li/div/div")
        sleep(2)
        Destination=driver.find_element_by_xpath("//*[@id='findRouteMain']/div[2]/div[1]/form/div[3]/div/input")
        Destination.click()
        Destination.send_keys(Keys.DOWN)
        Destination.send_keys(Keys.DOWN)
        sleep(2)
        submit=driver.find_element_by_xpath("//*[@id='findRouteMain']/div[2]/div[2]/button")
        submit.click()
        sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
