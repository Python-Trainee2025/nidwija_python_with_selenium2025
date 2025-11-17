import pytest

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

@pytest.mark.parametrize("username,password", [("standard_user","secret_sauce"),("problem_user","secret_sauce"),])
def test_demo(username,password):
    chrome_options=Options()

    driver=webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(3)
    print("Page Title: ", driver.title)
    driver.find_element(By.ID,"user-name").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    print(f"Logging in with username: {username} and password: {password}")
    driver.find_element(By.ID,"login-button").click()

    driver.quit()


