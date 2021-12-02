from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.common.exceptions import TimeoutException


url_rpma_getrequest="http://173.195.74.89:1880/ui/#!/1?socketid=NE09In4uXT5dU--YAAVV"
#url_rpma_setrequest="http://173.195.74.89:1880/ui/#!/2?socketid=NE09In4uXT5dU--YAAVV"
Node_id="820134"
Node_id_Xpath='//*[@id="input_0"]'
cor_id='12'
cor_id_Xpath="//*[@id='input_1']"
object_id='10'
object_id_Xpath="//*[@id='input_3']"
request_sumbit_button_Xpath='//*[@id="getRequest_getRequest_cards"]/md-card/form/div[6]/button[1]'
result_Xpath='//*[@id="nr-dashboard"]/md-toast/div/div/h4'
result_Xpath_01='//*[@id="nr-dashboard"]/md-toast/div/div/h4/text()'




web=webdriver.Chrome()
'''打开web'''
def open_web(url):
    web.get(url)
    web.fullscreen_window()
    time.sleep(5)

'''定位+输入'''
def input_text(Location_type,Xpath_value,text):
    web_text=web.find_element(by=Location_type,value=Xpath_value)
    web_text.clear()
    web_text.send_keys(text)
    time.sleep(1)

def click_button(Location_type,Xpath_value):
    web.find_element(by=Location_type,value=Xpath_value).click()
    time.sleep(3)


    
open_web(url_rpma_getrequest)
input_text(By.XPATH,Node_id_Xpath,Node_id)
input_text(By.XPATH,cor_id_Xpath,cor_id)
input_text(By.XPATH,object_id_Xpath,object_id)
click_button(By.XPATH,request_sumbit_button_Xpath)

'''获取结果'''
#  Example:
#             from selenium.webdriver.support.ui import WebDriverWait \n
#             element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId")) \n
#             is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).\ \n
#                         until_not(lambda x: x.find_element_by_id("someId").is_displayed())
#element=web.find_element_by_xpath(result_Xpath)
is_appeared=WebDriverWait(web,300,1,(ElementNotVisibleException)).until_not(lambda web:web.find_element_by_xpath(result_Xpath).is_displayed())
#is_appeared=WebDriverWait(web,300,1).until(lambda web: web.find_element_by_xpath(result_Xpath).is_displayed())
print(is_appeared)
if is_appeared:
    #element1=web.find_element_by_xpath(result_Xpath)
    print("is_appeared")
    #print(element1)
else:
    print("wu")




