import pytest

from src.steps.registration_steps import *


# @pytest.fixture(scope='session')
@pytest.fixture(scope='module')
def driver():
    """Pre-setup steps that can be passed to another function"""
    print(" ############### This is the SetUP steps ##################")
    driver = initialize_browser('chrome')

    yield driver
    print(" ############### This is the TearDown steps ##################")
    close_browser(driver)
