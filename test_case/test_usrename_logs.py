

import logging

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.info("Logger initialized for test_logs")
class TestLogs:
    def test_username_logs(self):
        chrome_options=Options()

        driver=webdriver.Chrome(options=chrome_options)

        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        user_list=driver.find_elements(By.XPATH,'//div[@id="login_credentials"]')
        time.sleep(3)
        accepted_user=[]
        for i in user_list:
            logger.info(f"{i.text}")
            accepted_user.append(i.text)
            time.sleep(2)
        logging.info(accepted_user)

        if not accepted_user:
            logger.warning("No login credentials found on the page.")
            return  # or raise an exception if needed

        raw_text = accepted_user[0]
        logging.info(f"{raw_text}")
        new_text = raw_text.split("\n")
        logging.info(f"{new_text}")
        final = new_text[1:]
        logging.info(f"{final}")