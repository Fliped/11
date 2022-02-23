# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Get10(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_get10(self):
        driver = self.driver
        driver.get("http://173.195.74.89:1880/ui/#!/3?socketid=3L8sjuoxcbBTOr7LAAAF")
        driver.find_element_by_xpath("//body[@id='nr-dashboard']/md-content/section/md-sidenav/md-list/md-list-item[2]/div/button").click()
        driver.find_element_by_id("input_62").clear()
        driver.find_element_by_id("input_62").send_keys("820134")
        driver.find_element_by_id("input_63").clear()
        driver.find_element_by_id("input_63").send_keys("820134")
        driver.find_element_by_xpath("//div[@id='getRequest_getRequest_cards']/md-card/form/div[3]/md-input-container/md-checkbox/div").click()
        driver.find_element_by_id("input_65").clear()
        driver.find_element_by_id("input_65").send_keys("10")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        self.assertTrue(driver.find_element_by_xpath("//body[@id='nr-dashboard']/md-toast/div/div").is_displayed())
        self.assertEqual("Sent \"0A0908A6873252030A010A\"", driver.find_element_by_xpath("//body[@id='nr-dashboard']/md-toast/div/div").text)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main(False)
   
