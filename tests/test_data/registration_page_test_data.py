from faker import Faker

fake = Faker()


def get_random_username():
    """Generate a random username for testing"""
    return fake.user_name()


def get_random_email():
    """Generate a random email for testing"""
    return fake.email()


def get_random_password():
    """Generate a random password for testing"""
    return fake.password(
        length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
    )


EXPECTED_REGISTRATION_PAGE_TITLE = "Register"
PERFORMANCE_THRESHOLD_MS = 10000
INVALID_USERNAME = " "
VALID_USERNAME = "testuser123"
VALID_EMAIL = "test@test.com"
VALID_PASSWORD = "Test@123"
