from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        try:
            login_button = driver.find_element_by_xpath(
                "//a[@href='/accounts/login/?source=auth_switcher']"
            )
            login_button.click()
        except:
            print('já estamos na página de login')
            pass
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        time.sleep(random.randint(1, 3))
        user_element.send_keys(self.username)
        time.sleep(random.randint(1, 3))
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(random.randint(1, 3))
        password_element.send_keys(Keys.RETURN)
        time.sleep(random.randint(1, 2))
        driver.get('https://www.instagram.com/vitim_gone/')
        print('Logado no instagram')





vitor=InstagramBot('login','senha')
vitor.login()
