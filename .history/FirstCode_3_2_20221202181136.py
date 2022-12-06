from selenium import webdriver # pip install –U selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 

driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='107.0.5304.62').install()))
driver.implicitly_wait(30) 
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.get("https://google.com")
print("----------------------------------") 
print("URL:"+ driver.current_url)
print("title:"+ driver.title) 
print("----------------------------------") 
print("BACK")
driver.back() 
print("URL:"+ driver.current_url)
print("title:"+ driver.title) 
print("----------------------------------") 
print("FORWAR")
driver.refresh()  
driver.forward() 
print("URL:"+ driver.current_url)
print("title:"+ driver.title) 
print("----------------------------------") 
driver.refresh() 
driver.close() 
driver.quit() 


# pytest FirstCode_3_2.py --html=FirstCode_3_2.html