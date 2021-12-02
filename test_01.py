from selenium import webdriver
import time

'''
getRequest page test case
''' 
driver=webdriver.Chrome()
driver.get("http://173.195.74.89:1880/ui/#!/1?socketid=SN88Dbtblr4q8BnDAAT0")
driver.fullscreen_window()
time.sleep(10)
#driver.switch_to_frame('')
UlpNodeId=driver.find_element_by_xpath('//*[@id="input_0"]')
UlpNodeId.clear()
UlpNodeId.send_keys("820134")
correlationId=driver.find_element_by_xpath('//*[@id="input_1"]')
correlationId.clear()
correlationId.send_keys("5555")
objectId=driver.find_element_by_xpath('//*[@id="input_3"]')
sumbit=driver.find_element_by_xpath('//*[@id="getRequest_getRequest_cards"]/md-card/form/div[6]/button[1]')
sumbit.click()
time.sleep(5)




