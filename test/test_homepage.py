# test_homepage.py


def test_click_sidebar_tab(home_page):
    """Test case to click a specific sidebar tab after login."""
    # Navigate to the homepage (if needed)
    home_page.open_link(
        "http://barista-uat.perkeso.gov.my:13491/home"
    )  # Adjust URL as needed

    # Click on a specific sidebar tab
    tab_to_click = "Pre-Registration"  # Example tab text
    home_page.click_sidebar_tab(tab_to_click)
    # Add assertions to verify the result of the tab click
    # For example:
    # assert "Expected Page Title" in driver.title
