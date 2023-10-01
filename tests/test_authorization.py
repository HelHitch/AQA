import time

import pytest

from Pages.log_in import LoginPage
from Pages.catalog import CatalogPage
from data.auth_data import return_valid_auth_data, return_invalid_auth_data, return_not_existing_data
from Pages import BasePage
from tests.conftest import init_parameters

class TestAuth:

    def test_valid_data_auth(self, init_parameters, username, password):
        self.LoginPage = LoginPage(init_parameters)
        self.CatalogPage = CatalogPage(init_parameters)
        auth = return_valid_auth_data()
        self.LoginPage.login(auth.login, auth.password)
        self.CatalogPage.element_is_visible(CatalogPage.CATALOG_DIV)

    @pytest.mark.parametrize("username, password", [('', 'secret_sauce'),
                                                    ('standard_user', ''),
                                                    ('', ''),
                                                    ('abc', '123'),
                                                    ('blocked_out_user', 'standard_user')])
    def test_invalid_data_auth(self, init_parameters, username, password):
        self.LoginPage = LoginPage(init_parameters)
        self.CatalogPage = CatalogPage(init_parameters)
        self.LoginPage.login(username, password)
        #Empty login
        if len(username) == 0:
            assert self.LoginPage.get_element_text(
                    self.LoginPage.ASSERTION_MESSAGES) == "Epic sadface: Username is required"
        #Empty password
        elif len(password) == 0:
            assert self.LoginPage.get_element_text(
                    self.LoginPage.ASSERTION_MESSAGES) == "Epic sadface: Password is required"
        #Blocked user
        elif username == 'locked_out_user' and len(password) != 0:
            assert self.LoginPage.get_element_text(
                    self.LoginPage.ASSERTION_MESSAGES) == "Epic sadface: Sorry, this user has been locked out."
        # Input dara doesn't exist
        elif ((username or password not in return_not_existing_data())
              and (len(username) !=0 and len(password)!=0)):
            assert self.LoginPage.get_element_text(
                self.LoginPage.ASSERTION_MESSAGES) == "Epic sadface: Username and password do not match any user in this service"

