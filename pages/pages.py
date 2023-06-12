import logging

import pytest
from playwright.sync_api import Page

from data.users import Users
from data.locators import (
    MainPageLocators,
    SignInPageLocators,
    RegistrationPageLocators,
    ReptileCategoryPageLocators,
)
logger = logging.getLogger(__name__)


class MainPage:
    def __init__(self, page: Page):
        self.locators = MainPageLocators
        self.page = page

    def navigate_to_sign_in_page_by_header_menu(self):
        self.page.click(self.locators.SIGN_IN_BUTTON)

    def navigate_to_shopping_cart_page_by_header_menu(self):
        self.page.click(self.locators.SHOPPING_CART_BUTTON)

    def navigate_to_reptile_category_by_sidebar_menu(self):
        self.page.click(self.locators.REPTILES_CATEGORY_IN_SIDEBAR_MENU)

    def check_sidebar_is_present(self):
        self.page.wait_for_url(self.locators.MAIN_PAGE_URL)
        return self.page.is_visible(self.locators.SIDEBAR_MENU)

    def check_user_is_login(self) -> str:
        self.page.wait_for_url(self.locators.MAIN_PAGE_URL)
        welcome_text = self.page.inner_text(self.locators.WELCOME_MESSAGE)
        name = welcome_text.removeprefix("Welcome ").removesuffix("!")
        logger.info("NAME: %s", name)
        return name


class SignInPage:
    def __init__(self, page: Page):
        self.locators = SignInPageLocators
        self.page = page

    def input_text_to_username_field(self, username: str):
        self.page.fill(self.locators.USERNAME_INPUT, username)

    def input_text_to_password_field(self, password: str):
        self.page.fill(self.locators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.page.click(self.locators.LOGIN_BUTTON)

    def check_login_button_is_visible(self):
        return self.page.is_visible(self.locators.LOGIN_BUTTON)

    def navigate_to_register_page_by_link(self):
        self.page.click(self.locators.REGISTER_BUTTON)

    def sign_on_failed_message_is_visible(self):
        return self.page.is_visible(self.locators.SIGN_ON_FAILED_MESSAGE)

    def login(self, username: str, password: str):
        """
        Provide sign in user.
        :param username:
        :param password:
        """
        logger.info("USERNAME: %s | PASSWORD: %s", username, password)

        self.input_text_to_username_field(username)
        self.input_text_to_password_field(password)
        self.click_login_button()


class RegistrationPage:
    def __init__(self, page: Page):
        self.locators = RegistrationPageLocators
        self.page = page

    # User Information

    def input_text_to_user_id_field(self, user_id: str):
        self.page.fill(self.locators.USER_ID, user_id)

    def input_text_to_new_password_field(self, new_password: str):
        self.page.fill(self.locators.NEW_PASSWORD, new_password)

    def input_text_to_repeat_password_field(self, repeat_password: str):
        self.page.fill(self.locators.REPEAT_PASSWORD, repeat_password)

    # Account Information

    def input_text_to_first_name_field(self, first_name: str):
        self.page.fill(self.locators.FIRST_NAME, first_name)

    def input_text_to_last_name_field(self, last_name: str):
        self.page.fill(self.locators.LAST_NAME, last_name)

    def input_text_to_email_field(self, email: str):
        self.page.fill(self.locators.EMAIL, email)

    def input_text_to_phone_field(self, phone: str):
        self.page.fill(self.locators.PHONE, phone)

    def input_text_to_address1_field(self, address1: str):
        self.page.fill(self.locators.ADDRESS_1, address1)

    def input_text_to_address2_field(self, address2: str):
        self.page.fill(self.locators.ADDRESS_2, address2)

    def input_text_to_city_field(self, city: str):
        self.page.fill(self.locators.CITY, city)

    def input_text_to_state_field(self, state: str):
        self.page.fill(self.locators.STATE, state)

    def input_text_to_zip_field(self, zip_code: str):
        self.page.fill(self.locators.ZIP, zip_code)

    def input_text_to_country_field(self, country: str):
        self.page.fill(self.locators.COUNTRY, country)

    # Profile Information

    def select_language(self, value: str):
        """
        Need to choose Language from the given list.
        :param value: "english", "japanese"
        """
        self.page.select_option(self.locators.LANGUAGE_PREFERENCE, value=value)

    def select_favourite_category(self, value: str):
        """
        Need to choose Favourite Category from the given list.
        :param value: "FISH", "DOGS", "REPTILES", "CATS", "BIRDS"
        """
        self.page.select_option(self.locators.FAVOURITE_CATEGORY, value=value)

    def select_my_list(self):
        self.page.click(self.locators.MY_LIST)

    def select_my_banner(self):
        self.page.click(self.locators.MY_BANNER)

    def send_new_user_information(self):
        self.page.click(self.locators.SAVE_ACCOUNT_INFORMATION_BUTTON)

    def filling_in_registration_form(self, user_id: None):
        rand_user_id = Users().user_id()
        user = Users().account_info()

        if user_id is None:
            user_id = rand_user_id
        else:
            user_id = user_id

        logger.info("Using USER_ID: %s", user_id)

    # User Information

        self.input_text_to_user_id_field(user_id)
        self.input_text_to_new_password_field(user_id)
        self.input_text_to_repeat_password_field(user_id)

    # Account Information

        self.input_text_to_first_name_field(user_id)
        self.input_text_to_last_name_field(user["last_name"])
        self.input_text_to_email_field(user["email"])
        self.input_text_to_phone_field(user["phone"])
        self.input_text_to_address1_field(user["address1"])
        self.input_text_to_address2_field(user["address2"])
        self.input_text_to_city_field(user["city"])
        self.input_text_to_state_field(user["state"])
        self.input_text_to_zip_field(user["zip_code"])
        self.input_text_to_country_field(user["country"])

    # Profile Information

        self.select_language("english")
        self.select_favourite_category("REPTILES")
        self.select_my_list()
        self.select_my_banner()


class ReptileCategoryPage:
    def __init__(self, page: Page):
        self.locators = ReptileCategoryPageLocators
        self.page = page

    def navigate_to_product_page(self):
        self.page.click()