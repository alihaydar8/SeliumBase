import pytest
import time
import json
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service



class TestSelectElement():
  def setup_method(self, method):
    logging.basicConfig(level=logging.WARNING)
    self.driver = webdriver.Chrome(service=Service('C:\\Formation\\WebDriver\\chromedriver.exe'))

    self.driver.implicitly_wait(30)
    self.wait = WebDriverWait(self.driver, 10)
    self.vars = {}
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    self.driver.find_element(By.NAME,"username").clear()
    self.driver.find_element(By.NAME, "username").send_keys("Admin")
    self.driver.find_element(By.NAME, "password").clear()
    self.driver.find_element(By.NAME, "password").send_keys("admin123")
    logging.info("hello")
    logging.warning("hello")
    logging.debug("hello")
    text = self.driver.find_element(By.NAME,"username").text
    logging.info(self.driver.find_element(By.NAME,"username").text)
    logging.warning(self.driver.find_element(By.NAME,"username").tag_name)
    logging.debug(self.driver.find_element(By.NAME,"username").text)
    btn = self.driver.find_element(By.CSS_SELECTOR, ".oxd-button")
    if self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button"))) :
      btn.click()
  
  def teardown_method(self, method):
    self.driver.close()
    self.driver.quit()
    pass
  
  def test_select_element(self):
    admin = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT,"Admin")))
    admin.click()
    element = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[7]/div[1]/div[1]/div[1]")
    element.click()
    element.click()
    # assert not element.is_enabled()

   



  
# pytest test_login.py --html=test_login.html