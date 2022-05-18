from src.pages.base_page import BasePage


class MainPage(BasePage):
    # locator
    signin_btn_xpath = '//a[@class="login"]'
    search_box_id = 'search_query_top'
    search_btn_name = 'submit_search'
    cart_link_xpath = '//a[@title="View my shopping cart"]'

    # methods
    def click_signin(self):
        """clicks sign in link on the top menu."""
        print(f"Clicking the sign in button...")
        self.click_element_by_xpath(self.signin_btn_xpath)

    def enter_text_in_search(self, phrase):
        print(f"entering '{phrase}' in the search box..")
        self.enter_text_by_id(self.search_box_id, phrase)

    def click_search_btn(self):
        print(f"clicking the search button")
        self.click_element_by_name(self.search_btn_name)

