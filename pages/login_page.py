from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        element = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        )
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        element = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        element.clear()
        element.send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
