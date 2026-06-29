# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class AppDynamicsJob3(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://proyecto-formulario-1.onrender.com/")
        driver.find_element(By.XPATH,"//input[@type='text']").click()
        driver.find_element(By.XPATH,"//input[@type='text']").clear()
        driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Juan")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/div/form/div[2]/div/div[2]/div/input").clear()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/div/form/div[2]/div/div[2]/div/input").send_keys("Perez")
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/div/form/div[2]/div/div[3]/div/input").clear()
        driver.find_element(By.XPATH,"//div[@id='app']/div/div/div/form/div[2]/div/div[3]/div/input").send_keys("44462927")
        driver.find_element(By.XPATH,"//input[@type='tel']").clear()
        driver.find_element(By.XPATH,"//input[@type='tel']").send_keys("12345678")
        driver.find_element(By.XPATH,"//input[@type='email']").clear()
        driver.find_element(By.XPATH,"//input[@type='email']").send_keys("pachi@test")
        file_inputs = driver.find_elements(By.XPATH, "//input[@type='file']")
        file_inputs[0].send_keys(os.path.join(BASE_DIR, "fixtures", "dni.png"))
        file_inputs[1].send_keys(os.path.join(BASE_DIR, "fixtures", "tax.png"))
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "//div[contains(text(),'Formato incorrecto')]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to.alert
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
