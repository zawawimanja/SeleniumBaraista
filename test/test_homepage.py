# test_homepage.py


def test_click_sidebar_tab(home_page):
    """Test case to click a specific sidebar tab after login."""
    # Navigate to the homepage (if needed)

    home_page.open_link(
        "http://barista-uat.perkeso.gov.my:13491/login/ActiveDirectory?returnUrl=%2F"
    )  # Adjust URL as needed

    # Click on a specific sidebar tab
    home_page.is_loaded()
    tab_to_click = "Pre-Registration"  # Example tab text
    home_page.click_sidebar_tab(tab_to_click)
