import pytest


from Pages.log_in_page import LoginPage
from locators.login_page import *


class Test_Auth():

		def __init__(self, driver):
				super().__init__(driver)


		@pytest.mark.parametrize("username, password" , [('standard_user' , 'secret_sauce')])
		def test_valid_data_auth(self , init_parameters , username , password):
				self.LoginPage = LoginPage(self.driver)
				self.LoginPage.login(username , password)
				# self.LoginPage.check_presence_of_an_element(catalog_block)

		@pytest.mark.parametrize("username, password" , [('locked_out_user' , 'secret_sauce')])
		def test_blocked_data_auth(self , init_parameters , username , password):
				self.LoginPage = LoginPage(self.driver)
				self.LoginPage.login(username , password)
				self.LoginPage.check_presence_of_an_element(blocked_user_message)
				assert self.LoginPage.get_element_text(
						self.LoginPage.ASSERTION_MESSAGES) == "Epic sadface: Sorry, this user has been locked out."

		@pytest.mark.parametrize("username, password" , [('' , 'secret_sauce')])
		def test_empty_login_auth(self , init_parameters , username , password):
				self.LoginPage = LoginPage(self.driver)
				self.LoginPage.login(username , password)
				self.LoginPage.check_presence_of_an_element(empty_login_filed_message)
				assert self.LoginPage.get_element_text(
						self.LoginPage.ASSERTION_MESSAGES) == "Epic sadface: Username is required"

		@pytest.mark.parametrize("username, password" , [('Text' , '')])
		def test_empty_password_auth(self , init_parameters , username , password):
				self.LoginPage = LoginPage(self.driver)
				self.LoginPage.login(username , password)
				self.LoginPage.check_presence_of_an_element(empty_password_filed_message)
				assert self.LoginPage.get_element_text(
						self.LoginPage.ASSERTION_MESSAGES) == "Epic sadface: Password is required"
