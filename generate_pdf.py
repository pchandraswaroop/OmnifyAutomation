import sys
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def build_pdf(filename="OrangeHRM_QA_Report_2026.pdf"):
    target_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    doc = SimpleDocTemplate(
        target_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Custom styles
    primary_color = colors.HexColor("#1A365D")   # Deep Navy
    secondary_color = colors.HexColor("#2B6CB0") # Slate Blue
    accent_pass = colors.HexColor("#2F855A")     # Forest Green
    accent_fail = colors.HexColor("#C53030")     # Deep Red
    bg_light = colors.HexColor("#F7FAFC")        # Off-white / light gray

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=primary_color,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=14,
        textColor=secondary_color,
        spaceAfter=10
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=primary_color,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#2D3748"),
        spaceAfter=5
    )

    cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#2D3748")
    )

    cell_header = ParagraphStyle(
        'TableHeaderCell',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white
    )

    cell_pass = ParagraphStyle(
        'TableCellPass',
        parent=cell_style,
        fontName='Helvetica-Bold',
        textColor=accent_pass
    )

    cell_fail = ParagraphStyle(
        'TableCellFail',
        parent=cell_style,
        fontName='Helvetica-Bold',
        textColor=accent_fail
    )

    elements = []

    # Title & Header
    elements.append(Paragraph("QA ENGINEER ASSIGNMENT 2026", title_style))
    elements.append(Paragraph("OrangeHRM — Manual Testing & QA Report", subtitle_style))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=primary_color, spaceAfter=10))

    # Meta Table
    meta_data = [
        [Paragraph("<b>Candidate Name:</b> [Your Name]", cell_style), Paragraph("<b>Application:</b> OrangeHRM OS 5.9", cell_style)],
        [Paragraph("<b>Application URL:</b> https://opensource-demo.orangehrmlive.com/", cell_style), Paragraph("<b>Testing Type:</b> Manual & Automated QA", cell_style)],
        [Paragraph("<b>Browser / OS:</b> Google Chrome / Windows", cell_style), Paragraph("<b>Test Account:</b> Admin / admin123", cell_style)],
    ]
    meta_table = Table(meta_data, colWidths=[270, 270])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg_light),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    elements.append(meta_table)
    elements.append(Spacer(1, 8))

    # 1. Objective
    elements.append(Paragraph("1. Objective", h1_style))
    elements.append(Paragraph(
        "The objective of this assignment is to manually test the OrangeHRM web application, with focus on: "
        "Login functionality, Employee management (adding, viewing, updating, and deleting employees), searching and verifying employee records, "
        "identifying potential bugs and usability/accessibility issues, documenting comprehensive test cases, and preparing workflows for POM-based Selenium automation.",
        body_style
    ))

    # 2. Application Under Test
    elements.append(Paragraph("2. Application Under Test", h1_style))
    elements.append(Paragraph(
        "<b>URL:</b> https://opensource-demo.orangehrmlive.com/web/index.php/auth/login<br/>"
        "<b>Credentials:</b> Username: Admin | Password: admin123<br/>"
        "<b>Browser:</b> Google Chrome (Desktop / Windows environment)",
        body_style
    ))

    # 3. Login Test Cases
    elements.append(Paragraph("3. Login Test Cases", h1_style))
    elements.append(Paragraph("A total of 10 primary login test cases were designed and executed manually.", body_style))

    login_tc_data = [
        [
            Paragraph("TC ID", cell_header),
            Paragraph("Scenario", cell_header),
            Paragraph("Test Steps", cell_header),
            Paragraph("Expected Result", cell_header),
            Paragraph("Actual Result", cell_header),
            Paragraph("Status", cell_header)
        ],
        [
            Paragraph("LOGIN-001", cell_style),
            Paragraph("Login with valid credentials", cell_style),
            Paragraph("1. Open login page.<br/>2. Enter Admin.<br/>3. Enter admin123.<br/>4. Click Login.", cell_style),
            Paragraph("User successfully authenticated and redirected to Dashboard.", cell_style),
            Paragraph("Logged in successfully; Dashboard displayed.", cell_style),
            Paragraph("Pass", cell_pass)
        ],
        [
            Paragraph("LOGIN-002", cell_style),
            Paragraph("Invalid username", cell_style),
            Paragraph("1. Open login page.<br/>2. Enter invalid username.<br/>3. Enter valid password.<br/>4. Click Login.", cell_style),
            Paragraph("Login fails with appropriate error message.", cell_style),
            Paragraph("'Invalid credentials' displayed.", cell_style),
            Paragraph("Pass", cell_pass)
        ],
        [
            Paragraph("LOGIN-003", cell_style),
            Paragraph("Invalid password", cell_style),
            Paragraph("1. Open login page.<br/>2. Enter username Admin.<br/>3. Enter invalid password.<br/>4. Click Login.", cell_style),
            Paragraph("Login fails with appropriate error message.", cell_style),
            Paragraph("'Invalid credentials' displayed.", cell_style),
            Paragraph("Pass", cell_pass)
        ],
        [
            Paragraph("LOGIN-004", cell_style),
            Paragraph("Both fields empty", cell_style),
            Paragraph("1. Open login page.<br/>2. Leave fields empty.<br/>3. Click Login.", cell_style),
            Paragraph("Required field validation displayed for both fields.", cell_style),
            Paragraph("'Required' validation displayed under both inputs.", cell_style),
            Paragraph("Pass", cell_pass)
        ],
        [
            Paragraph("LOGIN-005", cell_style),
            Paragraph("Username empty", cell_style),
            Paragraph("1. Leave Username empty.<br/>2. Enter valid password.<br/>3. Click Login.", cell_style),
            Paragraph("Username displays required validation message.", cell_style),
            Paragraph("'Required' displayed under Username field.", cell_style),
            Paragraph("Pass", cell_pass)
        ],
        [
            Paragraph("LOGIN-006", cell_style),
            Paragraph("Password empty", cell_style),
            Paragraph("1. Enter valid username.<br/>2. Leave Password empty.<br/>3. Click Login.", cell_style),
            Paragraph("Password displays required validation message.", cell_style),
            Paragraph("'Required' displayed under Password field.", cell_style),
            Paragraph("Pass", cell_pass)
        ],
        [
            Paragraph("LOGIN-007", cell_style),
            Paragraph("Password masking", cell_style),
            Paragraph("1. Open login page.<br/>2. Enter password.<br/>3. Observe field.", cell_style),
            Paragraph("Password masked as bullet/dot characters.", cell_style),
            Paragraph("Password displayed as masked characters.", cell_style),
            Paragraph("Pass", cell_pass)
        ],
        [
            Paragraph("LOGIN-008", cell_style),
            Paragraph("Forgot Password page", cell_style),
            Paragraph("1. Open login page.<br/>2. Click 'Forgot your password?'.", cell_style),
            Paragraph("User redirected to password recovery page.", cell_style),
            Paragraph("Password recovery page opened successfully.", cell_style),
            Paragraph("Pass", cell_pass)
        ],
        [
            Paragraph("LOGIN-009", cell_style),
            Paragraph("Invalid username & password", cell_style),
            Paragraph("1. Enter invalid username.<br/>2. Enter invalid password.<br/>3. Click Login.", cell_style),
            Paragraph("Login fails with appropriate error message.", cell_style),
            Paragraph("'Invalid credentials' displayed.", cell_style),
            Paragraph("Pass", cell_pass)
        ],
        [
            Paragraph("LOGIN-010", cell_style),
            Paragraph("Login after failed attempt", cell_style),
            Paragraph("1. Enter invalid credentials.<br/>2. Click Login.<br/>3. Enter valid credentials.<br/>4. Click Login.", cell_style),
            Paragraph("User successfully logs in after correcting credentials.", cell_style),
            Paragraph("Dashboard displayed after valid credentials entered.", cell_style),
            Paragraph("Pass", cell_pass)
        ],
    ]

    login_table = Table(login_tc_data, colWidths=[50, 85, 115, 115, 125, 50])
    login_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, bg_light])
    ]))
    elements.append(login_table)
    elements.append(Spacer(1, 10))

    # 4. Employee Management Test Cases
    elements.append(Paragraph("4. Employee Management Test Cases", h1_style))
    elements.append(Paragraph(
        "<b>Workflow:</b> PIM → Add Employee → Employee List → Search → View → Update → Delete", body_style
    ))

    # Employee Summary Table
    emp_sum_data = [
        [Paragraph("Employee Name", cell_header), Paragraph("Employee ID", cell_header), Paragraph("Current Status", cell_header)],
        [Paragraph("Chandra Swaroops Palika", cell_style), Paragraph("0694", cell_style), Paragraph("Active (Middle name updated from Swaroop to Swaroops)", cell_style)],
        [Paragraph("Priya M Nair", cell_style), Paragraph("0695", cell_style), Paragraph("Deleted (Successfully removed)", cell_style)],
        [Paragraph("Rahul K Verma", cell_style), Paragraph("0696", cell_style), Paragraph("Active", cell_style)],
        [Paragraph("Ananya P Singh", cell_style), Paragraph("0697", cell_style), Paragraph("Active", cell_style)],
    ]
    emp_sum_table = Table(emp_sum_data, colWidths=[180, 100, 260])
    emp_sum_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), secondary_color),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, bg_light])
    ]))
    elements.append(emp_sum_table)
    elements.append(Spacer(1, 8))

    # EMP Test Cases Details
    emp_tc_list = [
        ("EMP-001", "Duplicate Employee ID Validation",
         "1. Navigate to PIM → Add Employee.<br/>2. Enter valid employee info.<br/>3. Enter an existing Employee ID.<br/>4. Click Save.",
         "System prevents creation and displays duplicate Employee ID error.",
         "Validation message displayed indicating Employee ID already exists.", "Pass"),

        ("EMP-002", "Add Employee with Valid Details",
         "1. Navigate to PIM → Add Employee.<br/>2. Enter name details.<br/>3. Enter unique Employee ID.<br/>4. Click Save.",
         "Employee created successfully and profile displayed.",
         "Employee Chandra Swaroop Palika created successfully (ID 0694).", "Pass"),

        ("EMP-003", "Verify Employee in Employee List",
         "1. Navigate to PIM → Employee List.<br/>2. Enter name in search.<br/>3. Select autocomplete suggestion.<br/>4. Click Search.",
         "Newly created employee appears in search results with correct details.",
         "Employee record for Chandra Swaroop Palika (ID 0694) found.", "Pass"),

        ("EMP-004", "View Employee Details",
         "1. Search for Chandra Swaroop Palika.<br/>2. Click on record to open profile.<br/>3. Review Personal Details.",
         "Employee profile opens and displays saved information accurately.",
         "Profile opened successfully; personal details match.", "Pass"),

        ("EMP-005", "Update Employee Information",
         "1. Open employee profile.<br/>2. Update middle name from Swaroop to Swaroops.<br/>3. Click Save.",
         "Updated information saved successfully and reflected on profile.",
         "Success toast displayed; name updated to Chandra Swaroops Palika.", "Pass"),

        ("EMP-006", "Cancel Employee Deletion",
         "1. Navigate to Employee List.<br/>2. Search employee.<br/>3. Click Delete icon.<br/>4. Click 'No, Cancel' in modal.",
         "Confirmation dialog closes; employee record remains unchanged.",
         "Deletion cancelled; employee remains present in list.", "Pass"),

        ("EMP-007", "Delete Employee",
         "1. Search for Priya M Nair.<br/>2. Click Delete icon.<br/>3. Click 'Yes, Delete'.<br/>4. Reset search & search again.",
         "Employee permanently deleted; subsequent search yields no records.",
         "Priya M Nair deleted. Search returned 'No Records Found'.", "Pass")
    ]

    for id_code, title, steps, expected, actual, status in emp_tc_list:
        tc_box_data = [
            [Paragraph(f"<b>{id_code} — {title}</b>", cell_header), Paragraph(f"<b>Status: {status}</b>", cell_header)],
            [Paragraph(f"<b>Test Steps:</b> {steps}", cell_style), Paragraph(f"<b>Expected:</b> {expected}<br/><br/><b>Actual:</b> {actual}", cell_style)]
        ]
        tc_box_table = Table(tc_box_data, colWidths=[270, 270])
        tc_box_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), primary_color),
            ('BACKGROUND', (0, 1), (-1, 1), bg_light),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('LEFTPADDING', (0, 0), (-1, -1), 5),
            ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ]))
        elements.append(KeepTogether([tc_box_table, Spacer(1, 6)]))

    elements.append(Spacer(1, 4))

    # 5. Accessibility / Keyboard Testing
    elements.append(Paragraph("5. Accessibility / Keyboard Testing", h1_style))
    elements.append(Paragraph(
        "A keyboard-only accessibility test was performed on the OrangeHRM login page using the <b>Tab</b> key.<br/>"
        "<b>Expected Order:</b> Username → Password → Login → Forgot your password?<br/>"
        "<b>Observations:</b> Username and Password were reached relatively late in the tab sequence. The Forgot Password link was not reached during standard keyboard navigation. Pressing Enter submitted the form correctly.",
        body_style
    ))

    # 6. Bugs / Usability Issues
    elements.append(Paragraph("6. Bugs / Usability Issues", h1_style))

    bugs = [
        ("BUG-001", "Generic Invalid Credentials Message", "Login Module", "Medium", "Usability / Security Feedback",
         "When an incorrect username or password is entered, the system displays a generic 'Invalid credentials' message without clarifying which field was incorrect.",
         "The app displays 'Invalid credentials' for both invalid username and invalid password.",
         "Provides low clarity for legitimate users who made a single typo."),

        ("BUG-002", "Poor Keyboard Navigation / Tab Order", "Login Module", "Medium", "Accessibility / UI",
         "Login form focus sequence does not follow natural top-to-bottom keyboard navigation flow.",
         "Username & Password inputs are reached late in the tab order; 'Forgot your password?' is skipped.",
         "Impairs usability for keyboard-only and assistive technology users."),

        ("BUG-003", "Forgot Password Returns 504 Gateway Time-out", "Login / Recovery", "High", "Functional / Server Availability",
         "Submitting a password recovery request for a valid user returns a 504 Gateway Time-out page.",
         "Application displays: '504 Gateway Time-out nginx/1.18.0 (Ubuntu)'.",
         "Critical failure preventing users from recovering their accounts.")
    ]

    for bug_id, bug_title, module, severity, bug_type, desc, actual_res, impact in bugs:
        bug_data = [
            [Paragraph(f"<b>{bug_id} — {bug_title}</b>", cell_header), Paragraph(f"<b>Severity: {severity}</b> | Type: {bug_type}", cell_header)],
            [Paragraph(f"<b>Module:</b> {module}<br/><b>Description:</b> {desc}<br/><b>Actual Result:</b> {actual_res}<br/><b>Impact:</b> {impact}", cell_style), Paragraph("", cell_style)]
        ]
        bug_table = Table(bug_data, colWidths=[380, 160])
        bug_table.setStyle(TableStyle([
            ('SPAN', (0, 1), (1, 1)),
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#C53030") if severity == "High" else colors.HexColor("#DD6B20")),
            ('BACKGROUND', (0, 1), (-1, 1), bg_light),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('LEFTPADDING', (0, 0), (-1, -1), 5),
            ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ]))
        elements.append(KeepTogether([bug_table, Spacer(1, 6)]))

    # 7. Additional Observations
    elements.append(Paragraph("7. Additional Observations", h1_style))
    obs_text = (
        "<b>7.1 Employee ID Retention:</b> When adding consecutive employees, the ID field pre-filled previously submitted numbers.<br/>"
        "<b>7.2 Employee Name Search:</b> Autocomplete search works effectively when full name recommendations are selected.<br/>"
        "<b>7.3 Employee ID Search:</b> Partial ID searches (e.g. '069') do not match records, whereas full ID ('0694') works.<br/>"
        "<b>7.4 List Ordering:</b> Newly added employees appear based on default sorting rather than top of list.<br/>"
        "<b>7.5 Search State Reset:</b> Immediate search post-deletion requires clicking 'Reset' to clear cached parameters.<br/>"
        "<b>7.6 Recovery Email Requirement:</b> Employee creation does not mandate email binding unless user login account is enabled."
    )
    elements.append(Paragraph(obs_text, body_style))

    # 8. Manual Login Test Script
    elements.append(Paragraph("8. Manual Login Test Script", h1_style))
    elements.append(Paragraph(
        "<b>Objective:</b> Verify that a valid user can log into OrangeHRM, access the Dashboard, and log out.<br/>"
        "<b>Steps:</b> 1. Open login page → 2. Enter Admin → 3. Enter admin123 → 4. Click Login → 5. Verify Dashboard header → 6. Click User Profile → 7. Click Logout → 8. Verify return to Login URL.",
        body_style
    ))

    # 9. Automation Approach & Architecture
    elements.append(Paragraph("9. Automation Approach & Technology Stack", h1_style))
    tech_stack_data = [
        [Paragraph("Component", cell_header), Paragraph("Technology / Tool", cell_header)],
        [Paragraph("Programming Language", cell_style), Paragraph("Python 3.12", cell_style)],
        [Paragraph("Automation Library", cell_style), Paragraph("Selenium WebDriver 4.x", cell_style)],
        [Paragraph("Test Runner Framework", cell_style), Paragraph("PyTest", cell_style)],
        [Paragraph("Design Pattern", cell_style), Paragraph("Page Object Model (POM)", cell_style)],
        [Paragraph("Browser Driver", cell_style), Paragraph("Google Chrome (Selenium Automated Manager)", cell_style)],
        [Paragraph("Version Control", cell_style), Paragraph("Git & GitHub", cell_style)]
    ]
    tech_table = Table(tech_stack_data, colWidths=[180, 360])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, bg_light])
    ]))
    elements.append(tech_table)
    elements.append(Spacer(1, 8))

    # 10. Deliverables & Submission Checklist
    elements.append(Paragraph("10. Deliverables & Submission Links", h1_style))
    elements.append(Paragraph(
        "<b>GitHub Repository:</b> [ADD YOUR GITHUB LINK HERE]<br/>"
        "<i>Includes full POM framework: pages/login_page.py, pages/dashboard_page.py, pages/pim_page.py, tests/conftest.py, tests/test_login.py, tests/test_employee_management.py, requirements.txt, pytest.ini.</i><br/><br/>"
        "<b>Loom Video Walkthrough:</b> [ADD YOUR LOOM LINK HERE]<br/>"
        "<i>2–3 minute walkthrough demonstrating manual findings, POM architecture, and Selenium PyTest execution.</i>",
        body_style
    ))

    # 11. Conclusion
    elements.append(Paragraph("11. Conclusion", h1_style))
    elements.append(Paragraph(
        "The manual testing phase successfully validated OrangeHRM login and employee management modules across 17 distinct scenarios. "
        "Key findings including generic error messaging, keyboard accessibility gaps, and server-side 504 recovery timeouts were identified and documented. "
        "The automated test suite built with Python, Selenium, PyTest, and Page Object Model (POM) automates end-to-end employee lifecycle workflows cleanly without hardcoding dynamic employee IDs.",
        body_style
    ))

    doc.build(elements)
    print(f"PDF generated successfully: {target_path}")

if __name__ == "__main__":
    build_pdf()
