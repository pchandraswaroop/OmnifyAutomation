# OrangeHRM QA Automation Assignment 2026

## Overview

This project contains manual testing documentation and automated
test cases for the OrangeHRM demo application.

## Application

OrangeHRM Demo

URL:

https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

## Technology Stack

- Python
- Selenium WebDriver
- PyTest
- Page Object Model
- Google Chrome
- Git/GitHub

## Automated Workflows

The automation covers:

1. Login
2. Dashboard verification
3. Mouse hover over PIM
4. Navigate to PIM
5. Add four employees
6. Navigate to Employee List
7. Search for added employees
8. Verify employee names
9. Print "Name Verified"
10. Logout

## Project Structure

```text
orangehrm-qa-automation/
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── pim_page.py
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   └── test_employee_management.py
│
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/pchandraswaroop/OmnifyAutomation.git

```

Navigate to the project:

```bash
cd OmnifyAutomation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run All Tests

```bash
pytest -v
```

## Run Login Tests

```bash
pytest tests/test_login.py -v
```

## Run Employee Tests

```bash
pytest tests/test_employee_management.py -v
```

## Test Design

The Page Object Model is used to separate:

* Page locators
* Page actions
* Test logic

This improves code maintainability and reusability.

## Author

QA Engineer
