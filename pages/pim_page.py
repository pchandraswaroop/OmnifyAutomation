from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PimPage:

    PIM_MENU = (
        By.XPATH,
        "//span[normalize-space()='PIM']"
    )

    ADD_EMPLOYEE = (
        By.XPATH,
        "//a[normalize-space()='Add Employee']"
    )

    EMPLOYEE_LIST = (
        By.XPATH,
        "//a[normalize-space()='Employee List']"
    )

    FIRST_NAME = (
        By.NAME,
        "firstName"
    )

    MIDDLE_NAME = (
        By.NAME,
        "middleName"
    )

    LAST_NAME = (
        By.NAME,
        "lastName"
    )

    EMPLOYEE_ID = (
        By.XPATH,
        "//label[normalize-space()='Employee Id']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//input"
    )

    SAVE_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Save']"
    )

    EMPLOYEE_NAME_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Employee Name']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//input"
    )

    SEARCH_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Search']"
    )

    RESET_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Reset']"
    )

    TABLE_ROWS = (
        By.CSS_SELECTOR,
        ".oxd-table-body .oxd-table-row"
    )

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        ".oxd-toast"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # ---------------------------
    # PIM Navigation
    # ---------------------------

    def open_pim(self):

        pim = self.wait.until(
            EC.visibility_of_element_located(self.PIM_MENU)
        )

        # Requirement specifically asks for mouse hover
        ActionChains(self.driver).move_to_element(pim).perform()

        self.wait.until(
            EC.element_to_be_clickable(self.PIM_MENU)
        ).click()

        self.wait.until(
            EC.url_contains("/pim/")
        )

    # ---------------------------
    # Add Employee
    # ---------------------------

    def click_add_employee(self):

        self.wait.until(
            EC.element_to_be_clickable(self.ADD_EMPLOYEE)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )

    def add_employee(
        self,
        first_name,
        middle_name,
        last_name
    ):

        first_name_element = self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_NAME
            )
        )

        first_name_element.clear()
        first_name_element.send_keys(first_name)

        middle_name_element = self.wait.until(
            EC.visibility_of_element_located(
                self.MIDDLE_NAME
            )
        )

        middle_name_element.clear()
        middle_name_element.send_keys(middle_name)

        last_name_element = self.wait.until(
            EC.visibility_of_element_located(
                self.LAST_NAME
            )
        )

        last_name_element.clear()
        last_name_element.send_keys(last_name)

        # Employee ID is generated/pre-filled by the application.
        # We intentionally don't overwrite it.

        self.wait.until(
            EC.element_to_be_clickable(
                self.SAVE_BUTTON
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.SUCCESS_MESSAGE
            )
        )

    # ---------------------------
    # Employee List
    # ---------------------------

    def open_employee_list(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.EMPLOYEE_LIST
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.EMPLOYEE_NAME_INPUT
            )
        )

    def reset_search(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.RESET_BUTTON
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.EMPLOYEE_NAME_INPUT
            )
        )

    # ---------------------------
    # Search Employee
    # ---------------------------

    def search_employee(self, employee_name):

        search_box = self.wait.until(
            EC.visibility_of_element_located(
                self.EMPLOYEE_NAME_INPUT
            )
        )

        search_box.clear()
        search_box.send_keys(employee_name)

        # OrangeHRM Employee Name field uses autocomplete.
        suggestion = (
            By.XPATH,
            "//div[contains(@class,'oxd-autocomplete-option')]"
            f"//*[contains(normalize-space(),'{employee_name}')]"
        )

        try:
            self.wait.until(
                EC.element_to_be_clickable(
                    suggestion
                )
            ).click()
        except:
            # If the exact suggestion isn't available,
            # continue with the typed value.
            pass

        self.wait.until(
            EC.element_to_be_clickable(
                self.SEARCH_BUTTON
            )
        ).click()

    # ---------------------------
    # Verify Employee
    # ---------------------------

def verify_employee(self, employee_name):
    """
    Verify that an employee exists in the employee table.
    Re-fetches rows each time to avoid stale element references.
    """

    wait = WebDriverWait(self.driver, 15)

    try:
        # Wait until the employee table is loaded
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".oxd-table-body")
            )
        )

        # Get the table text directly instead of keeping stale row elements
        table = self.driver.find_element(
            By.CSS_SELECTOR,
            ".oxd-table-body"
        )

        table_text = table.text.lower()

        if employee_name.lower() in table_text:
            print(f"{employee_name} - Name Verified")
            return True

        return False

    except Exception as e:
        print(f"Error while verifying {employee_name}: {e}")
        return False
