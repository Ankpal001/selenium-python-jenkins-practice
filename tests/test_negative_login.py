from config.config import BASE_URL
from pages.login_page import LoginPage


def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)
    login_page.login("wrong_user", "wrong_password")

    assert "Username and password do not match" in login_page.error_message()
