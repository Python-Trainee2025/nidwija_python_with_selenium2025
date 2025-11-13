"""
send_keys()	-> element.send_keys("text")
click()-> element.click()
clear()	_>	element.clear()
text ->	print(element.text)
get_attribute()	_> element.get_attribute("href")
"""


import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_demo_element():
    chrome_options=Options()

    driver=webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    accepted_unames=[]
    username_list=driver.find_elements(By.XPATH,'//div[@id="login_credentials"]')
    for i in username_list:
        print(i.text)
        accepted_unames.append(i.text)

    print(accepted_unames)
    og_text=accepted_unames[0]
    print(og_text)
    new_text=og_text.split("\n")
    print(new_text)
    final_list=new_text[1:]
    print(final_list)


    driver.quit()