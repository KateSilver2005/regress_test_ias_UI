import inspect

from .base_page import BasePage
from .locators import LoginPageLocators
from .const_and_test_data import TestData

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage(BasePage):

    def should_be_auth_form(self):
        assert self.find_element(*LoginPageLocators.AUTH_FORM), \
            f'Форма авторизации пользователя отсутствует в {self.class_name}. {self.take_screenshot_message()}'


    def should_be_email_field(self):
        assert self.find_element(*LoginPageLocators.ENTER_EMAIL), \
            f'Поле для ввода логина отсутствует в {self.class_name}. {self.take_screenshot_message()}'

    def should_be_password_field(self):
        assert self.find_element(*LoginPageLocators.ENTER_PASSWORD), \
            f'Поле для ввода пароля отсутствует в {self.class_name}. {self.take_screenshot_message()}'

    def should_be_button(self):
        assert self.find_element(*LoginPageLocators.BUTTON_ENTER), \
            f'Кнопка для отправки данных авторизации отсутствует в {self.class_name}. {self.take_screenshot_message()}'


    def log_in(self):
        login = TestData.TEST_LOGIN
        password = TestData.TEST_PASSWORD
        choose_domain = self.find_element(*LoginPageLocators.CHOOSE_DOMAIN)
        choose_domain.click()
        no_domain = self.find_element(*LoginPageLocators.NO_DOMAIN)
        no_domain.click()
        enter_email = self.find_element(*LoginPageLocators.ENTER_EMAIL)
        enter_email.send_keys(login)
        enter_password = self.find_element(*LoginPageLocators.ENTER_PASSWORD)
        enter_password.send_keys(password)
        enter = self.find_element(*LoginPageLocators.BUTTON_ENTER)
        enter.click()


    def should_be_authorized_user(self):
        button_enabled = LoginPageLocators.BUTTON_PERSONAL_ACC
        attribute = "class"
        value = "px-4 btn btn-primary dropdown-toggle transition-ease"
        assert self.is_element_enabled(button_enabled, attribute, value), (f"Пользователь не авторизован"
                                                                           f"для {self.__class__.__name__}. "
                                                                           f"{self.take_screenshot_message()}")















