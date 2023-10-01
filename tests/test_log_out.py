import pytest

from Pages.BasePage import BasePage
from Pages.catalog import CatalogPage
from Pages.log_in import LoginPage
from Pages.sidebar import SideBar
from tests.test_authorization import TestAuth


class TestLogOut:

    @pytest.mark.dependency(depends=['test_valid_data_auth'])
    def test_log_out(self, init_parameters):
        self.LoginPage = LoginPage(init_parameters)
        self.SideBar = SideBar(init_parameters)
        self.CatalogPage = CatalogPage(init_parameters)
        self.CatalogPage.open_page(CatalogPage.URL)
        # self.LoginPage.login('standard_user', 'secret_sauce')
        self.SideBar.choose_sidebar_element(SideBar.LOG_OUT_BTN)
        self.CatalogPage.element_is_visible(LoginPage.LOG_IN_BUTTON)
