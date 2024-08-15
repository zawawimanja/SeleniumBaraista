from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.preregistration_page import PreregistrationPage
from pages.mycases_page import MyCasesPage
from pages.base_page import BasePage

# You might implement a factory pattern to manage the creation of
# different page objects, which can be useful if your application has a lot of different pages.


class PageFactory:
    def __init__(self, driver):
        self.driver = driver
        print("PageFactory initialized")

    def get_page(self, page_name):
        print(f"Attempting to get page: {page_name}")
        if page_name == "Login":
            login_page = LoginPage(self.driver)
            print(f"Created LoginPage: {login_page}")
            return login_page
        elif page_name == "Home":
            home_page = HomePage(self.driver)
            print(f"Created HomePage: {home_page}")
            return home_page
        elif page_name == "Preregistration":  # Fixed typo
            preregistration_page = PreregistrationPage(self.driver)
            print(f"Created PreregistrationPage: {preregistration_page}")
            return preregistration_page
