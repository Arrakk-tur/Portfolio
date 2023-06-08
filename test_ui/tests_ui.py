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

        assert m.check_sidebar_is_present() == True


class TestsSignInPage:

    def test_login_user_with_valid_data(self, driver):
        m = driver.main_page
        s = driver.sign_in_page
        r = driver.registration_page
        user = Users().static_user

        m.navigate_to_sign_in_page_by_header_menu()
        try:
            s.login(user, user)
            if s.sign_on_failed_message_is_visible() is True:
                s.navigate_to_register_page_by_link()
                r.filling_in_registration_form(user)
                r.send_new_user_information()
        finally:
            # TODO: fix it
            # s.login(user, user)
            assert m.check_user_is_login() == user  # 'Jessica'

    def test_user(self):
        user = Users().account_info()
        np = str(user)
        print("first_name: " + np)
