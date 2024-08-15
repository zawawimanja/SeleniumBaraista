from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from component.header_component import HeaderComponent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class PreregistrationPage(BasePage):
    _notice_type_pre_reg_locator = (By.ID, "NoticeTypePreReg")
    _accident_date_search_no_locator = (By.ID, "AccidentDateSearch")
    _accident_time_search_no_locator = (By.ID, "AccidentTimeSearch")
    _identification_type_preReg_no_locator = (By.ID, "IdentificationTypePreReg")
    _identification_no_locator = (By.ID, "IdentificationNo")
    _employer_code_pre_reg_locator = (By.ID, "EmployerCodePreReg")

    def __init__(self, driver):
        super().__init__(driver)
        self.header = HeaderComponent(driver)  # Initialize HeaderComponent

        self.dropdown_ids = {
            "dropdown1": self._notice_type_pre_reg_locator,
            "dropdown2": "id_of_dropdown2",
            "dropdown3": "id_of_dropdown3",
            "dropdown4": "id_of_dropdown4",
        }

        self.dropdown1_options = {
            "option1": "Accident",
            "option2": "OD",  # Ensure this is included
            "option3": "Value 3 for Dropdown 1",
            "option4": "Value 4 for Dropdown 1",
        }

    def open_link(self, url):
        self.driver.get(url)

    def select_option_from_dropdown1(self, option_value):
        # Ensure the option_value is valid
        valid_values = ["Accident", "Death - PKT", "Death - FOT", "OD", "ILAT"]

        if option_value not in valid_values:
            raise ValueError(f"Option value '{option_value}' is not valid")

        self.select_dropdown_option("NoticeTypePreReg", option_value)

    def click_profile(self):
        """Method to use HeaderComponent's functionality."""
        self.header.click_profile()
