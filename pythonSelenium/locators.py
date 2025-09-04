import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

#Support for ID, CSSselectors, classname, name, linkText

driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234567")
driver.find_element(By.ID,"exampleCheck1").click()
#CSS - tagname[attribute='value'] // don't need // and @ when using css selector #id .classname also allowed
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Emmanuel")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()


#static dropdowns
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value()

# //tagname[@attribute='value']   don't forget // and @ when using xpaths
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Helloagain")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()


time.sleep(2)