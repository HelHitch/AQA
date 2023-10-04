#!/usr/bin/env python3
# -- coding: utf-8 --
import pytest
from selenium import webdriver
from Pages.log_in import LoginPage
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager




"""Launch setup parameters"""
@pytest.fixture()
def browser(request):
		return request.config.getoption("--browser")

@pytest.fixture()
def headless(request):
		return request.config.getoption("--headless")


@pytest.fixture()
def init_parameters(browser, headless):
		if headless == "true":
				if browser == "chrome":
						options = webdriver.ChromeOptions()
						options.add_argument("--headless=new")
						driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()) , options = options)
				elif browser == "firefox":
						options = webdriver.FirefoxOptions()
						options.add_argument("--headless")
						driver = webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()) , options = options)

		if headless == "false":
				if browser == "chrome":
						driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
				elif browser == "firefox":
						driver = webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()))

		yield driver
		driver.close()
		driver.quit()



def pytest_addoption(parser):
		parser.addoption("--browser")
		parser.addoption("--headless")


@pytest.fixture()
def completed_auth(init_parameters, headless):
		yield LoginPage(init_parameters).login(username = 'standard_user' , password = 'secret_sauce')
