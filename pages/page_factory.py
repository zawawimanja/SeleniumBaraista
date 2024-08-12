from pages.login_page import LoginPage



class PageFactory:
    def __init__(self, driver):
        self.driver = driver

    def get_page(self, page_name):
        if page_name == "Login":
            return LoginPage(self.driver)
        elif page_name == "Dashboard":
            return DashboardPage(self.driver)
        # Add more pages as needed