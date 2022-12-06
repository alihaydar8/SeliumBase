from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service


class CommonOps :
    def __init__(self,driver):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='107.0.5304.62').install()))
        self.wait = WebDriverWait(self.driver, 10)
