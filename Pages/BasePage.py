import random

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
		def __init__(self , driver, url):
				self.driver = driver
				self.url = url

		def open_page(self):
				page = self.driver.get(self.url)
				return page

		def click(self , by_locator):
				WebDriverWait(self.driver , 10).until(EC.visibility_of_element_located(by_locator)).click()

		def click_random_element_from_list(self , by_locator):
				print('B')
				elements = self.driver.find_element(by_locator).click()
				print('A')
				# element = random.choice(elements)
				return elements

		def send_keys(self , by_locator , text):
				WebDriverWait(self.driver , 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

		def get_element_text(self , by_locator):
				element = WebDriverWait(self.driver , 10).until(EC.visibility_of_element_located(by_locator))
				print(element.text)
				return element.text

		def get_random_element_text(self , by_locator):
				element = WebDriverWait(self.driver , 10).until(EC.visibility_of_elements_located(by_locator))
				print(element.text)
				return element.text

		def check_presence_of_an_element(self , by_locator):
				element = WebDriverWait(self.driver , 10).until(EC.visibility_of_element_located(by_locator))
				return element


