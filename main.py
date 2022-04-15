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

def get_content():
    driver = webdriver.Chrome()
    title_list = []
    temp_data = []
    out_pd = pandas.DataFrame()
    for page in range(3):
        page = page + 1
        driver.get("http://fz.people.com.cn/skygb/sk/index.php/Index/index/" + str(page) + "?p=1")
        title = driver.find_elements_by_tag_name("th")
        if page == 1:
            for i in title:
                if (i.text != ""):
                    print i.text
                    title_list.append(i.text)
            print(title)
            data = pandas.DataFrame(columns=title_list)
            out_pd=data

        content = driver.find_element_by_class_name("jc_a").find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")
        for i in content:
            temp = []
            span=i.find_elements_by_tag_name("span")
            for n in range(7):
                if (span[n].text == ""):
                    temp.append(" ")
                    continue
                print(span[n].text)
                temp.append(span[n].text)
            size=out_pd.index.size
            out_pd.loc[size]=temp
        print(out_pd)
    driver.close()
    out_pd.to_csv("result.csv", sep=',',index="false")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        get_content()
        print("爬取成功")
    except:
        print("爬取失败")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
