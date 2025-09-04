import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client/#/auth/login")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()

driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello@9912")
driver.find_element(By.XPATH,"//form/div[3]/input").send_keys("Hello@9912")
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
#driver.find_element(By.XPATH,"//button[@type='submit']").click()

#practiceemail45@gmail.com email
#Bs123456789 password





time.sleep(2)