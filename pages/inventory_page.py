from selenium.webdriver.common.by import By


class InventoryPage:
    TITLE = (By.CSS_SELECTOR, ".title")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")

    def __init__(self, driver):
        self.driver = driver

    def title(self):
        return self.driver.find_element(*self.TITLE).text

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.ADD_BACKPACK).click()

    def cart_count(self):
        return self.driver.find_element(*self.CART_BADGE).text
