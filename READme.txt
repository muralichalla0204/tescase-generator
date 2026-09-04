# 🤖 AI Test Case Generator for Manual Testers

An AI-assisted tool that helps manual testers generate structured test cases from software requirements, user stories, or feature descriptions.

The goal is to reduce repetitive test-case writing while helping testers identify functional, negative, validation, boundary, and regression scenarios.

> **Note:** This is a personal QA automation project exploring how AI can assist software testing. It is not intended to replace manual testers or human test judgment.

---

## 🎯 Project Goal

Manual testers often spend significant time converting requirements into detailed test cases.

This project aims to simplify that process:

```text
Requirement / User Story
          │
          ▼
    AI Test Analysis
          │
          ▼
   Test Scenario Generation
          │
          ├── Functional
          ├── Negative
          ├── Validation
          ├── Boundary
          └── Regression
          │
          ▼
    Structured Test Cases
          │
          ▼
     Export / Reporting
```

---

## ✨ Planned Features

### Test Case Generation

* Generate functional test cases
* Generate positive test scenarios
* Generate negative test scenarios
* Generate validation scenarios
* Identify boundary-value scenarios
* Generate regression scenarios
* Assign test priority
* Identify test type

### Structured Test Cases

Each generated test case will contain:

| Field           | Description                             |
| --------------- | --------------------------------------- |
| Test Case ID    | Unique test case identifier             |
| Requirement ID  | Related requirement                     |
| Scenario        | What is being tested                    |
| Preconditions   | Conditions required before testing      |
| Test Steps      | Steps to execute                        |
| Test Data       | Required input data                     |
| Expected Result | Expected application behavior           |
| Priority        | Critical / High / Medium / Low          |
| Test Type       | Functional / Negative / Boundary / etc. |

---

## 🧪 Example

### Input

```text
User should be able to log in using a valid username and password.

The account should be locked after 5 consecutive failed login attempts.
```

### Generated Output

```text
TC001
Scenario: Login with valid credentials
Type: Functional
Priority: High

Steps:
1. Enter a valid username.
2. Enter a valid password.
3. Click Login.

Expected Result:
User should be successfully logged in.
```

```text
TC002
Scenario: Account lockout after consecutive failed attempts
Type: Negative / Security
Priority: Critical

Steps:
1. Enter a valid username.
2. Enter an incorrect password.
3. Repeat the failed login attempt five times.

Expected Result:
The account should be locked after the fifth failed attempt.
```

---

## 🏗️ Planned Architecture

```text
                   ┌─────────────────────┐
                   │ Manual Tester       │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │ Requirement Input   │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │ Prompt / QA Logic   │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │     LLM / AI        │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │ Output Validation   │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │ Structured Tests    │
                   └──────────┬──────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
                JSON/CSV             Excel
```

---

## 🛠️ Technology Stack

### Current

* Python
* Git
* GitHub

### Planned

* LLM API
* Pytest
* Pandas
* OpenPyXL
* JSON
* CSV
* Streamlit

---

## 📁 Planned Project Structure

```text
ai-testcase-generator/
│
├── app/
│   ├── __init__.py
│   ├── generator.py
│   ├── prompts.py
│   └── models.py
│
├── tests/
│   └── test_generator.py
│
├── output/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚧 Development Roadmap

### Phase 1 - Core Generator

* [ ] Accept requirement/user story
* [ ] Connect to LLM API
* [ ] Generate structured test cases
* [ ] Validate AI response
* [ ] Display generated test cases

### Phase 2 - QA Test Design

* [ ] Functional scenarios
* [ ] Positive scenarios
* [ ] Negative scenarios
* [ ] Boundary-value scenarios
* [ ] Validation scenarios
* [ ] Regression scenarios
* [ ] Priority classification

### Phase 3 - Export

* [ ] JSON export
* [ ] CSV export
* [ ] Excel export

### Phase 4 - Traceability

* [ ] Requirement IDs
* [ ] Requirement-to-test mapping
* [ ] Test coverage calculation
* [ ] Duplicate test detection

### Phase 5 - User Interface

* [ ] Simple web interface
* [ ] Requirement input
* [ ] Test-type selection
* [ ] Generate button
* [ ] Test-case preview
* [ ] Download generated test cases

### Phase 6 - Automation & CI

* [ ] Unit tests
* [ ] Integration tests
* [ ] GitHub Actions
* [ ] Automated test execution
* [ ] Test reports

---

## 🔍 QA Principles

The generator will follow common software testing techniques rather than simply asking an AI model to "generate some tests."

The project will explore:

* Equivalence Partitioning
* Boundary Value Analysis
* Positive Testing
* Negative Testing
* Validation Testing
* Functional Testing
* Regression Testing
* Error Handling
* Basic Security Scenarios

---

## 🎓 Learning Goals

This project is being developed to explore the intersection of:

```text
Software Testing
       +
Python
       +
Test Automation
       +
AI-assisted QA
```

The focus is on understanding how AI can **assist testers**, while keeping human review and QA judgment in the process.

---

## 📌 Project Status

🚧 **Currently in development**

Features will be added incrementally as the project evolves.

---

## 👨‍💻 Author

**Murali Challa**

Python Automation Test Engineer

GitHub: [@muralichalla0204](https://github.com/muralichalla0204)
