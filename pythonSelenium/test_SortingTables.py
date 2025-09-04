import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_sort(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.maximize_window()
    browserSortedVeggies = []
    # click on column headed
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
    # collect all veggie names -> BrowserSortedveggieList
    veggieElements = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")

    for ele in veggieElements:
        browserSortedVeggies.append(ele.text)

    originalBrowserSortedList = browserSortedVeggies.copy()

    # sort this BrowserSortedveggieList => newSortedList

    browserSortedVeggies.sort()
    # veggieList == newSortedList
    assert browserSortedVeggies == originalBrowserSortedList

    #
    # for product2 in productNames:
    #     print(product2.text)



