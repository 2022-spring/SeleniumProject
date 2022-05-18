from src.pages.base_page import BasePage


class AuthenticationPage(BasePage):
    # locator
    email_addr_id = 'email_create'
    create_an_account_btn_id = 'SubmitCreate'

    # methods
    def enter_signup_email(self, email):
        print(f"entering the email address ...")
        self.enter_text_by_id(self.email_addr_id, email)
        print(f"email entered")

    def click_create_account_button(self):
        print(f"printing create an account button..")
        self.click_element_by_id(self.create_an_account_btn_id)
