from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HeaderComponent:
    def __init__(self, driver):
        self.driver = driver
    
    def click_profile(self):
        profile_button = self.driver.find_element(By.ID, "profile")
        profile_button.click()

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.header = HeaderComponent(driver)

