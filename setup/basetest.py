from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest:
    def setup_method(self):
        chrome_options = Options()


        driver = webdriver.Chrome(options=chrome_options)
        self.driver = driver
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def open_url(self, url):
        self.driver.get(url)