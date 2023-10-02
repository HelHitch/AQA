import time
import pytest
from selenium.common import TimeoutException

from Pages.catalog import CatalogPage
from Pages.sidebar import SideBar
from Pages.log_in import LoginPage
from TestData.auth_data import return_valid_auth_data


@pytest.mark.auth
class TestLogOut:

    @pytest.mark.smoke
    def test_log_out(self,  init_parameters, completed_auth):
        self.SideBar = SideBar(init_parameters)
        self.CatalogPage = CatalogPage(init_parameters)
        try:
            self.SideBar.choose_sidebar_element(SideBar.LOG_OUT_BTN)
            self.CatalogPage.element_is_visible(LoginPage.LOG_IN_BUTTON)
        except TimeoutException:
            raise TimeoutException('Failed to find element')
