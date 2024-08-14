# Adjust the path to import from the pages module
import pytest
from selenium import webdriver
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.page_factory import PageFactory


@pytest.fixture(scope="module")
def credentialslogin():
    file_path = os.path.join(os.path.dirname(__file__), "..\config\credentials.json")
    print(f"Looking for credentials file at: {file_path}")
    with open(file_path, "r") as jsonfile:
        data = json.load(jsonfile)
        print(f"Looking for data: {data}")
        return data["credentials"][0]


@pytest.fixture(scope="module")
def driver():
    """Fixture to provide a WebDriver instance"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()  # Ensure the driver is quit after the test


def test_homepage(driver, credentialslogin):
    factory = PageFactory(driver)
    login_page = factory.get_page("Login")

    username = credentialslogin["username"]
    password = credentialslogin["password"]
    print(f"Looking for data: {username}")
    print(f"Looking for data: {password}")

    login_page.open_link(
        "http://barista-uat.perkeso.gov.my:13491/login/ActiveDirectory?returnUrl=%2F"
    )
    login_page.enter_username(username).enter_password(password).click_login_button()

    # Verify login was successful

    return factory.get_page("HomePage")
