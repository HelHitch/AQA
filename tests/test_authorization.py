import time

import pytest
import allure
from Pages.log_in import LoginPage
from Pages.catalog import CatalogPage
from TestData.auth_data import return_valid_auth_data, return_not_existing_data
from Pages import BasePage
from tests.conftest import init_parameters


@pytest.mark.auth
class TestAuth:

    @pytest.mark.smoke
    def test_valid_data_auth(self, init_parameters):
        self.LoginPage = LoginPage(init_parameters)
        auth = return_valid_auth_data()
        self.LoginPage.login(auth.login, auth.password)
        self.CatalogPage = CatalogPage(init_parameters)
        self.CatalogPage.element_is_visible(CatalogPage.CATALOG_DIV)

    @pytest.mark.smoke
    @pytest.mark.parametrize("login, password", [('', 'secret_sauce'),
                                                 ('standard_user', ''),
                                                 ('', ''),
                                                 ('abc', '123'),
                                                 ('locked_out_user', 'secret_sauce')])
    def test_invalid_data_auth(self, init_parameters, login, password):
        self.LoginPage = LoginPage(init_parameters)
        self.CatalogPage = CatalogPage(init_parameters)
        self.LoginPage.login(login, password)

        # Empty login
        if len(login) == 0:
            assert self.LoginPage.get_element_text(
                self.LoginPage.ASSERTION_MESSAGES) == "Epic sadface: Username is required"

        # Empty password
        elif len(password) == 0:
            assert self.LoginPage.get_element_text(
                self.LoginPage.ASSERTION_MESSAGES) == "Epic sadface: Password is required"

        # Blocked user
        elif login == 'locked_out_user' and len(password) != 0:
            assert self.LoginPage.get_element_text(
                self.LoginPage.ASSERTION_MESSAGES) == "Epic sadface: Sorry, this user has been locked out."

        # Input data doesn't exist
        elif ((login or password not in return_not_existing_data())
              and (len(login) != 0 and len(password) != 0)):
            assert self.LoginPage.get_element_text(
                self.LoginPage.ASSERTION_MESSAGES) == "Epic sadface: Username and password do not match any user in this service"
