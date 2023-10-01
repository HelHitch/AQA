from Pages.BasePage import BasePage


class SideBar(BasePage):
    BURGER_MENU = (By.XPATH, "//button[contains(@id, 'burger-menu')]")
    LOG_OUT_BTN = (By.XPATH, "//a[contains(@id, 'logout_sidebar_link')]")

    def __init__(self, driver):
        super().__init__(driver)

    def choose_sidebar_element(self):
        self.click(self.BURGER_MENU)
        self.click(self.LOG_OUT_BTN)
