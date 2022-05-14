#   Chapter 4: Webelement properties and methods

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def initialize_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)  # max wait time for all find element steps
    return driver


def initialize_firefox():
    driver = webdriver.Firefox()
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


def test_explicit_wait(driver):
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.implicitly_wait(20)  # max wait time for all find element steps

    # time object from WebDriverWait()
    # you need list of conditions from expected_conditions() class

    url = "https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver"
    wdwait = WebDriverWait(driver, 30)  # step 1

    print("########   test explicit wait started ##############")
    print("########   text_to_be_present_in_element ##############")
    print("# open the website")
    driver.get(url)

    print("# get the initial text")
    # option 1
    # original_msg = driver.find_element(By.ID, 'h2').text
    # option 2
    original_msg = wdwait.until(EC.presence_of_element_located((By.ID, 'h2'))).text
    print(f"Original message displayed: {original_msg}")

    print('# click on "Change Text to Selenium Webdriver" button')
    driver.find_element(By.ID, 'populate-text').click()

    print("# wait until text is present in the element 'Selenium', max wait time is 20")
    wdwait.until(EC.text_to_be_present_in_element((By.ID, "h2"), "Selenium"))  # step2
    target_msg = driver.find_element(By.ID, 'h2').text

    print(f"Target text : {target_msg}")
    print("######## text_to_be_present_in_element completed ########### ")

    print("########## element_to_be_clickable started ############")
    driver.find_element(By.ID, 'disable').click()

    print("check if button is enabled if not click on 'Enable button after 10 seconds'")
    print(f"checking the button : {driver.find_element(By.ID, 'disable').is_enabled()}")

    if not driver.find_element(By.ID, 'disable').is_enabled():
        driver.find_element(By.ID, 'enable-button').click()

    print("wait until 'Button' button is enabled, then click the button")
    wdwait.until(EC.element_to_be_clickable((By.ID, 'disable')))
    driver.find_element(By.ID, 'disable').click()
    print("######## element_to_be_clickable completed ########### ")


def test_drag_and_drop(driver):
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.implicitly_wait(20)  # max wait time for all find element steps

    print("############# test_drag_and_drop started ###########")
    url = 'https://jqueryui.com/droppable/'
    wdwait = WebDriverWait(driver, 10)

    print("# open the website")
    driver.get(url)
    # time.sleep(2)
    wdwait.until(EC.presence_of_element_located((By.ID, 'content')))

    print("# find draggable element")
    driver.switch_to.frame(0)  # option 1
    # driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")) # option 2
    element1 = driver.find_element(By.ID, 'draggable')

    print("# find droppable box where we need to drop first element")
    # element2 = driver.find_element(value='droppable')  # option 1
    element2 = wdwait.until(EC.presence_of_element_located((By.ID, 'droppable')))  # option 2

    print("# check the text before the action")
    print(f"Text in target element: '{element2.text}'")

    print("# perform drag and drop action on above elements")
    actions = ActionChains(driver)
    # option 1
    # actions.drag_and_drop(element1, element2).perform()
    # option 2
    actions.click_and_hold(element1).perform()
    actions.release(element2).perform()

    print("# check the text after the action")
    print(f"Text in target element: '{element2.text}'")
    assert 'Dropped' in element2.text, "Drag and drop action failed."
    print("######## test_drag_and_drop completed ################")


def test_hover_over_action(driver):
    pass
