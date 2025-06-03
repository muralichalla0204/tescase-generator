{
  "test_id": "TC-101",
  "category": "authentication",
  "description": "Verify login with valid credentials",
  "conditions": {
    "required_elements": ["#username", "#password", ".login-btn"],
    "required_functionality": ["form_submission"],
    "criticality": "high"
  },
  "steps": [
    "Enter valid username",
    "Enter valid password",
    "Click login button",
    "Verify dashboard loads"
  ]
}
