from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage


USERNAME = "Admin"
PASSWORD = "admin123"


def test_add_and_verify_employees(driver):

    # ---------------------------
    # Login
    # ---------------------------

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        USERNAME,
        PASSWORD
    )

    dashboard_page = DashboardPage(driver)

    assert dashboard_page.is_dashboard_visible(), \
        "Dashboard was not displayed"

    # ---------------------------
    # Navigate to PIM
    # ---------------------------

    pim_page = PimPage(driver)

    pim_page.open_pim()

    # ---------------------------
    # Employees to create
    # ---------------------------

    employees = [
        ("TestAarav", "QA", "Sharma"),
        ("TestPriya", "QA", "Nair"),
        ("TestRahul", "QA", "Verma"),
        ("TestAnanya", "QA", "Singh")
    ]

    # ---------------------------
    # Add Employees
    # ---------------------------

    for first_name, middle_name, last_name in employees:

        pim_page.click_add_employee()

        pim_page.add_employee(
            first_name,
            middle_name,
            last_name
        )

        # Return to PIM
        pim_page.open_pim()

    # ---------------------------
    # Employee List
    # ---------------------------

    pim_page.open_employee_list()

    # ---------------------------
    # Verify Employees
    # ---------------------------

    for first_name, middle_name, last_name in employees:

        full_name = (
            f"{first_name} "
            f"{middle_name} "
            f"{last_name}"
        )

        pim_page.reset_search()

        pim_page.search_employee(
            first_name
        )

        found = pim_page.verify_employee(
            first_name
        )

        assert found, \
            f"{full_name} was not found"

    # ---------------------------
    # Logout
    # ---------------------------

    dashboard_page.logout()
