import pytest
from selenium import webdriver

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.page_factory import PageFactory

import csv

@pytest.fixture(scope="module")
def credentials():
    with open('credentials.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        return [(row[0], row[1]) for row in reader]

@pytest.fixture
def driver():
    """Fixture to provide a WebDriver instance"""
    driver = webdriver.Chrome()
    yield driver
   
def test_login(driver):
    factory = PageFactory(driver)
    login_page = factory.get_page("Login")
    login_page.open_link('http://barista-uat.perkeso.gov.my:13491/login/ActiveDirectory?returnUrl=%2F') # login_page.enter_username("user")
    # login_page.enter_password("password")
    # login_page.click_login()