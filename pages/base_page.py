from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.page_abstract import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# provides utility methods that are commonly used across different page classes,


class BasePage(Page):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed

    def select_dropdown_option(self, dropdown_id, option_text):
        # Find the dropdown element by ID
        select_element = self.driver.find_element(By.ID, dropdown_id)
        # Create a Select object
        select_obj = Select(select_element)
        # Select the option by visible text
        select_obj.select_by_visible_text(option_text)

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

    def is_loaded(self, text):
        print(f"Text: {text}")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        f"//h2[@class='heading' and contains(text(), '{text}')]",
                    )
                )
            )
            print("Page loaded successfully")
            return True
        except Exception as e:
            print(f"Error checking if Home Page is loaded: {str(e)}")
            return False

    def open_link(self, url):
        print(f"Opening URL: {url}")
        self.driver.get(url)
        print(f"Current URL after opening: {self.driver.current_url}")

    def select_dropdown_option(self, dropdown_id, option_value):
        try:
            # Wait for the dropdown to be visible
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, dropdown_id))
            )

            # Find the dropdown element
            select_element = self.driver.find_element(By.ID, dropdown_id)

            # Create a Select object
            select_obj = Select(select_element)

            # Select the option by value
            select_obj.select_by_value(option_value)
            print(
                f"Selected option with value '{option_value}' from dropdown '{dropdown_id}'"
            )

        except Exception as e:
            print(f"Error selecting option from dropdown: {str(e)}")
