import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class TestchangeWindow():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(service=Service('C:\\Formation\\WebDriver\\chromedriver.exe'))
    self.driver.implicitly_wait(30)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.close()
    self.driver.quit()
    pass
  
  def test_change_window(self):
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    self.driver.execute_script("window.open('')")
    self.driver.switch_to.window(self.driver.window_handles[1]) # La façon la plus sûr est de déterminer quelle fenêtre est la fenêtre actuellement ouverte est d'utiliser l'attribut driver.find_element().title mentionné précédemment
    self.driver.get("https://python.org")
    self.driver.switch_to.window(self.driver.window_handles[0])
    self.driver.find_element(By.NAME,"username").clear()
    self.driver.find_element(By.NAME,"username").send_keys("Admin")
    assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login','ERROR url not match'
    assert self.driver.title == 'OrangeHRM','ERROR title not match'

# pytest test_changeWindow.py