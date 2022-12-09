import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

############################ Avant de lancer le code faire tourner docker 
# ################## docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:4.7.0-20221202 
class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor="http://chrome:4444/wd/hub", options=webdriver.ChromeOptions())
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
    
# pytest test_login_remote_server.py --html=html/test_login_remote_server.html
