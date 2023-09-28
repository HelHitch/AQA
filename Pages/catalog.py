
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):

		catalog_block = (By.ID , "inventory_container")
		URL = "https://www.saucedemo.com/inventory.html"
		ITEM_LOCATOR = (By.XPATH , "//button[contains(@class, 'btn_inventory')]")
		CARD_LOCATOR = (By.XPATH , "//span[contains(@class, 'shopping_cart_badge')]")

		def __init__(self, driver, url = URL):
				super().__init__(driver, url)
				self.driver.get(url)

		"""Paste data into form and authorize"""
		def add_element_to_card(self):
				self.click(self.ITEM_LOCATOR)

		def add_random_element_to_card(self):
				self.click_random_element_from_list(self.ITEM_LOCATOR)


