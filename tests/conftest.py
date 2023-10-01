#!/usr/bin/env python3
# -- coding: utf-8 --
import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def init_parameters(request):
    web_driver = webdriver.Chrome()
    yield web_driver
    web_driver.close()
