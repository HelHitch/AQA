from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class SideBar(BasePage):

    """Page locators"""
    BURGER_MENU = (By.XPATH, "//button[contains(@id, 'burger-menu')]")
    LOG_OUT_BTN = (By.XPATH, "//a[contains(@id, 'logout_sidebar_link')]")

    def __init__(self, driver):
        super().__init__(driver)

    """Main functions"""
    def choose_sidebar_element(self, by_element):
        self.click(self.BURGER_MENU)
        self.click(by_element)
