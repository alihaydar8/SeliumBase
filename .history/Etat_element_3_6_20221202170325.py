from selenium import webdriver # pip install –U selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
driver = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", options=webdriver.ChromeOptions())
# driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='107.0.5304.62').install()))
driver.implicitly_wait(30)
wait = WebDriverWait(driver, 10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.NAME,"username").clear()
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").clear()
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
driver.find_element(By.LINK_TEXT, "Admin").click()
element = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[3]")

if wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[3]"))):
    print("class = ",element.get_attribute("class"))
    print("size = ",element.size)
    print("text = ",element.text)
    print("tag_name = ",element.tag_name)
    print("element displayed : ",element.is_displayed())
    print("location = ",element.location)
    element.screenshot("element.png") 
