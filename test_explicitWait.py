# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait


class TestExplicitWait():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(service=Service('C:\\Formation\\WebDriver\\chromedriver.exe'))
    self.driver.implicitly_wait(30)
    self.wait = WebDriverWait(self.driver, 10)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.close()
    self.driver.quit()
    pass
  
  def test_explicit_wait(self):
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    self.driver.find_element(By.NAME,"username").clear()
    self.driver.find_element(By.NAME, "username").send_keys("Admin")
    self.driver.find_element(By.NAME, "password").clear()
    self.driver.find_element(By.NAME, "password").send_keys("admin123")
    btn = self.driver.find_element(By.CSS_SELECTOR, ".oxd-button")
    if self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button"))) :
      btn.click()
    element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT,"My Info")))
    element.click()

    assert self.driver.find_element(By.LINK_TEXT,"Personal Details"),"element Leave not fund"

  
# pytest test_explicitWait.py --html=test_explicitWait.html