from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    DASHBOARD_HEADER = (
        By.XPATH,
        "//h6[normalize-space()='Dashboard']"
    )

    PROFILE_MENU = (
        By.CSS_SELECTOR,
        "span.oxd-userdropdown-tab"
    )

    LOGOUT_LINK = (
        By.XPATH,
        "//a[normalize-space()='Logout']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def is_dashboard_visible(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(
                    self.DASHBOARD_HEADER
                )
            ).is_displayed()
        except:
            return False

    def logout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.PROFILE_MENU)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT_LINK)
        ).click()

        self.wait.until(
            EC.url_contains("/auth/login")
        )
