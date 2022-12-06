from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Login :
  
    def __init__(self,url):
        # options = Options()
        # options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='107.0.5304.62').install()))
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(30)
        self.driver.get(url)

    def wait_for(self,locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def wait_to_be_clickable(self,locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find(self,locator):
        if(self.driver.find_element(*locator).is_displayed()):
            return self.driver.find_element(*locator)
    
    def enter_login_username(self,locator,username):
        self.wait_for(locator).clear()
        self.find(locator).send_keys(username)
    
    def enter_login_password(self,locator,password):
        self.wait_for(locator).clear()
        self.find(locator).send_keys(password)

    def click_login_button(self,locator):
        self.wait_to_be_clickable(locator).click()
    
    def check_conextion_with_Link_Text_Present(self,locator):
        print ((self.find(locator)))

ORANGE_HRM_LOCATOR_USERNAME = (By.NAME,"username")
ORANGE_HRM_LOCATOR_PASSWORD = (By.NAME, "password")
ORANGE_HRM_LOCATOR_SUBMIT_BTN = (By.CSS_SELECTOR, ".oxd-button")
ORANGE_HRM_LOCATOR_ADMIN = (By.LINK_TEXT, "Admin")
ORANGE_HRM_USERNAME = "Admin"
ORANGE_HRM_PASSWORD = "admin123"

URL =  "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

Login = Login(URL)
Login.enter_login_username(ORANGE_HRM_LOCATOR_USERNAME,ORANGE_HRM_USERNAME)
Login.enter_login_password(ORANGE_HRM_LOCATOR_PASSWORD,ORANGE_HRM_PASSWORD)
Login.click_login_button(ORANGE_HRM_LOCATOR_SUBMIT_BTN)
Login.check_conextion_with_Link_Text_Present(ORANGE_HRM_LOCATOR_ADMIN)
