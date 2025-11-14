import time


from selenium.webdriver.common.by import By

from setup.basetest import BaseTest


class TestLogin(BaseTest):
    def test_demo_login(self):

        self.driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        print("Page Title: ", self.driver.title)
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        self.driver.find_element(By.ID,"login-button").click()



