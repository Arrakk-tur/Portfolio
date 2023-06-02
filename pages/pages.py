from playwright.sync_api import Page
from data.locators import (
    HeaderLocators,
    SignInPageLocators,
    RegistrationPageLocators,
)


class Header:
    def __init__(self, page: Page):
        self.locators = HeaderLocators
        self.page = page

    def navigate_to_sign_in_page_by_header_menu(self):
        self.page.click(self.locators.SIGN_IN_BUTTON)

    def navigate_to_shopping_cart_page_by_header_menu(self):
        self.page.click(self.locators.SHOPPING_CART_BUTTON)


class SignInPage:
    def __init__(self, page: Page):
        self.locators = SignInPageLocators
        self.page = page

    def input_text_to_username_field(self, username: str):
        self.page.fill(self.locators.USERNAME_INPUT, username)

    def input_text_to_password_field(self, password: str):
        self.page.fill(self.locators.PASSWORD_INPUT, password)

    def navigate_to_register_page_by_link(self):
        self.page.click(self.locators.REGISTER_BUTTON)


class RegistrationPage:
    def __init__(self, page: Page):
        self.locators = RegistrationPageLocators
        self.page = page

    # User Information

    def input_text_to_user_id_field(self, user_id: str):
        self.page.fill(self.locators.USER_ID, user_id)

# TODO: Finish form
