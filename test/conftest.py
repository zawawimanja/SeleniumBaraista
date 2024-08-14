import pytest
from selenium import webdriver
import json
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.page_factory import PageFactory


@pytest.fixture(scope="module")
def credentialslogin():
    file_path = os.path.join(
        os.path.dirname(__file__), "..", "config", "credentials.json"
    )
    print(f"Looking for credentials file at: {file_path}")
    with open(file_path, "r") as jsonfile:
        data = json.load(jsonfile)
        print(f"Looking for data: {data}")
        return data["credentials"][0]


@pytest.fixture(scope="module")
def driver():
    """Fixture to provide a WebDriver instance with SSL errors ignored"""
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument("--ignore-certificate-errors-spki-list")
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)

    yield driver

    driver.quit()


@pytest.fixture(scope="module")
def home_page(driver, credentialslogin):
    print("home_page fixture started")
    factory = PageFactory(driver)
    login_page = factory.get_page("Login")

    username = credentialslogin["username"]
    password = credentialslogin["password"]

    login_page.open_link("http://barista-uat.perkeso.gov.my:13491/home")
    login_page.enter_username(username).enter_password(password).click_login_button()

    print(f"Current URL after login: {driver.current_url}")
    print("Attempting to get HomePage")
    home_page = factory.get_page("Home")
    print(f"Home page object: {home_page}")

    if home_page is None:
        print("HomePage creation failed")
    else:
        print("HomePage created successfully")

    return home_page
