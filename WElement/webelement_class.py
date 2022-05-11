#   Chapter 4: Webelement properties and methods

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def initialize_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)  # max wait time for all find element steps
    return driver


def webelement_properties(driver):
    # driver.get("https://demoqa.com/browser-windows")
    driver.get("http://automationpractice.com")

    print("# finding the multiple element")
    product_names = driver.find_elements(By.XPATH, "//a[@class='product-name']")
    # print(cart_buttons)
    time.sleep(1)

    print(" Using the webelement properties for each element..")
    for prod_name in product_names:
        print("cart_button.text: ", prod_name.text)
        print("cart_button.size: ", prod_name.size)
        print("cart_button.tag_name: ", prod_name.tag_name)
    print("---------------------------------")
    print("number of elements found: ", len(product_names))


def close_browser(driver):
    print("# closing the whole browser")
    time.sleep(3)
    driver.quit()


def webelement_methods(driver):
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.implicitly_wait(20)  # max wait time for all find element steps

    # open website
    driver.get("http://automationpractice.com")

    # enter 'selenium' in the search box, wait 5 sec,
    search_box = driver.find_element(By.ID, 'search_query_top')
    search_box.send_keys('selenium')
    # search_box.send_keys('selenium' + Keys.ENTER)
    time.sleep(5)
    # clear the search box and enter 'dress'
    search_box.clear()
    search_box.send_keys('dress')

    # click search button
    # driver.find_element(By.NAME, 'submit_search').click()
    search_button = driver.find_element(By.NAME, 'submit_search')
    search_button.click()

    # verify compare button is displayed
    compare_btn = driver.find_element(By.XPATH, '//form[@class="compare-form"]')
    print("compare_btn.is_displayed(): ", compare_btn.is_displayed())
    # assert compare_btn.is_displayed()

    # verify compare button is not enabled
    print("compare_btn.is_enabled(): ", compare_btn.is_enabled())

    # get attribute 'action' of compare
    print("Action attribute of compare form: ", compare_btn.get_attribute('action'))


def working_with_alerts(driver):
    print("## Switching to Alert")
    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.ID, "promtButton").click()
    alrt = driver.switch_to.alert
    time.sleep(2)
    print("## Clicking the OK...")
    alrt.accept()  # clicking OK button

    print("## Clicking the cancel...")
    time.sleep(2)
    driver.find_element(By.ID, "promtButton").click()
    alrt = driver.switch_to.alert
    alrt.dismiss()  # clicking the Cancel button

    print("## Entering the text in Alert...")
    time.sleep(2)
    driver.find_element(By.ID, "promtButton").click()
    alrt = driver.switch_to.alert
    alrt.send_keys("john doe")  # clicking the Cancel button
    alrt.accept()
    time.sleep(2)
