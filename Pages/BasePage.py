import dataclasses
import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        page = self.driver.get(url)
        return page

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def click_random_element_from_list(self, by_locator):
        elem = WebDriverWait(self.driver, 5).until(EC.visibility_of_any_elements_located(by_locator))
        random_element = random.randint(1, len(elem))
        random_element = elem[int(random_element)]
        random_element.click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_random_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_elements_located(by_locator))
        print(element.text)
        return element.text

    def element_is_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element
        except TimeoutException:
            raise AssertionError('Element not found')


