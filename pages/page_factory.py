from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.preregistration_page import PregistrationPage
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
            try:
                print("Creating HomePage")
                home_page = HomePage(self.driver)
                print(f"Created HomePage: {home_page}")
                if home_page.is_loaded():
                    print("HomePage is loaded successfully")
                else:
                    print("HomePage failed to load")
                return home_page
            except Exception as e:
                print(f"Error creating HomePage: {str(e)}")
                import traceback

                traceback.print_exc()
                return None
        # ... rest of the method ...
