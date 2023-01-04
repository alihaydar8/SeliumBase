import pytest
from selenium.webdriver.common.by import By

URL =  "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = URL 
    
    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        username_input = self.driver.find_element(By.NAME,"username")

        username_input.send_keys(username)
        password_input = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, ".oxd-button")
        password_input.send_keys(password)
        submit_button.click()

    def checklogin(self):
        assert self.driver.find_element(By.LINK_TEXT, "Admin"),"ERROR LOGIN"
