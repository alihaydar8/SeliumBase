from selenium import webdriver # pip install –U selenium
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager #  pip install webdriver-manager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='107.0.5304.62').install()))
driver.implicitly_wait(30) 
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window() # maximiser
driver.minimize_window() # minimiser
driver.fullscreen_window()
driver.get_screenshot_as_file("fullscreenshot.png")
driver.find_element(By.CSS_SELECTOR,".orangehrm-login-slot").screenshot("form.png")
driver.find_element(By.NAME,"username").screenshot("username.png")

# python Capture_ecran_3_4.py 