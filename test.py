#coding=utf-8
from time import sleep
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://us.ceair.com/zh/flight-result.html")

Departure=driver.find_element_by_xpath("//*[@id='statusform']")
Departure.click()
Departure.send_keys(u"上海")
sleep(2)
list=driver.find_element_by_xpath("//*[@class='autocomplete-list-box']").text
# list=driver.find_elements_by_xpath("//*[@class='autocomplete-list-box']/*[@class='search-menu-container']/*["
#                                    "@class='search-item-container']/div/div[@class=' search-result-airport  flex "
#                                    "al-center']/div/span[contains(text(),'虹桥')]").get_attribute("class")
print(list)
# for i in range(len(list)):
#    print(list[i].find_elements_by_class_name("search-result-airport-1").text)


##//////////////*#558#*
sleep(2)
