import time

import pytest

from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.const_and_test_data import Const, Env



class TestLoginPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_link = Env.MAIN_LINK
        self.login_page = LoginPage(browser, self.login_link)
        self.login_page.open()
        yield


    @pytest.mark.smoke
    def test_should_be_login_form(self, browser):
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_auth_form()


    @pytest.mark.smoke
    def test_should_be_email_field(self, browser):
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_email_field()


    @pytest.mark.smoke
    def test_should_be_password_field(self, browser):
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_password_field()


    @pytest.mark.smoke
    def test_should_be_button_send_login(self, browser):
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_button()


