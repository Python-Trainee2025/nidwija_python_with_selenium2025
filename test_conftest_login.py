import time


from selenium.webdriver.common.by import By



def test_demo(driver):

    driver.get("https://www.saucedemo.com/")
    time.sleep(3)
    print("Page Title: ", driver.title)
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()



