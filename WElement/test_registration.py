from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select

# VARIABLE

url = "http://automationpractice.com"
email = f"jdoe{time.strftime('%Y%m%d%H%M%S')}@mail.com"
first_name = 'John'
last_name = 'Doe'
password = '123456'

print("# test case steps here")
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)  # max wait time for all find element steps

print("Browser initialized. Opening the website ...")
driver.get(url)

driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign in').click()
time.sleep(2)
print("Verify 'authentication' is in the url")
assert 'authentication' in driver.current_url, "Authentication page verification Failed"

print("enter email in the Create and Account box")
# email = 'jdoe20220510828123@mail.com'
print(f"email to register: '{email}'")
driver.find_element(By.ID, 'email_create').send_keys(email)
time.sleep(1)
print("Click 'Create an account' button")
driver.find_element(By.ID, 'SubmitCreate').click()
time.sleep(5)

print("verify 'account-creation' in the current url")
assert 'account-creation' in driver.current_url, "Account creation page verification Failed"

print("Filling form: ")
print("select 'Mr' radio button")
mr_title = driver.find_element(By.ID, 'id_gender1')
mr_title.click()
time.sleep(1)
print("MR is selected or not? ", mr_title.is_selected())
assert mr_title.is_selected(), 'Title MR was not selected'

print("Enter first name: John")
driver.find_element(By.ID, 'customer_firstname').send_keys(first_name)
print("enter last name: Doe")
driver.find_element(By.ID, 'customer_lastname').send_keys(last_name)

print("Enter the email or click to confirm")
driver.find_element(By.ID, 'email').click()

# email = driver.find_element(By.ID, 'email')
# email.clear()
# email.send_keys(email)

print("enter password '12345'")
driver.find_element(By.ID, 'passwd').send_keys(password)

print("select Day '10'")  # drop down
drop_down = driver.find_element(By.ID, 'days')  # find element with Select tagname
selection = Select(drop_down)
selection.select_by_value('10')

print("Select month 'December'")  # drop down
selection = Select(driver.find_element(By.ID, 'months'))  # find element with Select tagname
selection.select_by_value('12')

print("select year '2000'")  # drop down
selection = Select(driver.find_element(By.ID, 'years'))  # find element with Select tagname
selection.select_by_visible_text('2000  ')

print("Check 'Sign up for our newsletter' checkbox")
signup_checkbox = driver.find_element(By.ID, 'newsletter')
signup_checkbox.click()
time.sleep(2)
assert signup_checkbox.is_selected(), "Sign up to newsletter checkbox verification Failed"

print("enter address: 123 Address st")
driver.find_element(By.ID, 'address1').send_keys('123 Address st')

# print("enter city: Brooklyn")
# driver.find_element(By.ID, '').send_keys('Brooklyn')

print("Select state: New York")
# drop down
selection = Select(driver.find_element(By.ID, 'id_state'))  # find element with Select tagname
print("selection.first_selected_option: ", selection.first_selected_option)
selection.select_by_visible_text('New York')


# print("enter zip code: 11224")
# driver.find_element(By.ID, '')

print("select country : first country")
# drop down
selection = Select(driver.find_element(By.ID, 'id_country'))  # find element with Select tagname
selection.select_by_index(1)  # index: '-' is 0, and 'United States' option is index 1

# print("enter mobile number: '1234567894'")
# driver.find_element(By.ID, '').send_keys('1234567897')

# print("enter address alias name: 'primary'")
# driver.find_element(By.ID, '').send_keys('primary')
#
# print("Click Register button ")
# driver.find_element(By.ID, '').click()
#
# print("verify 'controller=order' in the url")
# assert 'controller=order' in driver.current_url, "Order page verification Failed"

print("# closing the whole browser")
time.sleep(10)
driver.quit()

# hw: fill the undefined IDs in the commented steps and run to get registered.
# forms: text box, checkbox, radio button, drop down (object Select class, by value/visible text/index)
