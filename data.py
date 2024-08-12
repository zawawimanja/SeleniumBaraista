import pytest


@pytest.mark.parametrize("username, password", [
    ("valid_user", "valid_pass"),
    ("invalid_user", "invalid_pass"),
])
def test_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    assert "Dashboard" in login_page.get_title()
