from selenium.webdriver.common.by import By  # type: ignore
from pages.base_page import BasePage
from component.header_component import HeaderComponent


class LoginPage(BasePage):
    _username_locator = (By.ID, "username-email")
    _password_locator = (By.ID, "password")
    _login_button_locator = (By.CLASS_NAME, "primaryAction.signin-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.header = HeaderComponent(driver)  # Initialize HeaderComponent

    def enter_username(self, username):
        username_input = self.driver.find_element(*self._username_locator)
        username_input.send_keys(username)
        return self  # Allow chaining

    def enter_password(self, password):
        password_input = self.driver.find_element(*self._password_locator)
        password_input.send_keys(password)
        return self  # Allow chaining

    def click_login_button(self):
        login_button = self.driver.find_element(*self._login_button_locator)
        login_button.click()
        return self  # Allow chaining or continue the flow if needed

    # To allow for a more fluent interface, you might want to return the page object itself from certain methods. This allows method chaining, making tests more readable.

    def click_profile(self):
        """Method to use HeaderComponent's functionality."""
        self.header.click_profile()
