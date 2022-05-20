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
# @pytest.fixture
# def driver():
#     """Pre-setup steps that can be passed to another function"""
#     return initialize_browser('chrome')


@pytest.mark.smoke
@pytest.mark.regression
def test_registration_scenario1(driver):
    print("# test case steps here")
    open_website(driver, url)
    # open_registration_form(driver, email)
    # complete_registration_form(driver, first_name, last_name, password, email)
    #
    # print("verify 'controller=order' in the url")
    # is_keyword_in_url(driver, 'controller=order')


def test_regression_scenario2(driver):
    print("This is the regression scenario 2 ##############")
