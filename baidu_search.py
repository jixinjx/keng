# coding=utf-8
import unittest
from time import sleep
import pandas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys
print (sys.path)

reload(sys)
sys.setdefaultencoding('utf-8')
class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_something(self):

        driver = self.driver
        title_list = []
        temp_data = []
        out_pd=pandas.DataFrame()
        for page in range(2):
            page=page+2
            driver.get("http://fz.people.com.cn/skygb/sk/index.php/Index/index/"+str(page)+"?p=1")
            title = driver.find_elements_by_tag_name("th")

            for i in title:
                if (i.text != ""):
                    print i.text
                    title_list.append(i.text)
            print(title)
            data = pandas.DataFrame(columns=title_list)
            content = driver.find_element_by_class_name("jc_a").find_element_by_tag_name("tbody")
            all = content.find_elements_by_tag_name("span")

            for i in all:
                if (i.text != ""):
                    print i.text
                    temp_data.append(i.text)

        with open('data.txt','w') as f:
            for i in range(7):
                f.write(title_list[i]+"\t")
            f.write('\n')
            for n in range(len(temp_data)/7):
                for i in range(7):
                    f.write(temp_data.pop(0) + '\t')
                f.write('\n')


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
