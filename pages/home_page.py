from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from component.header_component import HeaderComponent
from component.sidebar_component import SidebarComponent


class HomePage(BasePage):
    _heading_locator = (By.ID, "username-email")

    def __init__(self, driver):
        super().__init__(driver)
        print("Initializing HomePage")
        self.header = HeaderComponent(driver)  # Initialize HeaderComponent
        self.sidebar = SidebarComponent(driver)  # Fixed: Initialize SidebarComponent
        print("HomePage initialized")

    def is_loaded(self):
        #   print(f"Text: {text}")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        f"//h2[@class='heading' and contains(text(), 'Home Page')]",
                    )
                )
            )
            print("Home Page loaded successfully")
            return True
        except Exception as e:
            print(f"Error checking if Home Page is loaded: {str(e)}")
            return False

    def open_link(self, url):
        print(f"Opening URL: {url}")
        self.driver.get(url)
        print(f"Current URL after opening: {self.driver.current_url}")

    def click_profile(self):
        """Method to use HeaderComponent's functionality."""
        print("Attempting to click profile")
        self.header.click_profile()
        print("Profile clicked")

    def click_sidebar_tab(self, tab_name):
        print(f"Attempting to click sidebar tab: {tab_name}")
        self.sidebar.click_tab(tab_name)
        print(f"Sidebar tab '{tab_name}' clicked")
