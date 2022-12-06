import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='107.0.5304.62').install()))
    self.driver.implicitly_wait(30)
    self.wait = WebDriverWait(self.driver, 10)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.close()
    self.driver.quit()
  
  def test_login(self):
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username = self.driver.find_element(By.NAME,"username")
    password = self.driver.find_element(By.NAME,"password")
    if username.is_displayed() and password.is_displayed():
        username.click()
        username.send_keys("Admin")
        password.clear()
        password.send_keys("admin123")
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
    if  self.driver.find_element(By.LINK_TEXT,"Leave").is_displayed():
        assert self.driver.find_element(By.LINK_TEXT,"Leave"),"element Leave not fund"
        assert self.driver.find_element(By.LINK_TEXT,"My Info"),"element My Info not fund"
    
# pytest test_login.py --html=test_login.html