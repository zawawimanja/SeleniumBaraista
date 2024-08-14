from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.page_abstract import Page

# provides utility methods that are commonly used across different page classes,


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
