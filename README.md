# 🤖 AI-Powered Web Test Case Generator

An AI-assisted QA tool that helps manual testers generate application-specific test cases by providing a **web application URL and test credentials**.

The tool uses **Playwright** to explore the application, identify pages, elements, and user workflows, and then uses an **AI model** to generate structured, domain-specific test cases.

The generated test cases can be exported to **Excel**, where manual testers can execute each scenario and mark it as **Working, Not Working, Blocked, or Not Tested**.



## 🎯 Project Objective

Manual testers often spend significant time:

* Understanding application workflows
* Identifying test scenarios
* Writing test cases
* Creating positive and negative scenarios
* Preparing regression test cases
* Maintaining Excel test-case sheets

This project aims to reduce that repetitive work by combining **browser automation + AI + structured QA test design**.

The goal is **not to replace manual testers**.

Instead, the tool acts as a QA assistant that helps testers discover and prepare test coverage faster, while the tester remains responsible for validating the actual application behavior.



# 🔄 How It Works


                  Manual Tester
                       │
                       ▼
             ┌────────────────────┐
             │ Application Details│
             │                    │
             │ URL                │
             │ Username           │
             │ Password           │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │ Playwright Engine  │
             │                    │
             │ Login              │
             │ Navigate           │
             │ Discover Pages     │
             │ Discover Elements  │
             │ Discover Actions   │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │ Application Model  │
             │                    │
             │ Pages              │
             │ Workflows          │
             │ Actions            │
             │ Forms              │
             │ Navigation         │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │     AI QA Engine   │
             │                    │
             │ Domain Detection   │
             │ Workflow Analysis  │
             │ Test Generation    │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │ Generated Test     │
             │ Cases              │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │    Excel Report    │
             │                    │
             │ Test Case          │
             │ Expected Result    │
             │ Priority           │
             │ Status             │
             │ Comments           │
             └─────────┬──────────┘
                       │
                       ▼
                  Manual Tester


# 🛒 Example: E-Commerce Application

Suppose the tester provides an e-commerce application.


Application URL:
https://example-shop.com

Username:
test_user

Password:
********


The Playwright engine explores the application and discovers workflows such as:

Login
  │
  ▼
Product Listing
  │
  ├── Search Product
  ├── Filter Product
  └── Open Product
          │
          ▼
       Add to Cart
          │
          ├── Increase Quantity
          ├── Decrease Quantity
          └── Remove Item
          │
          ▼
        Checkout
          │
          ├── Address
          ├── Order Summary
          └── Payment
                  │
                  ▼
            Order Confirmation
                  │
                  ▼
                Logout

The AI then uses the discovered application information to generate relevant test cases.



# 📋 Example Generated Test Cases

| ID    | Module   | Scenario                        | Expected Result                 | Priority | Type       | Tester Status |
| ----- | -------- | ------------------------------- | ------------------------------- | -------- | ---------- | ------------- |
| TC001 | Login    | Login with valid credentials    | User successfully logs in       | High     | Positive   | Not Tested    |
| TC002 | Login    | Login with invalid password     | Error message is displayed      | High     | Negative   | Not Tested    |
| TC003 | Product  | Search for an existing product  | Matching products are displayed | Medium   | Functional | Not Tested    |
| TC004 | Cart     | Add product to cart             | Product appears in cart         | High     | Functional | Not Tested    |
| TC005 | Cart     | Increase product quantity       | Product quantity increases      | Medium   | Functional | Not Tested    |
| TC006 | Cart     | Remove product                  | Product is removed from cart    | High     | Negative   | Not Tested    |
| TC007 | Checkout | Checkout with valid information | User proceeds to payment        | High     | Functional | Not Tested    |
| TC008 | Payment  | Complete payment                | Order is successfully placed    | Critical | Functional | Not Tested    |
| TC009 | Logout   | Logout from application         | User is redirected to login     | High     | Functional | Not Tested    |

---

# ✅ Tester Execution

The generated Excel file will allow the manual tester to record the actual result.

Possible statuses:


WORKING
NOT WORKING
BLOCKED
NOT TESTED


For example:


TC001 → WORKING
TC002 → WORKING
TC003 → WORKING
TC004 → NOT WORKING
TC005 → WORKING
TC006 → WORKING
TC007 → BLOCKED


For failed or blocked scenarios, the tester can add:


Comments:
"Cart quantity does not update after clicking +."

Evidence:
Screenshot / attachment


This turns the generated test cases into an actual **manual testing execution sheet**.



# 🌐 Domain-Aware Test Generation

The system should not generate the same generic test cases for every application.

The AI should identify the likely application domain and generate relevant workflows.

### 🛒 E-Commerce


Login
Product Search
Product Details
Cart
Wishlist
Checkout
Payment
Order Confirmation
Logout


### 🏦 Banking


Login
Account Summary
Balance
Transaction History
Fund Transfer
Beneficiary
Payments
Logout


### ✈️ Travel


Login
Search
Filters
Selection
Passenger Details
Booking
Payment
Confirmation
Logout


### 🏥 Healthcare


Login
Patient Search
Patient Details
Appointments
Reports
Prescriptions
Logout


The system should use the **actual application structure** as the primary source rather than blindly assuming that every website follows a predefined workflow.



# 🧪 Test Design Techniques

The AI-generated test cases will be guided by common QA techniques.

### Functional Testing

Verify that application features behave according to requirements.

### Positive Testing

Test valid inputs and expected user behavior.

### Negative Testing

Test invalid inputs, incorrect actions, and error conditions.

### Boundary Value Analysis

Identify important minimum, maximum, and boundary conditions.

### Equivalence Partitioning

Divide input data into valid and invalid classes.

### Validation Testing

Verify required fields, formats, constraints, and validation messages.

### Regression Testing

Identify important workflows that should be retested after application changes.



# 🏗️ Planned Architecture


ai-testcase-generator/
│
├── app/
│   ├── __init__.py
│   ├── scanner/
│   │   ├── browser.py
│   │   ├── navigator.py
│   │   └── discovery.py
│   │
│   ├── ai/
│   │   ├── generator.py
│   │   ├── prompts.py
│   │   └── parser.py
│   │
│   ├── models/
│   │   └── test_case.py
│   │
│   └── exporters/
│       ├── excel.py
│       ├── csv.py
│       └── json.py
│
├── tests/
│   ├── test_scanner.py
│   ├── test_generator.py
│   └── test_exporter.py
│
├── output/
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md


# 🛠️ Technology Stack

## Core

* Python
* Playwright
* Pytest

## AI

* LLM API
* Structured AI output
* Prompt engineering

## Reporting

* Pandas
* OpenPyXL
* Excel
* CSV
* JSON

## Development

* Git
* GitHub
* GitHub Actions

## Planned UI

* Streamlit



# 🔐 Security Considerations

Application credentials are sensitive and should not be stored permanently by the application.

The project will follow these principles:

* Never commit credentials to GitHub
* Use environment variables for local configuration
* Provide `.env.example` instead of real credentials
* Avoid writing passwords to logs
* Avoid including credentials in AI prompts
* Avoid storing credentials in generated Excel files
* Use dummy/test credentials for demonstrations
* Clear session data after testing where appropriate

For the public GitHub version, only test applications and non-sensitive credentials will be used.



# 🚧 Development Roadmap

## Phase 1 — Project Foundation

* [ ] Create Python project structure
* [ ] Configure Playwright
* [ ] Create configuration management
* [ ] Create basic logging
* [ ] Create test-case data model

## Phase 2 — Application Discovery

* [ ] Accept application URL
* [ ] Accept temporary test credentials
* [ ] Launch browser
* [ ] Login to application
* [ ] Discover pages
* [ ] Discover links
* [ ] Discover buttons
* [ ] Discover input fields
* [ ] Capture navigation
* [ ] Identify user workflows

## Phase 3 — AI Test Generation

* [ ] Connect LLM API
* [ ] Detect application domain
* [ ] Analyze discovered workflows
* [ ] Generate functional scenarios
* [ ] Generate positive scenarios
* [ ] Generate negative scenarios
* [ ] Generate boundary scenarios
* [ ] Generate validation scenarios
* [ ] Generate regression scenarios
* [ ] Generate priorities

## Phase 4 — Output Validation

* [ ] Validate AI response structure
* [ ] Detect incomplete test cases
* [ ] Detect duplicate scenarios
* [ ] Validate required fields
* [ ] Ensure consistent test-case IDs

## Phase 5 — Excel Reporting

* [ ] Generate Excel workbook
* [ ] Add test-case formatting
* [ ] Add tester status column
* [ ] Add comments column
* [ ] Add evidence column
* [ ] Add filters
* [ ] Add summary sheet
* [ ] Add execution statistics

## Phase 6 — Tester Execution

* [ ] Working status
* [ ] Not Working status
* [ ] Blocked status
* [ ] Not Tested status
* [ ] Tester comments
* [ ] Evidence tracking

## Phase 7 — Web Interface

* [ ] Application URL input
* [ ] Secure credential input
* [ ] Start scan button
* [ ] Discovery progress
* [ ] Test-case preview
* [ ] Excel download
* [ ] Execution summary

## Phase 8 — CI/CD & Quality

* [ ] Unit tests
* [ ] Integration tests
* [ ] GitHub Actions
* [ ] Automated test execution
* [ ] Code quality checks
* [ ] Test reports



# 📊 Planned Execution Summary

After testers execute the generated test cases, the Excel report should provide a summary such as:


Total Test Cases     : 42
Working              : 34
Not Working          : 5
Blocked              : 2
Not Tested           : 1

Execution             : 97.6%
Pass Rate             : 81.0%
Failure Rate          : 11.9%
Blocked Rate          : 4.8%


The summary should help the tester quickly understand the application's current test status.



# ⚠️ Important Design Principle

AI-generated test cases are **suggestions, not truth**.

The system should never assume that an AI-generated scenario is automatically correct.

The workflow is:


AI generates
      ↓
System validates structure
      ↓
Manual tester reviews
      ↓
Manual tester executes
      ↓
Actual result recorded


Human QA judgment remains part of the process.



# 🎓 Learning Goals

This project is designed to explore how AI can assist real-world software testing.

The project combines:

Software Testing
       +
Python
       +
Playwright
       +
Test Automation
       +
AI-assisted QA
       +
Excel Reporting
       +
CI/CD


The primary focus is building a practical QA tool rather than simply demonstrating an AI API.

---

# 📌 Project Status

🚧 **Early Development**

The project is currently being designed and will be implemented incrementally.

---

## 👨‍💻 Author

**Murali Challa**

Python Automation Test Engineer

GitHub: [@muralichalla0204](https://github.com/muralichalla0204)
