# 📋 Manual Test Cases - Retro Gaming Store (Atomic)

## Overview
This document contains atomic manual test cases written by manual QA testers for the Retro Gaming Store, based on actual implementation from the [GitHub repository](https://github.com/LightNeO/retro-gaming-store). Each test case verifies exactly one specific functionality.

**Document Version:** 5.0  
**Last Updated:** January 2025  
**Test Environment:** Production (Railway) - https://web-production-c47e.up.railway.app/  
**Browser Requirements:** Chrome and Firefox  

---

## 🎯 Test Case Template
Each test case follows this structure:
- **Title**: Clear, descriptive test case name
- **ID**: Unique test case identifier
- **Priority**: High/Medium/Low
- **Preconditions**: Required setup before test execution
- **Test Data**: Required data for test execution
- **Steps**: Detailed step-by-step instructions
- **Expected Result**: What should happen after test execution

---

## 🏠 Homepage Test Cases

### TC-001: Verify Homepage Loads Within 5 Seconds
**ID:** TC-001  
**Priority:** High  
**Preconditions:** Browser is open, user is not logged in  
**Test Data:** None  

**Steps:**
1. Navigate to the homepage URL
2. Start timer
3. Wait for page to fully load
4. Stop timer

**Expected Result:**
- Page loads within 8 seconds

---

### TC-002: Verify Homepage Displays Correct Page Title
**ID:** TC-002  
**Priority:** High  
**Preconditions:** User is on homepage  
**Test Data:** None  

**Steps:**
1. Navigate to the homepage URL
2. Wait for page to fully load
3. Check the page title

**Expected Result:**
- Page title displays "Retro Gaming Store"

---

### TC-003: Verify Homepage Displays Header Navigation Menu
**ID:** TC-003  
**Priority:** High  
**Preconditions:** User is on homepage  
**Test Data:** None  

**Steps:**
1. Navigate to the homepage URL
2. Wait for page to fully load
3. Locate the header navigation menu

**Expected Result:**
- Header navigation menu is visible on the page

---

### TC-004: Verify Header Navigation Menu Contains Required Items
**ID:** TC-004  
**Priority:** High  
**Preconditions:** User is on homepage  
**Test Data:** None  

**Steps:**
1. Navigate to the homepage URL
2. Wait for page to fully load
3. Locate the header navigation menu
4. Check for menu items: Home, Products, Cart, Login, Register

**Expected Result:**
- Header navigation menu contains all required menu items: Home, Products, Cart, Login, Register

---

### TC-005: Verify Homepage Displays Footer
**ID:** TC-005  
**Priority:** Medium  
**Preconditions:** User is on homepage  
**Test Data:** None  

**Steps:**
1. Navigate to the homepage URL
2. Wait for page to fully load
3. Scroll to the bottom of the page
4. Locate the footer

**Expected Result:**
- Footer is displayed at the bottom of the page

---

### TC-006: Verify Homepage Displays Retro Gaming Aesthetic Elements
**ID:** TC-006  
**Priority:** Medium  
**Preconditions:** User is on homepage  
**Test Data:** None  

**Steps:**
1. Navigate to the homepage URL
2. Wait for page to fully load
3. Look for retro gaming aesthetic elements on the page

**Expected Result:**
- Retro gaming aesthetic elements are visible on the page

---

### TC-007: Verify Products Menu Item Hover Effect
**ID:** TC-007  
**Priority:** Medium  
**Preconditions:** User is on homepage  
**Test Data:** None  

**Steps:**
1. Navigate to the homepage URL
2. Wait for page to fully load
3. Locate the header navigation menu
4. Hover over the "Products" menu item

**Expected Result:**
- Hover effect is displayed when mouse is over "Products" menu item

---

### TC-008: Verify Products Menu Item Hover Effect Disappears
**ID:** TC-008  
**Priority:** Medium  
**Preconditions:** User is on homepage, hovering over Products menu item  
**Test Data:** None  

**Steps:**
1. Move mouse away from "Products" menu item

**Expected Result:**
- Hover effect disappears when mouse moves away from menu item

---

### TC-009: Verify Navigation to Products Page
**ID:** TC-009  
**Priority:** High  
**Preconditions:** User is on homepage  
**Test Data:** None  

**Steps:**
1. Navigate to the homepage URL
2. Wait for page to fully load
3. Locate the header navigation menu
4. Click on the "Products" menu item
5. Wait for page navigation to complete

**Expected Result:**
- URL changes to products page URL

---

### TC-010: Verify Products Page Loads Successfully
**ID:** TC-010  
**Priority:** High  
**Preconditions:** User clicked on Products menu item  
**Test Data:** None  

**Steps:**
1. Wait for products page to load after clicking Products menu item

**Expected Result:**
- Products page loads successfully

---

### TC-011: Verify Footer Displays Contact Information
**ID:** TC-011  
**Priority:** Medium  
**Preconditions:** User is on homepage  
**Test Data:** None  

**Steps:**
1. Navigate to the homepage URL
2. Wait for page to fully load
3. Scroll to the bottom of the page
4. Locate the footer
5. Check for contact information

**Expected Result:**
- Footer displays contact information

---

### TC-012: Verify Facebook Social Media Icon is Visible
**ID:** TC-012  
**Priority:** Medium  
**Preconditions:** User is on homepage  
**Test Data:** None  

**Steps:**
1. Navigate to the homepage URL
2. Wait for page to fully load
3. Scroll to the bottom of the page
4. Locate the footer
5. Look for Facebook social media icon

**Expected Result:**
- Facebook social media icon is visible in the footer

---

### TC-013: Verify Facebook Social Media Link Opens in New Tab
**ID:** TC-013  
**Priority:** Medium  
**Preconditions:** User is on homepage  
**Test Data:** None  

**Steps:**
1. Navigate to the homepage URL
2. Wait for page to fully load
3. Scroll to the bottom of the page
4. Locate the footer
5. Click on Facebook icon

**Expected Result:**
- Facebook link opens in new tab/window

---

### TC-014: Verify Twitter Social Media Icon is Visible
**ID:** TC-014  
**Priority:** Medium  
**Preconditions:** User is on homepage  
**Test Data:** None  

**Steps:**
1. Navigate to the homepage URL
2. Wait for page to fully load
3. Scroll to the bottom of the page
4. Locate the footer
5. Look for Twitter social media icon

**Expected Result:**
- Twitter social media icon is visible in the footer

---

### TC-015: Verify Twitter Social Media Link Opens in New Tab
**ID:** TC-015  
**Priority:** Medium  
**Preconditions:** User is on homepage  
**Test Data:** None  

**Steps:**
1. Navigate to the homepage URL
2. Wait for page to fully load
3. Scroll to the bottom of the page
4. Locate the footer
5. Click on Twitter icon

**Expected Result:**
- Twitter link opens in new tab/window

---

## 🔐 Authentication Test Cases

### TC-016: Verify Registration Page Loads
**ID:** TC-016  
**Priority:** High  
**Preconditions:** User is not logged in, browser is open  
**Test Data:** None  

**Steps:**
1. Navigate to registration page
2. Wait for page to load

**Expected Result:**
- Registration page loads successfully

---

### TC-017: Verify Username Field is Present on Registration Page
**ID:** TC-017  
**Priority:** High  
**Preconditions:** User is on registration page  
**Test Data:** None  

**Steps:**
1. Locate the username field on the registration page

**Expected Result:**
- Username field is present on the registration page

---

### TC-018: Verify Email Field is Present on Registration Page
**ID:** TC-018  
**Priority:** High  
**Preconditions:** User is on registration page  
**Test Data:** None  

**Steps:**
1. Locate the email field on the registration page

**Expected Result:**
- Email field is present on the registration page

---

### TC-019: Verify Password Field is Present on Registration Page
**ID:** TC-019  
**Priority:** High  
**Preconditions:** User is on registration page  
**Test Data:** None  

**Steps:**
1. Locate the password field on the registration page

**Expected Result:**
- Password field is present on the registration page

---

### TC-020: Verify Confirm Password Field is Present on Registration Page
**ID:** TC-020  
**Priority:** High  
**Preconditions:** User is on registration page  
**Test Data:** None  

**Steps:**
1. Locate the confirm password field on the registration page

**Expected Result:**
- Confirm password field is present on the registration page

---

### TC-021: Verify Register Button is Present on Registration Page
**ID:** TC-021  
**Priority:** High  
**Preconditions:** User is on registration page  
**Test Data:** None  

**Steps:**
1. Locate the Register button on the registration page

**Expected Result:**
- Register button is present on the registration page

---

### TC-022: Verify Username Field Accepts Valid Input
**ID:** TC-022  
**Priority:** High  
**Preconditions:** User is on registration page  
**Test Data:** Username: "testuser123"  

**Steps:**
1. Locate the username field on the registration page
2. Enter "testuser123" in the username field

**Expected Result:**
- Username field accepts the input "testuser123"

---

### TC-023: Verify Email Field Accepts Valid Input
**ID:** TC-023  
**Priority:** High  
**Preconditions:** User is on registration page  
**Test Data:** Email: "test@example.com"  

**Steps:**
1. Locate the email field on the registration page
2. Enter "test@example.com" in the email field

**Expected Result:**
- Email field accepts the input "test@example.com"

---

### TC-024: Verify Password Field Accepts Valid Input
**ID:** TC-024  
**Priority:** High  
**Preconditions:** User is on registration page  
**Test Data:** Password: "TestPass123!"  

**Steps:**
1. Locate the password field on the registration page
2. Enter "TestPass123!" in the password field

**Expected Result:**
- Password field accepts the input "TestPass123!"

---

### TC-025: Verify Confirm Password Field Accepts Valid Input
**ID:** TC-025  
**Priority:** High  
**Preconditions:** User is on registration page  
**Test Data:** Confirm Password: "TestPass123!"  

**Steps:**
1. Locate the confirm password field on the registration page
2. Enter "TestPass123!" in the confirm password field

**Expected Result:**
- Confirm password field accepts the input "TestPass123!"

---

### TC-026: Verify Registration with Valid Data Completes Successfully
**ID:** TC-026  
**Priority:** High  
**Preconditions:** User is on registration page with valid data filled  
**Test Data:** Username: "testuser123", Email: "test@example.com", Password: "TestPass123!", Confirm Password: "TestPass123!"  

**Steps:**
1. Enter "testuser123" in the username field
2. Enter "test@example.com" in the email field
3. Enter "TestPass123!" in the password field
4. Enter "TestPass123!" in the confirm password field
5. Click the "Register" button
6. Wait for registration process to complete

**Expected Result:**
- Registration process completes successfully

---

### TC-027: Verify User is Automatically Logged In After Registration
**ID:** TC-027  
**Priority:** High  
**Preconditions:** User completed registration successfully  
**Test Data:** None  

**Steps:**
1. Complete registration process with valid data
2. Check user authentication status

**Expected Result:**
- User is automatically logged in after successful registration

---

### TC-028: Verify User is Redirected After Successful Registration
**ID:** TC-028  
**Priority:** High  
**Preconditions:** User completed registration successfully  
**Test Data:** None  

**Steps:**
1. Complete registration process with valid data
2. Check current page URL

**Expected Result:**
- User is redirected to homepage or profile page after successful registration

---

### TC-029: Verify Registration Form Displays Error for Invalid Email Format
**ID:** TC-029  
**Priority:** High  
**Preconditions:** User is on registration page  
**Test Data:** Username: "testuser456", Email: "invalid-email", Password: "TestPass123!", Confirm Password: "TestPass123!"  

**Steps:**
1. Enter "testuser456" in the username field
2. Enter "invalid-email" in the email field
3. Enter "TestPass123!" in the password field
4. Enter "TestPass123!" in the confirm password field
5. Click the "Register" button

**Expected Result:**
- Form displays error message for invalid email format

---

### TC-030: Verify Registration Process Does Not Complete with Invalid Email
**ID:** TC-030  
**Priority:** High  
**Preconditions:** User submitted registration form with invalid email  
**Test Data:** None  

**Steps:**
1. Submit registration form with invalid email format
2. Check if registration process completes

**Expected Result:**
- Registration process does not complete with invalid email format

---

### TC-031: Verify User Remains on Registration Page with Invalid Email
**ID:** TC-031  
**Priority:** High  
**Preconditions:** User submitted registration form with invalid email  
**Test Data:** None  

**Steps:**
1. Submit registration form with invalid email format
2. Check current page URL

**Expected Result:**
- User remains on registration page after submitting invalid email format

---

### TC-032: Verify Login Page Loads
**ID:** TC-032  
**Priority:** High  
**Preconditions:** User is not logged in, browser is open  
**Test Data:** None  

**Steps:**
1. Navigate to login page
2. Wait for page to load

**Expected Result:**
- Login page loads successfully

---

### TC-033: Verify Username Field is Present on Login Page
**ID:** TC-033  
**Priority:** High  
**Preconditions:** User is on login page  
**Test Data:** None  

**Steps:**
1. Locate the username field on the login page

**Expected Result:**
- Username field is present on the login page

---

### TC-034: Verify Password Field is Present on Login Page
**ID:** TC-034  
**Priority:** High  
**Preconditions:** User is on login page  
**Test Data:** None  

**Steps:**
1. Locate the password field on the login page

**Expected Result:**
- Password field is present on the login page

---

### TC-035: Verify Remember Me Checkbox is Present on Login Page
**ID:** TC-035  
**Priority:** Medium  
**Preconditions:** User is on login page  
**Test Data:** None  

**Steps:**
1. Locate the "Remember Me" checkbox on the login page

**Expected Result:**
- "Remember Me" checkbox is present on the login page

---

### TC-036: Verify Login Button is Present on Login Page
**ID:** TC-036  
**Priority:** High  
**Preconditions:** User is on login page  
**Test Data:** None  

**Steps:**
1. Locate the Login button on the login page

**Expected Result:**
- Login button is present on the login page

---

### TC-037: Verify Username Field Accepts Valid Input on Login Page
**ID:** TC-037  
**Priority:** High  
**Preconditions:** User is on login page  
**Test Data:** Username: [valid username]  

**Steps:**
1. Locate the username field on the login page
2. Enter valid username in the username field

**Expected Result:**
- Username field accepts the valid username input

---

### TC-038: Verify Password Field Accepts Valid Input on Login Page
**ID:** TC-038  
**Priority:** High  
**Preconditions:** User is on login page  
**Test Data:** Password: [valid password]  

**Steps:**
1. Locate the password field on the login page
2. Enter valid password in the password field

**Expected Result:**
- Password field accepts the valid password input

---

### TC-039: Verify Remember Me Checkbox Can Be Checked
**ID:** TC-039  
**Priority:** Medium  
**Preconditions:** User is on login page  
**Test Data:** None  

**Steps:**
1. Locate the "Remember Me" checkbox on the login page
2. Click on the "Remember Me" checkbox

**Expected Result:**
- "Remember Me" checkbox can be checked

---

### TC-040: Verify Login with Valid Credentials Completes Successfully
**ID:** TC-040  
**Priority:** High  
**Preconditions:** User is on login page with valid credentials filled  
**Test Data:** Username: [valid username], Password: [valid password]  

**Steps:**
1. Enter valid username in the username field
2. Enter valid password in the password field
3. Check the "Remember Me" checkbox
4. Click the "Login" button
5. Wait for authentication process to complete

**Expected Result:**
- Authentication process completes successfully

---

### TC-041: Verify JWT Token is Stored After Successful Login
**ID:** TC-041  
**Priority:** High  
**Preconditions:** User completed login successfully  
**Test Data:** None  

**Steps:**
1. Complete login process with valid credentials
2. Check if JWT token is stored

**Expected Result:**
- JWT token is stored after successful login

---

### TC-042: Verify User is Redirected After Successful Login
**ID:** TC-042  
**Priority:** High  
**Preconditions:** User completed login successfully  
**Test Data:** None  

**Steps:**
1. Complete login process with valid credentials
2. Check current page URL

**Expected Result:**
- User is redirected to homepage or profile page after successful login

---

### TC-043: Verify Login Fails with Invalid Credentials
**ID:** TC-043  
**Priority:** High  
**Preconditions:** User is on login page  
**Test Data:** Username: "invaliduser", Password: "wrongpassword"  

**Steps:**
1. Enter "invaliduser" in the username field
2. Enter "wrongpassword" in the password field
3. Click the "Login" button

**Expected Result:**
- Login fails with invalid credentials

---

### TC-044: Verify Error Message is Displayed for Invalid Login
**ID:** TC-044  
**Priority:** High  
**Preconditions:** User submitted login form with invalid credentials  
**Test Data:** None  

**Steps:**
1. Submit login form with invalid credentials
2. Look for error message

**Expected Result:**
- Error message is displayed for invalid login attempt

---

### TC-045: Verify User Remains on Login Page After Invalid Login
**ID:** TC-045  
**Priority:** High  
**Preconditions:** User submitted login form with invalid credentials  
**Test Data:** None  

**Steps:**
1. Submit login form with invalid credentials
2. Check current page URL

**Expected Result:**
- User remains on login page after invalid login attempt

---

### TC-046: Verify Form Fields Are Not Cleared After Invalid Login
**ID:** TC-046  
**Priority:** Medium  
**Preconditions:** User submitted login form with invalid credentials  
**Test Data:** None  

**Steps:**
1. Submit login form with invalid credentials
2. Check if form fields are cleared

**Expected Result:**
- Form fields are not cleared after invalid login attempt

---

### TC-047: Verify Logout Button is Visible When User is Logged In
**ID:** TC-047  
**Priority:** Medium  
**Preconditions:** User is logged in  
**Test Data:** None  

**Steps:**
1. Navigate to any page while logged in
2. Look for logout button/link

**Expected Result:**
- Logout button/link is visible when user is logged in

---

### TC-048: Verify Logout Process Completes Successfully
**ID:** TC-048  
**Priority:** Medium  
**Preconditions:** User is logged in  
**Test Data:** None  

**Steps:**
1. Locate the logout button/link
2. Click on the logout button
3. Wait for logout process to complete

**Expected Result:**
- Logout process completes successfully

---

### TC-049: Verify JWT Token is Cleared After Logout
**ID:** TC-049  
**Priority:** Medium  
**Preconditions:** User completed logout process  
**Test Data:** None  

**Steps:**
1. Complete logout process
2. Check if JWT token is cleared

**Expected Result:**
- JWT token is cleared after logout

---

### TC-050: Verify User is Redirected to Homepage After Logout
**ID:** TC-050  
**Priority:** Medium  
**Preconditions:** User completed logout process  
**Test Data:** None  

**Steps:**
1. Complete logout process
2. Check current page URL

**Expected Result:**
- User is redirected to homepage after logout

---

### TC-051: Verify Login/Register Links Are Visible After Logout
**ID:** TC-051  
**Priority:** Medium  
**Preconditions:** User completed logout process  
**Test Data:** None  

**Steps:**
1. Complete logout process
2. Check navigation menu for Login/Register links

**Expected Result:**
- Login/Register links are visible in navigation after logout

---

## 🐛 Known Bug Testing Summary

### Bug Test Cases Implemented:
1. **TC-029**: Email validation bug testing
2. **TC-030**: Registration process failure with invalid email
3. **TC-031**: User remains on registration page with invalid email

### Bug Testing Strategy:
- Each bug test case is atomic and tests one specific bug
- Expected results clearly state when the bug occurs
- Test cases are repeatable and measurable

---

## 📊 Test Execution Guidelines

### Test Environment Setup:
1. **Browser Requirements**: Chrome, Firefox
2. **Screen Resolutions**: Desktop (1920x1080), Tablet (768x1024), Mobile (320x568)
3. **Network Conditions**: Fast 3G, Slow 3G, Offline
4. **User Types**: Guest, Registered User, Admin

### Test Data Management:
1. **Test Users**: Create dedicated test accounts
2. **Test Products**: Use consistent test product data
3. **Test Orders**: Create test orders for order management testing
4. **Data Cleanup**: Implement cleanup after test execution

### Reporting Requirements:
1. **Test Results**: Pass/Fail status for each test case
2. **Bug Reports**: Detailed bug documentation with steps to reproduce
3. **Performance Metrics**: Page load times, response times
4. **Screenshots**: Capture screenshots for failed tests

---

## 🎯 Automation Implementation Notes

### Priority Implementation Order:
1. **High Priority**: TC-001 to TC-051 (Homepage, Authentication)
2. **High Priority**: Shopping Cart and Checkout test cases
3. **Medium Priority**: Product Browsing test cases
4. **Medium Priority**: Orders and Profile test cases
5. **Low Priority**: Admin and Responsive test cases

### Automation Best Practices:
1. **Page Object Model**: Implement POM for all pages
2. **Data-Driven Testing**: Use external test data files
3. **Parallel Execution**: Implement parallel test execution
4. **Reporting**: Generate comprehensive test reports
5. **Maintenance**: Regular test maintenance and updates

### Success Criteria:
- 90%+ test automation coverage
- <5% flaky tests
- <30 seconds average test execution time
- Comprehensive bug detection and reporting

---

**Document prepared by Manual QA Team**  
**For implementation by QA Automation Team**  
**Version 5.0 - January 2025** 