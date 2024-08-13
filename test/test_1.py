import pytest
from selenium import webdriver
import json
import os
import sys

# Adjust the path to import from the pages module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.page_factory import PageFactory


@pytest.fixture(scope="module")
def credentialslogin():
    with open("config/credentials.json", "r") as jsonfile:
        data = json.load(jsonfile)
        # Return the first set of credentials as a dictionary
        return data["credentials"][
            0
        ]  # Ensure this key matches the key in your JSON file


@pytest.fixture(scope="module")
def driver():
    """Fixture to provide a WebDriver instance"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()  # Ensure the driver is quit after the test


@pytest.fixture(scope="session")
def home_page(driver, credentialslogin):
    print("home_page fixture is being used")
    """Fixture to handle login and return the HomePage instance."""
    factory = PageFactory(driver)
    login_page = factory.get_page("Login")

    username = credentialslogin["username"]
    password = credentialslogin["password"]

    login_page.open_link(
        "http://barista-uat.perkeso.gov.my:13491/login/ActiveDirectory?returnUrl=%2F"
    )
    login_page.enter_username(username).enter_password(password).click_login_button()

    return factory.get_page("HomePage")


def test_dummy():
    assert True
    print("testconf")
