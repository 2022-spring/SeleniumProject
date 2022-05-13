from WElement.webelement_class import *

# driver = initialize_chrome()
driver = initialize_firefox()
# webelement_properties(driver)
# webelement_methods(driver)
test_explicit_wait(driver)
close_browser(driver)
