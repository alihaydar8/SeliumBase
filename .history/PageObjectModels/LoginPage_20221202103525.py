from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Login :
  
    def __init__(self,driver):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='107.0.5304.62').install()))
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(30)

    def wait_for(self,locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def wait_to_be_clickable(self,locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find(self,locator):
        return self.driver.find_element(*locator)
    
    def enter_login_username(self,locator,username):
        self.wait_for(locator).clear()
        self.find(locator).send_keys(username)
    
    def enter_login_password(self,locator,password):
        self.wait_for(locator).clear()
        self.find(locator).send_keys(password)

    def click_login_button(self,locator):
        self.wait_to_be_clickable(locator).click()


Orange_HRM_LOCATOR_USERNAME = (By.NAME,"username")
Orange_HRM_LOCATOR_PASSWORD = (By.NAME, "password")
Orange_HRM_LOCATOR_SUBMIT_BTN = (By.CSS_SELECTOR, ".oxd-button")

Orange_HRM_USERNAME = "Admin"
Orange_HRM_PASSWORD = "admin123"

Login = Login()
Login.enter_login_username(Orange_HRM_LOCATOR_USERNAME,Orange_HRM_USERNAME)
Login.enter_login_password(Orange_HRM_LOCATOR_PASSWORD,Orange_HRM_PASSWORD)
Login.click_login_button(Orange_HRM_LOCATOR_SUBMIT_BTN)