import time

from src.pages.base_page import BasePage


class MainPage(BasePage):
    # locator
    __signin_btn_xpath = '//a[@class="login"]'
    __search_box_id = 'search_query_top'
    __search_btn_name = 'submit_search'
    __cart_link_xpath = '//a[@title="View my shopping cart"]'

    # methods
    def click_signin(self):
        """clicks sign in link on the top menu."""
        print(f"Clicking the sign in button...")
        self.click_element_by_xpath(self.__signin_btn_xpath)
        time.sleep(2)

    def enter_text_in_search(self, phrase):
        print(f"entering '{phrase}' in the search box..")
        self.enter_text_by_id(self.__search_box_id, phrase)

    def click_search_btn(self):
        print(f"clicking the search button")
        self.click_element_by_name(self.__search_btn_name)

