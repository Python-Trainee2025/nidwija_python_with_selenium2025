import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options=Options()

driver=webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(3)
print(driver.title)
driver.quit()


