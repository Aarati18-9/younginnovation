import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# checking login for my project called farm trading
def basic_auth():
    de = webdriver.Chrome()
    de.get("http://localhost:5173/")
    de.find_element(By.XPATH, "//input[@placeholder='Enter your email address']").send_keys("admin@admin.com")
    de.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("admin123")
    de.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    time.sleep(10)


basic_auth()
