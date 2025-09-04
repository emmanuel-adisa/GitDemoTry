import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
time.sleep(3)
driver.switch_to.frame("mce_0_ifr") #can use id or name value
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")
driver.switch_to.default_content() #switch back to normal browser scope
print(driver.find_element(By.CSS_SELECTOR,"h3").text)