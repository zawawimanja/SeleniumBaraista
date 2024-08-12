from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver

    def open_link(self, url):
        self.driver.get(url)

    def verify_title(self,expected_title):  # Add expected title as parameter
       actual_title = self.driver.title
       assert expected_title in actual_title, f"Expected title '{expected_title}', but found '{actual_title}'"
       print('Result',self.driver.title)
       
    def search_on_google(self, search_term):
        search_box = self.driver.find_element(By.NAME, 'q')  # Replace with the correct locator
        search_box.clear()
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)
        print('Search executed.')

        # Wait for the search results to load and verify the presence of an element on the results page
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='test']"))
            )
            print('Search results verification success. Test pass.')
        except Exception as e:
            print(f'An error occurred: {e}. Test failed.')
