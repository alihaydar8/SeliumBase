from selenium import webdriver # pip install –U selenium
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager #  pip install webdriver-manager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='107.0.5304.62').install()))
driver.implicitly_wait(30) 
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.fullscreen_window()
driver.find_element(By.CSS_SELECTOR,".orangehrm-login-slot").screenshot("form_find_by_CSS_SELECTOR.png")
driver.find_element(By.NAME,"username").screenshot("username_find_by_name.png")
driver.find_element(By.TAG_NAME,"img").screenshot("img_login_find_by_TAG_NAME.png")
driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]").screenshot("password_find_by_XPATH.png")
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").screenshot("OrangeHRM_find_by_LINK_TEXT.png")
driver.find_element(By.ID,"app").screenshot("app_find_by_ID.png")
