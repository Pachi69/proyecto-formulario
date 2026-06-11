# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestArticleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.base_url = "https://www.google.com/"
        cls.verificationErrors = []
        cls.accept_next_alert = True

    def test_valid_code_displays_article_details(self):
        driver = self.driver
        driver.get("https://um-2025-articulos.tiiny.site/")
        driver.find_element(By.ID,"code").click()
        driver.find_element(By.ID,"code").clear()
        driver.find_element(By.ID,"code").send_keys("1111111111111")
        driver.find_element(By.ID,"search").click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "alert")))

    def test_nonexistent_code_displays_not_found_alert(self):
        driver = self.driver
        driver.get("https://um-2025-articulos.tiiny.site/")
        driver.find_element(By.ID,"code").click()
        driver.find_element(By.ID,"code").clear()
        driver.find_element(By.ID,"code").send_keys("1111111111112")
        driver.find_element(By.ID,"search").click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "alert")))
        try: self.assertEqual(u"Artículo no encontrado", driver.find_element(By.ID,"alert").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertFalse(self.is_element_present(By.CSS_SELECTOR, "#code.required"))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "alert")))
        self.assertFalse(self.is_element_present(By.CSS_SELECTOR, "#article-info:not(.d-none)"))

    def test_malformed_barcode_displays_validation_error(self):
        driver = self.driver
        driver.get("https://um-2025-articulos.tiiny.site/")
        driver.find_element(By.ID,"code").click()
        driver.find_element(By.ID,"code").clear()
        driver.find_element(By.ID,"code").send_keys("11111111111121")
        driver.find_element(By.ID,"search").click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "alert")))
        try: self.assertEqual(u"El código de barras debe tener entre 1 y 13 caracteres de longitud", driver.find_element(By.ID,"alert").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#code.required"))

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

    @classmethod
    def tearDownClass(cls):
        try:
            cls.driver.quit()
        except Exception:
            pass
        cls().assertEqual([], cls.verificationErrors)

if __name__ == "__main__":
    unittest.main()
