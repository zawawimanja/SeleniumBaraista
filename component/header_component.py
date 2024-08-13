from selenium.webdriver.common.by import By
## composition where a LoginPage might contain instances of smaller,
# reusable components (like a Header or Footer).
class HeaderComponent:
    def __init__(self, driver):
        self.driver = driver

    def click_profile(self):
        profile_button = self.driver.find_element(By.ID, "profile")
        profile_button.click()
