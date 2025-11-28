from page_objects.loginpom.loginprops import LoginPageProperties


class LoginPage(LoginPageProperties):
    def __init__(self, driver):
        self.driver = driver

    def login(self, username):
        self.username_input.send_keys(username)
        self.username_input.click()


