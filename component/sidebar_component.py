## composition where a LoginPage might contain instances of smaller,
# reusable components (like a Header or Footer).
from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore
from selenium.webdriver.support import expected_conditions as EC  # type: ignore


class SidebarComponent:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_tab(self, tab_name):
        """Clicks a tab in the sidebar by its visible text."""
        tab_locator = (
            By.XPATH,
            f"//a[contains(@class, 'ap-MenuItem-link') and text()='{tab_name}']",
        )
        tab = self.wait.until(EC.element_to_be_clickable(tab_locator))
        tab.click()
