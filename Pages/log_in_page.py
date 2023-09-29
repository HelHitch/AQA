
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

		URL = "https://www.saucedemo.com/"

		LOGIN = (By.ID , "user-name")
		PASSWORD = (By.ID , "password")
		LOG_IN_BUTTON = (By.ID , "login-button")
		ASSERTION_MESSAGES = (By.XPATH , '//div[3]/h3')

		def __init__(self, driver):
				super().__init__(driver, url = self.URL)
				self.driver.get(self.URL)

		"""Paste data into form and authorize"""
		def login(self, username, password):
				self.send_keys(self.LOGIN, username)
				self.send_keys(self.PASSWORD , password)
				self.click(self.LOG_IN_BUTTON)


