import logging
import re

import pytest
from playwright.sync_api import Page

from data.users import Users
from data.locators import (
    MainPageLocators,
    SignInPageLocators,
    RegistrationPageLocators,
    ReptileCategoryPageLocators,
    ProductsPageLocators,
    ShoppingCartPageLocators,
    NewOrderFormPageLocators,
    OrderFormPageLocators,
    ConfirmedOrderFormPageLocators,
    MyAccountPageLocators,
    MyOrdersPageLocators
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

    def navigate_to_my_account_page_by_header_menu(self):
        self.page.click(self.locators.MY_ACCOUNT_BUTTON)

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

    def login_by_static_user(self):
        m = MainPage(self.page)
        r = RegistrationPage(self.page)
        user = Users().static_user

        m.navigate_to_sign_in_page_by_header_menu()
        self.login(user, user)
        if self.sign_on_failed_message_is_visible() is True:
            self.navigate_to_register_page_by_link()
            r.filling_in_registration_form(user)
            r.send_new_user_information()
            m.navigate_to_sign_in_page_by_header_menu()
            self.login(user, user)


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

    def navigate_to_product_page_by_name(self, product_name: str):
        self.page.click(self.locators.product_item_by_name(product_name))


class ProductsPage:
    def __init__(self, page: Page):
        self.locators = ProductsPageLocators
        self.page = page

    def add_first_item_on_products_page(self):
        self.page.click(self.locators.FIRST_PRODUCT_ADD_TO_CART_BUTTON)


class ShoppingCartPage:
    def __init__(self, page: Page):
        self.locators = ShoppingCartPageLocators
        self.page = page

    def check_remove_button_is_visible(self):
        return self.page.is_visible(self.locators.REMOVE_BUTTON)

    def click_remove_button(self):
        self.page.click(self.locators.REMOVE_BUTTON)

    def add_item_to_shopping_cart(self, product_name: str):
        m = MainPage(self.page)
        rc = ReptileCategoryPage(self.page)
        p = ProductsPage(self.page)

        m.navigate_to_reptile_category_by_sidebar_menu()
        rc.navigate_to_product_page_by_name(product_name)
        p.add_first_item_on_products_page()

    def change_quantity(self, number: int):
        self.page.fill(self.locators.INPUT_QUANTITY, str(number))

    def get_list_price(self) -> str:
        value = self.page.inner_text(self.locators.LIST_PRICE)
        logger.info("LIST_PRICE: %s", value)
        return value

    def get_total_coast(self) -> str:
        value = self.page.inner_text(self.locators.TOTAL_COAST)
        logger.info("TOTAL_COAST: %s", value)
        return value

    def click_update_cart(self):
        self.page.click(self.locators.UPDATE_CART_BUTTON)

    def click_proceed_to_checkout_button(self):
        self.page.click(self.locators.PROCEED_TO_CHECKOUT_BUTTON)

    def create_new_order(self):
        si = SignInPage(self.page)
        sc = ShoppingCartPage(self.page)
        no = NewOrderFormPage(self.page)
        o = OrderFormPage(self.page)
        co = ConfirmedOrderFormPage(self.page)

        si.login_by_static_user()
        sc.add_item_to_shopping_cart("Iguana")
        sc.click_proceed_to_checkout_button()
        no.click_continue_button()
        o.click_confirm_button()


class NewOrderFormPage:
    def __init__(self, page: Page):
        self.locators = NewOrderFormPageLocators
        self.page = page

    def click_continue_button(self):
        self.page.click(self.locators.CONTINUE_BUTTON)


class OrderFormPage:
    def __init__(self, page: Page):
        self.locators = OrderFormPageLocators
        self.page = page

    def click_confirm_button(self):
        self.page.click(self.locators.CONFIRM_BUTTON)


class ConfirmedOrderFormPage:
    def __init__(self, page: Page):
        self.locators = ConfirmedOrderFormPageLocators
        self.page = page

    def check_order_header_is_visible(self):
        return self.page.is_visible(self.locators.ORDER_HEADER)

    def get_order_number(self) -> str:
        order_header = self.page.inner_text(self.locators.ORDER_HEADER)
        order_number = order_header.removeprefix("Order #")[:-20]
        logger.info("ORDER_HEADER: %s", order_header)
        logger.info("ORDER_NUMBER: %s", order_number)
        return order_number


class MyAccountPage:
    def __init__(self, page: Page):
        self.locators = MyAccountPageLocators
        self.page = page

    def navigate_to_my_orders_page_by_header_menu(self):
        self.page.click(self.locators.MY_ORDERS_BUTTON)


class MyOrdersPage:
    def __init__(self, page: Page):
        self.locators = MyOrdersPageLocators
        self.page = page

    def search_order_number_in_orders_list(self, order_number: str):
        order_id_list = []
        order_ids = self.page.query_selector_all(self.locators.ORDER_ID)
        for i in order_ids:
            order_id_list.append(i.inner_text())

        result = any(order_number in order_id_list for order_number in order_id_list)
        logger.info("ORDER_ID_LIST: %s", order_id_list)
        logger.info("Is ORDER_NUMBER in ORDER_ID_LIST: %s", result)
        return result
