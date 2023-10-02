#!/usr/bin/env python3
# -- coding: utf-8 --
import pytest
from selenium import webdriver
from Pages.log_in import LoginPage

@pytest.fixture(scope='class')
def init_parameters():
    web_driver = webdriver.Chrome()
    yield web_driver
    web_driver.close()


@pytest.fixture(scope='class')
def completed_auth(init_parameters):
    CatalogPage = LoginPage(init_parameters)
    yield CatalogPage.login(username='standard_user', password='secret_sauce')

