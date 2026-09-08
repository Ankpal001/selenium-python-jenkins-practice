from config.config import BASE_URL, STANDARD_USER, STANDARD_PASSWORD, TEST_ENV
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_login(driver):
    print(f"Running tests in environment: {TEST_ENV}")
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)

    inventory_page = InventoryPage(driver)

    assert inventory_page.title() == "Products"


def test_add_product_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()

    assert inventory_page.cart_count() == "1"

def test_application_title(driver):
    driver.get("https://www.saucedemo.com/")
    assert driver.title == "Swag Labs"