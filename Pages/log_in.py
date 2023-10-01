from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    """Page locators"""
    LOGIN = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOG_IN_BUTTON = (By.ID, "login-button")
    ASSERTION_MESSAGES = (By.XPATH, '//div[3]/h3')

    def __init__(self, driver):
        super().__init__(driver)

    """Main functions"""
    def login(self, username, password):
        self.open_page(self.URL)
        self.send_keys(self.LOGIN, username)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOG_IN_BUTTON)
