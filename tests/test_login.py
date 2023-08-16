from test_utils import *
from pages.index_page import IndexPage
from pages.register_success_page import RegisterSuccessPage
from resources.constants import TEST_SITE_URL
from pages.register_page import RegisterPage


class TestLogin:

    def test_register_new_user(self, driver, username_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_register_button()
        register_page = RegisterPage(driver)
        register_page.wait_and_type_user_name(username_password)
        register_page.type_password(username_password)
        register_page.type_confirm_password(username_password)
        register_page.click_submit_btn()
        register_success_page = RegisterSuccessPage(driver)
        register_success_lbl = register_success_page.get_register_success_label()
        assert register_success_lbl.__contains__(username_password[0]), "User registration failed!"

    def test_register_new_user_with_invalid_confirm_password(self, driver, username_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_register_button()
        register_page = RegisterPage(driver)
        register_page.wait_and_type_user_name(username_password)
        register_page.type_password(username_password)
        register_page.type_confirm_password("invalid")
        register_page.click_submit_btn()
        register_success_page = RegisterSuccessPage(driver)
        register_success_lbl = register_success_page.get_register_success_label()
        assert not register_success_lbl.__contains__(username_password[0]), "User registration failed!"
