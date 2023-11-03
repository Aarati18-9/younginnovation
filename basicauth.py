import time

from selenium import webdriver


# this is used because it has authentication popup
def basic_auth():
    de = webdriver.Chrome()
    de.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
    time.sleep(5)


basic_auth()
