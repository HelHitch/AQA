from Pages.log_in_page import LoginPage
from Pages.sidebar import SideBar


class Test_LogOut:
    def __init__(self, driver):
        super().__init__(driver)
        self.LogInPage = LoginPage(self)
        self.SideBar = SideBar(self)

    def test_log_out(self):
        self.LogInPage.login("standard_user", "secret_sauce")
        self.SideBar.choose_sidebar_element(SideBar.LOG_OUT_BTN)
        self.LogInPage.element_is_visible(LoginPage.LOG_IN_BUTTON)
