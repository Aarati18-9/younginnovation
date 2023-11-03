import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def checkboxes_function():
    de = webdriver.Chrome()
    de.get("https://the-internet.herokuapp.com/checkboxes")
    check1 = de.find_element(By.XPATH, "//input[1]")
    check2 = de.find_element(By.XPATH, "//input[2]")
    if not check1.is_selected():
        check1.click()
        print(check1.is_selected())
    if check2.is_selected():
        check2.click()
        print(check2.is_selected())


checkboxes_function()
