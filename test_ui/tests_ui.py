import pytest
from time import sleep
from data.users import Users


class TestsRegistrationPage:

    def test_create_new_user_with_valid_data(self, driver):
        m = driver.main_page
        s = driver.sign_in_page
        r = driver.registration_page

        m.navigate_to_sign_in_page_by_header_menu()
        s.navigate_to_register_page_by_link()
        r.filling_in_registration_form()
        r.send_new_user_information()

        assert m.check_sidebar_is_present() is True


class TestsSignInPage:

    ddt = {
        "argnames": "username, password",
        "argvalues": [
            ("Invalid", Users().static_user),
            (Users().static_user, "Invalid"),
            ("", Users().static_user),
            (Users().static_user, ""),
            ("", "")
        ],
        "ids": ["Invalid Username and Valid Password",
                "Valid Username and Invalid Password",
                "Blank Username field and Filled Password field",
                "Filled Username field and Blank Password field",
                "Blank Username and Password fields"
                ]
    }

    def test_login_user_with_valid_data(self, driver):
        m = driver.main_page
        s = driver.sign_in_page
        r = driver.registration_page
        user = Users().static_user

        m.navigate_to_sign_in_page_by_header_menu()
        s.login(user, user)
        if s.sign_on_failed_message_is_visible() is True:
            s.navigate_to_register_page_by_link()
            r.filling_in_registration_form(user)
            r.send_new_user_information()
            m.navigate_to_sign_in_page_by_header_menu()
            s.login(user, user)

        assert m.check_user_is_login() == user  # 'Jessica'

    @pytest.mark.parametrize(**ddt)
    def test_login_user_with_invalid_data(self, driver, username, password):
        m = driver.main_page
        s = driver.sign_in_page

        m.navigate_to_sign_in_page_by_header_menu()
        s.login(username, password)
        assert s.check_login_button_is_visible() is True

    # def test_user(self):
    #     user = Users().account_info()
    #     np = str(user)
    #     print("first_name: " + np)


class TestsOrder:

    def test_add_item_to_shopping_cart(self, driver):
        m = driver.main_page
        rc = driver.reptile_category_page
        p = driver.products_page
        s = driver.shopping_cart_page

        m.navigate_to_reptile_category_by_sidebar_menu()
        rc.navigate_to_product_page_by_name("Iguana")
        p.add_first_item_on_products_page()
        assert s.check_remove_button_is_visible() is True

    def test_change_item_quantity_in_shopping_cart(self, driver):
        s = driver.shopping_cart_page

        s.add_item_to_shopping_cart("Iguana")

        total_coast = s.get_total_coast()

        s.change_quantity(2)
        s.click_update_cart()

        updated_total_coast = s.get_total_coast()

        assert total_coast != updated_total_coast

    def test_delete_item_from_shopping_cart(self, driver):
        s = driver.shopping_cart_page

        s.add_item_to_shopping_cart("Iguana")
        s.click_remove_button()

        assert s.check_remove_button_is_visible() is False

    def test_checkout_an_order_from_the_shopping_cart(self, driver):
        sc = driver.shopping_cart_page
        s = driver.sign_in_page
        no = driver.new_order_form_page
        o = driver.order_form_page
        co = driver.confirmed_order_form_page

        s.login_by_static_user()
        sc.add_item_to_shopping_cart("Iguana")
        sc.click_proceed_to_checkout_button()
        no.click_continue_button()
        o.click_confirm_button()

        assert co.check_order_header_is_visible() is True
