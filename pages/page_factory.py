from pages.login_page import LoginPage
from pages.preregistration_page import PregistrationPage
from pages.mycases_page import MyCasesPage
from pages.base_page import BasePage

# You might implement a factory pattern to manage the creation of
# different page objects, which can be useful if your application has a lot of different pages.


class PageFactory:
    def __init__(self, driver):
        self.driver = driver

    def get_page(self, page_name):
        if page_name == "Login":
            return LoginPage(self.driver)
        elif page_name == "Pre-Registration":
            return PregistrationPage(self.driver)
        elif page_name == "MyCases":
            return MyCasesPage(self.driver)
