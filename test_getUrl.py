import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class TestgetUrl():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(service=Service('C:\\Formation\\WebDriver\\chromedriver.exe'))
    self.driver.implicitly_wait(30)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.close()
    self.driver.quit()
  
  def test_get_url(self):
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login','ERROR url not match'
    assert self.driver.title == 'OrangeHRM','ERROR title not match'
  
# pytest test_getUrl.py --html=html/test_getUrl.html