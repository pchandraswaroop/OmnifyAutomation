import time

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage


USERNAME = "Admin"
PASSWORD = "admin123"


def test_add_and_verify_employees(driver):



    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        USERNAME,
        PASSWORD
    )

    dashboard_page = DashboardPage(driver)

    assert dashboard_page.is_dashboard_visible(), \
        "Dashboard was not displayed"


    pim_page = PimPage(driver)

    pim_page.open_pim()



    run_id = str(int(time.time()))[-4:]

    employees = [
        (f"Aarav{run_id}", "QA", "Sharma", f"{run_id}01"),
        (f"Priya{run_id}", "QA", "Nair", f"{run_id}02"),
        (f"Rahul{run_id}", "QA", "Verma", f"{run_id}03"),
        (f"Ananya{run_id}", "QA", "Singh", f"{run_id}04")
    ]

   

    for first_name, middle_name, last_name, employee_id in employees:

        pim_page.click_add_employee()

        pim_page.add_employee(
            first_name,
            middle_name,
            last_name,
            employee_id
        )

        pim_page.open_pim()



    pim_page.open_employee_list()

    
    for first_name, middle_name, last_name, employee_id in employees:

        full_name = (
            f"{first_name} "
            f"{middle_name} "
            f"{last_name}"
        )

        pim_page.reset_search()

        pim_page.search_employee(first_name)

        found = pim_page.verify_employee(first_name)

        assert found, \
            f"{full_name} was not found"

    

    dashboard_page.logout()