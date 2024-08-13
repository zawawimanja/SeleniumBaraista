from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.page import Page  # Import the abstract Page class

class BasePage(Page):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed

    def wait_for_element(self, locator):
        """Waits for an element to be present on the page."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def accept_alert(self):
        """Accepts an alert if it is present."""
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()

    def scroll_to_element(self, locator):
        """Scrolls to the element specified by the locator."""
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

   
