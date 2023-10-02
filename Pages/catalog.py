from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    """Page locators"""
    CATALOG_DIV = (By.ID, "inventory_container")
    ITEM_LOCATOR = (By.XPATH, "//button[contains(@class, 'btn_inventory')]")
    CARD_LOCATOR = (By.XPATH, "//span[contains(@class, 'shopping_cart_badge')]")

    def __init__(self, driver):
        super().__init__(driver)

    """Main functions"""

    def add_element_to_card(self):
        self.click(self.ITEM_LOCATOR)

    def add_random_element_to_card(self):
        self.click_random_element_from_list(self.ITEM_LOCATOR)
        assert self.get_element_text(self.CARD_LOCATOR) == '1'
