from Page_objects.loginpom.loginlocators import LoginLocators



class LoginPageProperties(LoginLocators):

    @property
    def username_input(self):
        return self.driver.find_element(*LoginLocators.USERNAME_INPUT)


