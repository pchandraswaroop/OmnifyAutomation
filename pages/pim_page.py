import time
from selenium.webdriver.common.keys import Keys
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



    def open_pim(self):

        pim = self.wait.until(
            EC.visibility_of_element_located(self.PIM_MENU)
        )

        ActionChains(self.driver).move_to_element(pim).perform()

        self.wait.until(
            EC.element_to_be_clickable(self.PIM_MENU)
        ).click()

        self.wait.until(
            EC.url_contains("/pim/")
        )



    def click_add_employee(self):

        self.wait.until(
            EC.element_to_be_clickable(self.ADD_EMPLOYEE)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )
    def add_employee(self, first_name, middle_name, last_name, employee_id=None):
        """
        Add a new employee with a unique Employee ID.
        """

        # First Name
        first_name_field = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_NAME)
        )
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        # Middle Name
        middle_name_field = self.wait.until(
            EC.element_to_be_clickable(self.MIDDLE_NAME)
        )
        middle_name_field.clear()
        middle_name_field.send_keys(middle_name)

        last_name_field = self.wait.until(
            EC.element_to_be_clickable(self.LAST_NAME)
        )
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        
        if employee_id:
            employee_id_field = self.wait.until(
                EC.element_to_be_clickable(self.EMPLOYEE_ID)
            )

            employee_id_field.click()
            employee_id_field.send_keys(Keys.CONTROL, "a")

            employee_id_field.send_keys(Keys.BACKSPACE)

            employee_id_field.send_keys(employee_id)

        save_button = self.wait.until(
            EC.element_to_be_clickable(self.SAVE_BUTTON)
        )
        save_button.click()


        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/pim/viewPersonalDetails/")
            )
        except:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
            )

        time.sleep(1)


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
          
            pass

        self.wait.until(
            EC.element_to_be_clickable(
                self.SEARCH_BUTTON
            )
        ).click()



    def verify_employee(self, employee_name):
        """
        Verify an employee exists in the current employee table.
        Handles OrangeHRM table refreshes and stale elements.
        """

        wait = WebDriverWait(self.driver, 15)

        try:
            wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".oxd-table-body")
                )
            )

            time.sleep(1)


            table_text = self.driver.execute_script("""
                const table = document.querySelector('.oxd-table-body');
                return table ? table.innerText : '';
            """)

            if employee_name.lower() in table_text.lower():
                print(f"{employee_name} - Name Verified")
                return True

            print(f"{employee_name} - Name NOT Verified")
            return False

        except Exception as e:
            print(f"Error while verifying {employee_name}: {e}")
            return False