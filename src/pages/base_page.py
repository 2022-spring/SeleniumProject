from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from src.utilities import *

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wdwait = WebDriverWait(driver, 10)

    def click_element_by_id(self, id):
        try:
            # element = self.driver.find_element(By.ID, id)
            element = self.wdwait.until(EC.element_to_be_clickable((By.ID, id)))
            element.click()
        except (NoSuchElementException, TimeoutException) as err:
            print(f"Error in click element by id, please check id='{id}'")
            print(f"Error message: {err}")

    def click_element_by_xpath(self, xpath):
        try:
            self.wdwait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except (NoSuchElementException, TimeoutException) as err:
            print(f"Error in click element by id, please check id='{xpath}'")
            print(f"Error message: {err}")

    def click_element_by_name(self, name):
        try:
            self.wdwait.until(EC.element_to_be_clickable((By.NAME, name))).click()
        except (NoSuchElementException, TimeoutException) as err:
            print(f"Error in click element by id, please check id='{name}'")
            print(f"Error message: {err}")

    def enter_text_by_id(self, id, text):
        try:
            element = self.wdwait.until(EC.presence_of_element_located((By.ID, id)))
            element.clear()
            element.send_keys(text)
        except (NoSuchElementException, TimeoutException) as err:
            print(f"Error in entering the text by id, please check id='{id}'")
            print(f"Error message: {err}")

    def select_from_dropdown_by_id_by_index(self, id, index_value):
        try:
            element = self.wdwait.until(EC.presence_of_element_located((By.ID, id)))
            selection = Select(element)  # find element with Select tagname
            selection.select_by_index(1)  # index: '-' is 0, and 'United States' option is index 1

        except (NoSuchElementException, TimeoutException) as err:
            print(f"Error in select from drop down, please check id='{id}' and index='{index_value}'")
            print(f"Error message: {err}")

    def is_element_selected_by_id(self, id):
        element = self.wdwait.until(EC.presence_of_element_located((By.ID, id)))
        return element.is_selected()

    def is_element_displayed_by_id(self, id):
        element = self.driver.find_element(By.ID, id)
        return element.is_displayed()
