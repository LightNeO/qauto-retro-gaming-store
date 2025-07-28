# 🧪 QA Automation Testing Framework Plan

## Overview
This document outlines the comprehensive testing framework implementation plan for the Retro Gaming Store using Python, pytest, and Playwright with Page Object Model (POM) design pattern. The framework is designed to implement **150+ test cases** that each verify exactly one specific functionality.

## 🎯 Testing Framework Architecture

### Technology Stack
- **Python 3.9+**: Core programming language
- **pytest**: Test framework and runner
- **Playwright**: Browser automation and testing
- **Page Object Model**: Design pattern for maintainable tests
- **Allure Reports**: Test reporting and visualization
- **pytest-html**: HTML test reports
- **pytest-xdist**: Parallel test execution
- **pytest-bdd**: Behavior-driven development (optional)

### Project Structure
```
tests/
├── conftest.py                 # Pytest configuration and fixtures
├── pages/                      # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py           # Base page with common methods
│   ├── home_page.py           # Homepage interactions
│   ├── login_page.py          # Login page interactions
│   ├── register_page.py       # Registration page interactions
│   ├── products_page.py       # Product listing interactions
│   ├── product_detail_page.py # Product detail interactions
│   ├── cart_page.py           # Shopping cart interactions
│   ├── checkout_page.py       # Checkout process interactions
│   ├── profile_page.py        # User profile interactions
│   ├── orders_page.py         # Order management interactions
│   ├── admin_page.py          # Admin panel interactions
│   └── responsive_page.py     # Responsive design interactions
├── test_data/                  # Test data and configurations
│   ├── __init__.py
│   ├── test_users.py          # Test user credentials
│   ├── test_products.py       # Test product data
│   ├── test_orders.py         # Test order data
│   └── config.py              # Test configuration
├── locators/                   # Element locators for all pages
│   ├── __init__.py
│   ├── base_locators.py       # Common locators and base selectors
│   ├── home_locators.py       # Homepage element locators
│   ├── auth_locators.py       # Authentication page locators
│   ├── product_locators.py    # Product page locators
│   ├── cart_locators.py       # Shopping cart locators
│   ├── checkout_locators.py   # Checkout page locators
│   ├── order_locators.py      # Order management locators
│   ├── profile_locators.py    # User profile locators
│   ├── admin_locators.py      # Admin panel locators
│   └── responsive_locators.py # Responsive design locators
├── utils/                      # Utility functions and helpers
│   ├── __init__.py
│   ├── data_generator.py      # Test data generation
│   ├── api_helpers.py         # API testing helpers
│   ├── screenshot_helper.py   # Screenshot utilities
│   ├── timer_helper.py        # Performance timing utilities
│   └── assertion_helper.py    # Custom assertion utilities
├── test_suites/               # Organized test suites by functionality
│   ├── __init__.py
│   ├── test_homepage/         # Homepage atomic tests
│   │   ├── __init__.py
│   │   ├── test_page_load.py
│   │   ├── test_navigation.py
│   │   ├── test_footer.py
│   │   └── test_responsive.py
│   ├── test_authentication/   # Authentication atomic tests
│   │   ├── __init__.py
│   │   ├── test_registration.py
│   │   ├── test_login.py
│   │   ├── test_logout.py
│   │   └── test_validation.py
│   ├── test_products/         # Product atomic tests
│   │   ├── __init__.py
│   │   ├── test_browsing.py
│   │   ├── test_search.py
│   │   ├── test_details.py
│   │   └── test_ratings.py
│   ├── test_cart/             # Shopping cart atomic tests
│   │   ├── __init__.py
│   │   ├── test_add_items.py
│   │   ├── test_remove_items.py
│   │   ├── test_quantity.py
│   │   └── test_calculations.py
│   ├── test_checkout/         # Checkout atomic tests
│   │   ├── __init__.py
│   │   ├── test_process.py
│   │   ├── test_validation.py
│   │   └── test_confirmation.py
│   ├── test_orders/           # Order management atomic tests
│   │   ├── __init__.py
│   │   ├── test_history.py
│   │   ├── test_details.py
│   │   └── test_status.py
│   ├── test_profile/          # User profile atomic tests
│   │   ├── __init__.py
│   │   ├── test_information.py
│   │   ├── test_password.py
│   │   └── test_preferences.py
│   ├── test_admin/            # Admin panel atomic tests
│   │   ├── __init__.py
│   │   ├── test_login.py
│   │   ├── test_products.py
│   │   ├── test_orders.py
│   │   └── test_users.py
│   └── test_bugs/             # Known bug atomic tests
│       ├── __init__.py
│       ├── test_email_validation.py
│       ├── test_phantom_cart.py
│       ├── test_stuck_button.py
│       ├── test_missing_orders.py
│       ├── test_rating_failure.py
│       └── test_profile_update.py
├── reports/                   # Test reports and screenshots
│   ├── html_reports/
│   ├── allure_reports/
│   ├── screenshots/
│   └── videos/
├── requirements.txt           # Testing dependencies
└── pytest.ini               # Pytest configuration
```

## 📋 Implementation Phases

### Phase 1: Foundation Setup (Week 1)
**Goal**: Set up the basic testing framework infrastructure

#### Tasks:
1. **Environment Setup**
   - Install Python 3.9+
   - Create virtual environment
   - Install testing dependencies
   - Configure pytest settings

2. **Base Configuration**
   - Create `conftest.py` with fixtures
   - Set up Playwright browser configuration
   - Configure test data management
   - Set up reporting framework

3. **Page Object Model Foundation**
   - Create `base_page.py` with interaction methods
   - Implement single-action methods
   - Set up element locators strategy
   - Create utility functions for assertions

4. **Locators Management**
   - Create separate locators directory for all element selectors
   - Implement base locators with common selectors
   - Create page-specific locator files for maintainability
   - Use data-qa attributes and semantic selectors for stability

5. **Test Structure**
   - Create test suite directories for each functionality area
   - Set up test templates
   - Configure test data for scenarios
   - Implement test helpers

#### Deliverables:
- Test framework structure
- Working pytest configuration
- Base page class with methods
- Locators directory with organized element selectors
- Test suite organization structure

### Phase 2: Homepage Tests (Week 2)
**Goal**: Implement all homepage test cases (TC-001 to TC-015)

#### Tasks:
1. **Page Load Tests**
   - TC-001: Verify homepage loads within 8 seconds
   - TC-002: Verify homepage displays correct page title
   - Implement performance timing utilities

2. **Navigation Tests**
   - TC-003: Verify homepage displays header navigation menu
   - TC-004: Verify header navigation menu contains required items
   - TC-007: Verify Products menu item hover effect
   - TC-008: Verify Products menu item hover effect disappears
   - TC-009: Verify navigation to products page
   - TC-010: Verify products page loads successfully

3. **Footer Tests**
   - TC-005: Verify homepage displays footer
   - TC-011: Verify footer displays contact information
   - TC-012: Verify Facebook social media icon is visible
   - TC-013: Verify Facebook social media link opens in new tab
   - TC-014: Verify Twitter social media icon is visible
   - TC-015: Verify Twitter social media link opens in new tab

4. **Aesthetic Tests**
   - TC-006: Verify homepage displays retro gaming aesthetic elements

#### Deliverables:
- Complete homepage page object class
- 15 homepage test cases
- Performance timing utilities
- Social media link testing utilities

### Phase 3: Authentication Tests (Week 3-4)
**Goal**: Implement all authentication test cases (TC-016 to TC-051)

#### Tasks:
1. **Registration Page Tests**
   - TC-016: Verify registration page loads
   - TC-017: Verify username field is present on registration page
   - TC-018: Verify email field is present on registration page
   - TC-019: Verify password field is present on registration page
   - TC-020: Verify confirm password field is present on registration page
   - TC-021: Verify register button is present on registration page

2. **Registration Input Tests**
   - TC-022: Verify username field accepts valid input
   - TC-023: Verify email field accepts valid input
   - TC-024: Verify password field accepts valid input
   - TC-025: Verify confirm password field accepts valid input

3. **Registration Process Tests**
   - TC-026: Verify registration with valid data completes successfully
   - TC-027: Verify user is automatically logged in after registration
   - TC-028: Verify user is redirected after successful registration

4. **Registration Bug Tests**
   - TC-029: Verify registration form displays error for invalid email format
   - TC-030: Verify registration process does not complete with invalid email
   - TC-031: Verify user remains on registration page with invalid email

5. **Login Page Tests**
   - TC-032: Verify login page loads
   - TC-033: Verify username field is present on login page
   - TC-034: Verify password field is present on login page
   - TC-035: Verify remember me checkbox is present on login page
   - TC-036: Verify login button is present on login page

6. **Login Input Tests**
   - TC-037: Verify username field accepts valid input on login page
   - TC-038: Verify password field accepts valid input on login page
   - TC-039: Verify remember me checkbox can be checked

7. **Login Process Tests**
   - TC-040: Verify login with valid credentials completes successfully
   - TC-041: Verify JWT token is stored after successful login
   - TC-042: Verify user is redirected after successful login

8. **Login Error Tests**
   - TC-043: Verify login fails with invalid credentials
   - TC-044: Verify error message is displayed for invalid login
   - TC-045: Verify user remains on login page after invalid login
   - TC-046: Verify form fields are not cleared after invalid login

9. **Logout Tests**
   - TC-047: Verify logout button is visible when user is logged in
   - TC-048: Verify logout process completes successfully
   - TC-049: Verify JWT token is cleared after logout
   - TC-050: Verify user is redirected to homepage after logout
   - TC-051: Verify login/register links are visible after logout

#### Deliverables:
- Complete authentication page object classes
- 36 authentication test cases
- JWT token management utilities
- Form validation testing utilities

### Phase 4: Product Browsing Tests (Week 5)
**Goal**: Implement product browsing test cases

#### Tasks:
1. **Product Listing Tests**
   - Verify products page loads successfully
   - Verify product grid is displayed
   - Verify product cards display required information
   - Verify product images load correctly

2. **Product Search Tests**
   - Verify search bar is present on products page
   - Verify search functionality works with "Atari"
   - Verify search results are displayed
   - Verify search with other terms

3. **Product Detail Tests**
   - Verify product detail page loads
   - Verify product information is displayed correctly
   - Verify add to cart button is present
   - Verify product images display

4. **Product Interaction Tests**
   - Verify clicking product card navigates to detail page
   - Verify product ratings display (if available)
   - Verify product comments display (if available)

#### Deliverables:
- Complete product page object classes
- Product browsing test cases
- Search functionality testing utilities
- Product data validation utilities

### Phase 5: Shopping Cart Tests (Week 6)
**Goal**: Implement shopping cart test cases

#### Tasks:
1. **Add to Cart Tests**
   - Verify add to cart button is present on product detail page
   - Verify item is added to cart successfully
   - Verify cart icon shows updated count
   - Verify cart page displays added item

2. **Cart Management Tests**
   - Verify cart page loads successfully
   - Verify item details are correct in cart
   - Verify quantity selector is present
   - Verify remove button is present

3. **Cart Operations Tests**
   - Verify quantity can be increased
   - Verify quantity can be decreased
   - Verify item can be removed from cart
   - Verify cart total updates correctly

4. **Cart Bug Tests**
   - Verify phantom cart bug (20% chance total doesn't update)
   - Implement retry logic for cart calculations
   - Document bug occurrence rates

#### Deliverables:
- Complete cart page object class
- Shopping cart test cases
- Cart calculation testing utilities
- Bug testing utilities

### Phase 6: Checkout Tests (Week 7)
**Goal**: Implement checkout test cases

#### Tasks:
1. **Checkout Navigation Tests**
   - Verify proceed to checkout button is present
   - Verify checkout page loads successfully
   - Verify checkout form fields are present

2. **Checkout Form Tests**
   - Verify each form field accepts valid input
   - Verify form validation works correctly
   - Verify payment information can be entered

3. **Checkout Process Tests**
   - Verify checkout process completes successfully
   - Verify order confirmation is displayed
   - Verify user is redirected after successful checkout

4. **Checkout Bug Tests**
   - Verify stuck button bug (25% chance button disabled for 5 seconds)
   - Implement wait logic for button state
   - Document bug occurrence rates

#### Deliverables:
- Complete checkout page object class
- Checkout test cases
- Form validation testing utilities
- Payment processing testing utilities

### Phase 7: Order Management Tests (Week 8)
**Goal**: Implement order management test cases

#### Tasks:
1. **Order History Tests**
   - Verify order history section is accessible
   - Verify order history table is displayed
   - Verify order information is correct
   - Verify order details can be viewed

2. **Order Details Tests**
   - Verify order details page loads
   - Verify order information is accurate
   - Verify order status is displayed
   - Verify order items are listed

3. **Order Bug Tests**
   - Verify missing order history bug (20% chance table empty)
   - Implement retry logic for order display
   - Document bug occurrence rates

#### Deliverables:
- Complete orders page object class
- Order management test cases
- Order data validation utilities
- Bug testing utilities

### Phase 8: User Profile Tests (Week 9)
**Goal**: Implement user profile test cases

#### Tasks:
1. **Profile Information Tests**
   - Verify profile page loads successfully
   - Verify profile information is displayed
   - Verify profile can be updated
   - Verify password can be changed

2. **Profile Bug Tests**
   - Verify profile update bug (30% chance update fails)
   - Implement retry logic for profile updates
   - Document bug occurrence rates

#### Deliverables:
- Complete profile page object class
- User profile test cases
- Profile update testing utilities
- Bug testing utilities

### Phase 9: Admin Panel Tests (Week 10)
**Goal**: Implement admin panel test cases

#### Tasks:
1. **Admin Authentication Tests**
   - Verify admin login page loads
   - Verify admin login works correctly
   - Verify admin dashboard is accessible

2. **Admin Management Tests**
   - Verify product management is accessible
   - Verify order management is accessible
   - Verify user management is accessible

#### Deliverables:
- Complete admin page object class
- Admin panel test cases
- Admin authentication testing utilities

### Phase 10: Responsive Design Tests (Week 11)
**Goal**: Implement responsive design test cases

#### Tasks:
1. **Mobile Navigation Tests**
   - Verify navigation adapts to mobile layout
   - Verify hamburger menu works (if present)
   - Verify navigation items are accessible on mobile

2. **Mobile Product Tests**
   - Verify product grid adapts to mobile layout
   - Verify product cards are readable on mobile
   - Verify add to cart buttons are accessible on mobile

#### Deliverables:
- Complete responsive page object class
- Responsive design test cases
- Mobile testing utilities

### Phase 11: Bug Testing Suite (Week 12)
**Goal**: Implement comprehensive bug testing suite

#### Tasks:
1. **Email Validation Bug Tests**
   - Test intentionally broken email validation
   - Verify error messages are displayed
   - Document bug behavior

2. **Phantom Cart Bug Tests**
   - Test cart total calculation bug
   - Implement retry logic
   - Document occurrence rates

3. **Stuck Button Bug Tests**
   - Test checkout button disabled bug
   - Implement wait logic
   - Document occurrence rates

4. **Missing Order History Bug Tests**
   - Test order table empty bug
   - Implement retry logic
   - Document occurrence rates

5. **Rating Submission Bug Tests**
   - Test rating submission failure
   - Implement retry logic
   - Document occurrence rates

6. **Profile Update Bug Tests**
   - Test profile update failure
   - Implement retry logic
   - Document occurrence rates

#### Deliverables:
- Complete bug testing suite
- Bug testing utilities
- Retry logic implementations
- Bug documentation

### Phase 12: Reporting and CI/CD (Week 13)
**Goal**: Implement comprehensive reporting and CI/CD integration

#### Tasks:
1. **Test Reporting**
   - Allure report configuration
   - HTML report setup with test details
   - Screenshot capture for failed tests
   - Video recording for test execution

2. **CI/CD Integration**
   - GitHub Actions setup
   - Parallel test execution
   - Automated reporting for test results
   - Slack notifications for test failures

3. **Performance Testing**
   - Page load time testing
   - API response time testing
   - Browser performance metrics

#### Deliverables:
- Comprehensive test reports
- CI/CD pipeline for test execution
- Performance monitoring
- Automated notifications for test results

## 🎮 Test Implementation Guide

### Test Structure:
```python
# Example test structure
class TestHomepageLoad:
    def test_homepage_loads_within_5_seconds(self, page):
        """TC-001: Verify Homepage Loads Within 5 Seconds"""
        # Single action: measure page load time
        start_time = time.time()
        page.goto("/")
        page.wait_for_load_state("networkidle")
        load_time = time.time() - start_time
        
        # Single assertion: verify load time
        assert load_time <= 5, f"Page loaded in {load_time} seconds, expected <= 5"

class TestPageTitle:
    def test_homepage_displays_correct_title(self, page):
        """TC-002: Verify Homepage Displays Correct Page Title"""
        # Single action: navigate to homepage
        page.goto("/")
        
        # Single assertion: verify page title
        assert page.title() == "Retro Gaming Store"
```

### Locators Management:
```python
# locators/base_locators.py
class BaseLocators:
    """Common locators used across multiple pages"""
    PAGE_TITLE = "title"
    LOADING_SPINNER = "[data-qa='loading-spinner']"
    ERROR_MESSAGE = "[data-qa='error-message']"
    SUCCESS_MESSAGE = "[data-qa='success-message']"
    NAVIGATION_MENU = "[data-qa='navigation-menu']"
    FOOTER = "[data-qa='footer']"

# locators/home_locators.py
class HomeLocators(BaseLocators):
    """Homepage specific locators"""
    PRODUCTS_MENU_ITEM = "[data-qa='products-menu']"
    LOGIN_MENU_ITEM = "[data-qa='login-menu']"
    REGISTER_MENU_ITEM = "[data-qa='register-menu']"
    CART_MENU_ITEM = "[data-qa='cart-menu']"
    FACEBOOK_ICON = "[data-qa='facebook-icon']"
    TWITTER_ICON = "[data-qa='twitter-icon']"
    CONTACT_INFO = "[data-qa='contact-info']"
    RETRO_GAMING_ELEMENTS = "[data-qa='retro-gaming-elements']"

# locators/auth_locators.py
class AuthLocators(BaseLocators):
    """Authentication page locators"""
    USERNAME_FIELD = "[data-qa='username-field']"
    EMAIL_FIELD = "[data-qa='email-field']"
    PASSWORD_FIELD = "[data-qa='password-field']"
    CONFIRM_PASSWORD_FIELD = "[data-qa='confirm-password-field']"
    LOGIN_BUTTON = "[data-qa='login-button']"
    REGISTER_BUTTON = "[data-qa='register-button']"
    REMEMBER_ME_CHECKBOX = "[data-qa='remember-me-checkbox']"
    LOGOUT_BUTTON = "[data-qa='logout-button']"
    EMAIL_ERROR = "[data-qa='email-error']"
    LOGIN_ERROR = "[data-qa='login-error']"
```

### Page Object Model with External Locators:
```python
from locators.home_locators import HomeLocators

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locators = HomeLocators()
    
    def get_page_title(self):
        """Single action: get page title"""
        return self.page.title()
    
    def is_navigation_menu_visible(self):
        """Single action: check if navigation menu is visible"""
        return self.page.is_visible(self.locators.NAVIGATION_MENU)
    
    def get_navigation_menu_items(self):
        """Single action: get navigation menu items"""
        return self.page.locator(self.locators.NAVIGATION_MENU).all_text_contents()
    
    def hover_over_products_menu(self):
        """Single action: hover over products menu item"""
        self.page.hover(self.locators.PRODUCTS_MENU_ITEM)
    
    def click_products_menu(self):
        """Single action: click products menu item"""
        self.page.click(self.locators.PRODUCTS_MENU_ITEM)
```

### Test Data Management:
```python
# test_data/test_data.py
TEST_DATA = {
    'homepage': {
        'expected_title': 'Retro Gaming Store',
        'expected_menu_items': ['Home', 'Products', 'Cart', 'Login', 'Register'],
        'load_timeout': 5
    },
    'registration': {
        'valid_username': 'testuser123',
        'valid_email': 'test@example.com',
        'valid_password': 'TestPass123!',
        'invalid_email': 'invalid-email'
    },
    'login': {
        'valid_username': 'testuser',
        'valid_password': 'TestPass123!',
        'invalid_username': 'invaliduser',
        'invalid_password': 'wrongpassword'
    }
}
```

### Locators Best Practices:
```python
# locators/locator_strategy.py
class LocatorStrategy:
    """Best practices for locator management"""
    
    # Priority order for locators (most stable to least stable)
    LOCATOR_PRIORITY = [
        'data-qa',           # Custom test attributes (most stable)
        'id',                # Unique IDs
        'name',              # Form field names
        'aria-label',        # Accessibility labels
        'class',             # CSS classes (use specific ones)
        'xpath'              # XPath (use as last resort)
    ]

### Bug Test Implementation:
```python
from locators.auth_locators import AuthLocators

class TestEmailValidationBug:
    def test_registration_form_displays_error_for_invalid_email(self, page):
        """TC-029: Verify Registration Form Displays Error for Invalid Email Format"""
        auth_locators = AuthLocators()
        
        # Navigate to registration page
        page.goto("/register")
        
        # Fill form with invalid email
        page.fill(auth_locators.USERNAME_FIELD, "testuser456")
        page.fill(auth_locators.EMAIL_FIELD, "invalid-email")
        page.fill(auth_locators.PASSWORD_FIELD, "TestPass123!")
        page.fill(auth_locators.CONFIRM_PASSWORD_FIELD, "TestPass123!")
        
        # Submit form
        page.click(auth_locators.REGISTER_BUTTON)
        
        # Single assertion: verify error message is displayed
        assert page.is_visible(auth_locators.EMAIL_ERROR)

class TestPhantomCartBug:
    def test_cart_total_update_bug(self, page):
        """TC-019: Test Cart Total Update Bug"""
        # Add items to cart
        self.add_items_to_cart(page, 3)
        
        # Check cart total multiple times
        for i in range(10):
            total = self.get_cart_total(page)
            if total != self.expected_total:
                # Document bug occurrence
                self.log_bug_occurrence("phantom_cart", i+1)
                break
```

## 📊 Test Reporting Strategy

### Allure Reports:
- Individual test case reports
- Screenshot attachments for each test
- Video recordings for test execution
- Performance metrics for each test
- Bug tracking integration for test failures

### HTML Reports:
- Self-contained HTML reports with test details
- Screenshot galleries for each test
- Test execution timeline
- Pass/fail statistics for test cases

## 🚀 CI/CD Integration

### GitHub Actions Workflow:
```yaml
name: QA Automation Tests
on: [push, pull_request]
jobs:
  tests:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        test-suite: [homepage, authentication, products, cart, checkout, orders, profile, admin, responsive, bugs]
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          playwright install
      - name: Run tests
        run: pytest tests/test_suites/test_${{ matrix.test-suite }}/ --parallel 2
      - name: Generate test reports
        run: |
          allure generate reports/allure_reports --clean
          pytest --html=reports/html_reports/report_${{ matrix.test-suite }}.html
```

## 📚 Learning Resources for Testing

### Documentation:
- [Playwright Python Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Best Practices](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
- [Atomic Testing Principles](https://www.guru99.com/test-case-design-techniques.html)

### Practice Exercises for Atomic Tests:
1. Start with single element verification tests
2. Implement single action tests
3. Create single assertion tests
4. Add performance timing tests
5. Implement bug reproduction tests

## 🎯 Success Metrics

### Framework Quality:
- 150+ test cases implemented
- <5% flaky tests
- <10 seconds average test execution time
- Comprehensive bug detection

### Code Quality:
- Clean, maintainable test code
- Proper documentation for each test
- Consistent naming conventions
- Modular architecture for test organization

### Reporting Quality:
- Clear, actionable reports
- Detailed failure analysis for test cases
- Performance metrics
- Bug tracking integration

---

## 💡 Tips for Testing Success

- **Start Small**: Begin with single element verification tests
- **Practice Regularly**: Implement tests daily
- **Document Everything**: Keep notes of your testing learning
- **Ask Questions**: Use the comprehensive test scenarios as reference
- **Iterate**: Improve your tests based on feedback
- **Focus on One Thing**: Each test should verify exactly one functionality
- **Measure Performance**: Track execution time for each test
- **Use External Locators**: Keep all element selectors in separate locator files for maintainability
- **Follow Locator Strategy**: Use data-qa attributes as primary locators for stability
- **Organize Locators**: Group locators by page/functionality for easy maintenance

**Happy Testing! 🎮🧪** 