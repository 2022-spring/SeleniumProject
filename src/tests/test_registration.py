from src.steps.registration_steps import *
from src.utilities import *
import pytest

# VARIABLE
# data = load_yaml_file(f"../../data/config.yml")
data = load_yaml_file(f"{ROOT_DIR}/data/config.yml")

url = data['url']
first_name = data['first_name']
last_name = data['last_name']
password = data['password']
email = f"jdoe{get_timestamp()}@mail.com"


# SCENARIO

@pytest.mark.smoke
@pytest.mark.regression
def test_registration_scenario1():
    print("# test case steps here")
    driver = initialize_browser('chrome')
    open_website(driver, url)
    # open_registration_form(driver, email)
    # complete_registration_form(driver, first_name, last_name, password, email)
    #
    # print("verify 'controller=order' in the url")
    # is_keyword_in_url(driver, 'controller=order')
    close_browser(driver)


def test_regression_scenario2():
    print("This is the regression scenario 2 ##############")
