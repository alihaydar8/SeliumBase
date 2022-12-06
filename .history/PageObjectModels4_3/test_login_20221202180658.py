import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from LoginPage import Login

URL =  "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
ORANGE_HRM_LOCATOR_USERNAME = (By.NAME,"username")
ORANGE_HRM_LOCATOR_PASSWORD = (By.NAME, "password")
ORANGE_HRM_LOCATOR_SUBMIT_BTN = (By.CSS_SELECTOR, ".oxd-button")
ORANGE_HRM_LOCATOR_ADMIN = (By.LINK_TEXT, "Admin")
ORANGE_HRM_USERNAME = "Admin"
ORANGE_HRM_PASSWORD = "admin123"

class TestLogin():

  def setup_method(self, method):
    self.Login = Login(URL)
  
  def teardown_method(self, method):
    self.Login.close_and_close()
  
  def test_login(self):
    self.Login.enter_login_username(ORANGE_HRM_LOCATOR_USERNAME,ORANGE_HRM_USERNAME)
    self.Login.enter_login_password(ORANGE_HRM_LOCATOR_PASSWORD,ORANGE_HRM_PASSWORD)
    self.Login.click_login_button(ORANGE_HRM_LOCATOR_SUBMIT_BTN)
    self.Login.check_conextion_with_Link_Text_Present(ORANGE_HRM_LOCATOR_ADMIN)
  
# pytest test_login.py --html=test_login.html


    





