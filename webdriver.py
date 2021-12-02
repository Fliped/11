from selenium import webdriver
import time



#def Web():
driver=webdriver.Chrome()

#driver.get("http://173.195.74.89:1880/ui/#!/1?socketid=lDX1xF3uIzs3MaafAATX") #RPMA Web
driver.get('https://www.baidu.com/')

driver.find_element_by_name('wd').send_keys("zhihu")
driver.find_element_by_id('su').click()

serach_link=driver.find_elements_by_class_name("result")



#Web()
