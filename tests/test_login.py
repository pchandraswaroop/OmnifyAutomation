from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


USERNAME = "Admin"
PASSWORD = "admin123"


def test_valid_login(driver):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        USERNAME,
        PASSWORD
    )

    dashboard_page = DashboardPage(driver)

    assert dashboard_page.is_dashboard_visible(), \
        "Dashboard was not displayed after login"


def test_login_and_logout(driver):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        USERNAME,
        PASSWORD
    )

    dashboard_page = DashboardPage(driver)

    assert dashboard_page.is_dashboard_visible(), \
        "Dashboard was not displayed"

    dashboard_page.logout()

    assert "/auth/login" in driver.current_url, \
        "User was not redirected to login page after logout"
