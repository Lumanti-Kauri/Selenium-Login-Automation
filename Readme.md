# Selenium Login Automation Framework

## Project Description

This project is a Selenium automation framework built using Python and Pytest. It automates login functionality testing for a sample web application using the Page Object Model (POM) design pattern.

## Tools & Technologies

- Python
- Selenium
- Pytest
- Page Object Model (POM)
- GitHub Actions (CI/CD)

## Website Tested

https://the-internet.herokuapp.com/login

## Test Cases Covered

1. Valid Login
2. Invalid Password
3. Invalid Username
4. Empty Login
5. Logout Functionality
6. UI Elements Verification
7. Page Title Validation
8. Special Character Validation
9. Long Input Validation
10. Multiple Login Attempts

## Project Structure

pages/
tests/
conftest.py
requirements.txt
pytest.ini

## Run Tests

pip install -r requirements.txt

pytest -v