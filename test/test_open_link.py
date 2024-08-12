import pytest
from selenium import webdriver
from pages.page import Page  # Assuming Page class is in page_objects directory


@pytest.fixture
def driver():
    """Fixture to provide a WebDriver instance"""
    driver = webdriver.Chrome()
    yield driver
   


def test_open_google_and_verify_title(driver):
    """Test case using POM and pytest"""
    page = Page(driver)
    page.open_link("http://barista-uat.perkeso.gov.my:13491/login/ActiveDirectory?returnUrl=%2F")
    page.verify_title("Google")
    page.search_on_google('test')
