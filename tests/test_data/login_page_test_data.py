from faker import Faker

fake = Faker()


def get_random_username():
    """Generate a random username for testing"""
    return fake.user_name()


def get_random_email():
    """Generate a random email for testing"""
    return fake.email()


PERFORMANCE_THRESHOLD_MS = 10000
