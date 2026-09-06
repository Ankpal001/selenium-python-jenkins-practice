import os

TEST_ENV = os.getenv("TEST_ENV", "qa")
print(f"Running tests in environment: {TEST_ENV}")

BASE_URL = "https://www.saucedemo.com/"
STANDARD_USER = "standard_user"
STANDARD_PASSWORD = "secret_sauce"