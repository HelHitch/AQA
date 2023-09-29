import random
import time

from Pages.BasePage import BasePage
from Pages.catalog import CatalogPage
import pytest

from Pages.log_in_page import LoginPage


class TestCatalog():

		def test_add_element_to_card(self , init_parameters):
				self.LoginPage = LoginPage(self.driver)
				self.LoginPage.login('standard_user' , 'secret_sauce')
				self.CatalogPage = CatalogPage(self.driver)
				self.CatalogPage.add_random_element_to_card()
