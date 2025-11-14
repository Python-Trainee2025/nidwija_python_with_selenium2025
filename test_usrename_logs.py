

import logging

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
class TestLogs:
    def test_demo_list_items(self):
        chrome_options=Options()

        driver=webdriver.Chrome(options=chrome_options)

        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        user_list=driver.find_elements(By.XPATH,'//div[@id="login_credentials"]')
        time.sleep(2)
        accepted_user=[]
        for i in user_list:
            logging.info(f"{i.text}")
            accepted_user.append(i.text)
        logging.info(accepted_user)
        raw_text=accepted_user[0]
        logging.info(f"{raw_text}")
        new_text=raw_text.split("\n")
        logging.info(f"{new_text}")
        final=new_text[1:]
        logging.info(f"{final}")
