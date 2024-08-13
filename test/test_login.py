# Adjust the path to import from the pages module
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.page_factory import PageFactory


def test_login(driver, credentialslogin):
    factory = PageFactory(driver)
    login_page = factory.get_page("Login")

    username = credentialslogin["username"]
    password = credentialslogin["password"]

    login_page.open_link(
        "http://barista-uat.perkeso.gov.my:13491/login/ActiveDirectory?returnUrl=%2F"
    )
    login_page.enter_username(username).enter_password(password).click_login_button()

    # Verify login was successful
    home_page = factory.get_page("HomePage")
    assert home_page.is_loaded()  # Assuming HomePage has an is_loaded() method
