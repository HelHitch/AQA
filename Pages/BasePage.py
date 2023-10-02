import random
from selenium.common import TimeoutException, InvalidArgumentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        try:
            page = self.driver.get(url)
            return page
        except InvalidArgumentException:
            raise InvalidArgumentException('Failed getting page by URL')

    def click(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        except TimeoutException:
            raise TimeoutException(f'Failed to click {by_locator} element')

    def click_random_element_from_list(self, by_locator):
        try:
            elem = WebDriverWait(self.driver, 5).until(EC.visibility_of_any_elements_located(by_locator))
            random_element = random.randint(0, len(elem) - 1)
            random_element = elem[int(random_element)]
            random_element.click()
        except TimeoutException:
            raise TimeoutException('Element for clicking not found')

    def send_keys(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except TimeoutException:
            raise TimeoutException('Element for inserting data not found')


    def get_element_text(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element.text
        except TimeoutException:
            raise TimeoutException('Failed getting element text')

    def element_is_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element
        except TimeoutException:
            raise TimeoutException('Failed getting searched element')


