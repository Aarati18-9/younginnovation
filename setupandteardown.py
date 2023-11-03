import time

from selenium import webdriver


def teardown_function():
    de = webdriver.Chrome()
    de.get("https://www.google.com")
    time.sleep(3)


teardown_function()
