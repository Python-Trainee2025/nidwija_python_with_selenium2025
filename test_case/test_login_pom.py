import logging
import time


from selenium.webdriver.common.by import By

from page_objects.loginpom.loginpage import LoginPage
from setup.basetest import BaseTest


class TestLoginPom(BaseTest):
    def test_demo_login_basetest_pom(self):
        login=LoginPage(self.driver)

        self.driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        print("Page Title: ", self.driver.title)
        login.login(username="standard_user")
        # self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        logging.info(("Username entered successfully"))
        self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        logging.info(("Password entered successfully"))
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(4)
        self.driver.find_element(By.CLASS_NAME,'inventory_item_name ').click()



