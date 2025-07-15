import inspect
import time
import pyautogui
import pygetwindow as gw
import requests
from jsonschema import validate, SchemaError
from pywinauto import Application, ElementAmbiguousError
from pywinauto import findwindows
from datetime import datetime, timedelta
import re

import pytest
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from ..utils import take_screenshot
from .locators import MainPageLocators, HeaderLocators, FooterLocators, HotNewsLocators, LoginPageLocators, ReleasePageLocators
from .const_and_test_data import Env, ConstMainPage
from .endpoints import Endpoints



class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.class_name = self.__class__.__name__


    def get_token(self):
        try:
            token = requests.post(Endpoints.Login, json=Endpoints.params, verify="").json()['token']
            return token
        except Exception as err:
            print(f'Произошла ошибка: {err} во время выполнения запроса на выгрузку')


    def logout(self):
        try:
            button_in_lk = self.browser.find_element(*HeaderLocators.BUTTON_IN_LK)
            assert button_in_lk is not None, "Кнопка 'Личный кабинет не найдена'"
            self.browser.execute_script("arguments[0].scrollIntoView();", button_in_lk)
            time.sleep(2)
            button_in_lk.click()
            exit = HeaderLocators.EXIT
            self.click(exit)
            # exit = WebDriverWait(self.browser, 10).until(
            #     EC.element_to_be_clickable(HeaderLocators.EXIT)
            # )
            # exit.click()

            window_log_out = self.find_element(*HeaderLocators.WINDOW_LOG_OUT)
            assert window_log_out is not None, "Диалоговое окно с подтверждением о выходе из системы не появилось"
            # logout = WebDriverWait(self.browser, 10).until(
            #     EC.element_to_be_clickable(HeaderLocators.BUTTON_LOG_OUT)
            # )
            # logout.click()
            logout = HeaderLocators.BUTTON_LOG_OUT
            self.click(logout)

            # time.sleep(3)
        except Exception as e:
            assert False, f"Ошибка при разлогинивании из сервиса: {e}, {type(e)}"


    def should_not_be_authorized_user(self):
        try:
            button_disabled = LoginPageLocators.BUTTON_PERSONAL_ACC
            disabled = WebDriverWait(self.browser, 10).until(
                EC.element_attribute_to_include(button_disabled, 'class')
            )
            button = self.browser.find_element(*button_disabled)
            assert 'disabled' in button.get_attribute('class'), ("Кнопка профиля кликабельна, пользователь авторизован, "
                                                                 "но не должен быть.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")



    def scroll_by_element(self, locator, pixels):
        """
        Ожидаем загрузки последнего элемента на странице.
        Элемент ищем по locator. После того как он будет найден,
        скролим страницу в нужную зону.
        Формат locator - кортеж (как искать, css-селектор).
        """
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(locator)
            )
            time.sleep(1)
            self.browser.execute_script(f"window.scrollBy(0, {pixels});")
        except TimeoutException:
            assert False, f"Элемент с локатором {locator} не найден."


    def take_screenshot_message(self):
        return f'Скриншот: {take_screenshot(self.browser, inspect.currentframe().f_code.co_name)}'


    def open(self):
        self.browser.get(self.url)


    def click(self, locator):
        try:
            element = WebDriverWait(self.browser, timeout=10).until(
                EC.element_to_be_clickable(locator)
            )
            self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.5)
            element.click()
        except TimeoutException:
            assert False, (f"Невозможно совершить клик на элемент с локатором {locator}"
                           f" для {self.__class__.__name__}. {self.take_screenshot_message()}")


    def scroll_and_click(self, locator):
        try:
            element = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            assert False, (f"Элемент с локатором {locator} отсутствует для {self.__class__.__name__}. "
                           f"{self.take_screenshot_message()}")
        self.browser.execute_script("arguments[0].click();", element)
        #assert self.checkbox_is_checked(element), 'Чекбокс не установлен'


    def find_element(self, how, what, timeout=20):
        try:
            locator = WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located((how, what))
            )
        except TimeoutException:
            return None
        return locator


    def should_be_element(self, locator, error_message):
        element = self.find_element(*locator)
        assert element is not None, (
            f'{error_message} для {self.__class__.__name__}. '
            f'{self.take_screenshot_message()}'
        )
        return element


    def should_be_attribute(self, locator, attribute):
        element = self.find_element(*locator)
        assert element is not None, f"Элемент не найден {locator}"
        attribute = element.get_attribute(attribute)
        return attribute


    def should_be_attribute_with_value(self, locator, attribute, value):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.text_to_be_present_in_element_attribute(
                    locator, attribute, value
                )
            )
            return True
        except Exception as e:
            print(f"Произошла ошибка: {e}")


    def should_be_no_attribute_with_value(self, locator, attribute, value):
        try:
            WebDriverWait(self.browser, 10).until_not(
                EC.text_to_be_present_in_element_attribute(
                    locator, attribute, value
                )
            )
            return True
        except Exception as e:
            print(f"Произошла ошибка: {e}")


    def checkbox_is_checked(self, checkbox):
        try:
            WebDriverWait(self.browser, 10).until(EC.element_selection_state_to_be(checkbox, True)),
        except TimeoutException:
            return False
        return True


    def url_contain(self, url, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.url_contains(url)
            )
            return True
        except TimeoutException:
            return False


    def is_element_enabled(self, locator, attribute, value, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.text_to_be_present_in_element_attribute(
                    locator,
                    attribute,
                    value
                )
            )
        except TimeoutException:
            return False
        return True


    def should_be_true_text(self, locator, text_part1, text_part2=None):
        assert text_part1.lower() in locator.text.lower(), (
            f'Ожидаемый текст "{text_part1}" не найден в тексте локатора. '
            f'Фактический текст: "{locator.text}" для {self.__class__.__name__}. '
            f'{self.take_screenshot_message()}'
        )
        if text_part2:
            assert text_part2.lower() in locator.text.lower(), (
                f'Ожидаемый текст "{text_part2}" не найден в тексте локатора. '
                f'Фактический текст: "{locator.text}" для {self.__class__.__name__}. '
                f'{self.take_screenshot_message()}'
            )


    def should_be_true_url(self, path_segment):
        assert self.url_contain(path_segment), (f'Переход осуществлен не на страницу {path_segment}. '
                                             f'Ожидалось - {Env.MAIN_LINK}+{path_segment}. '
                                             f'Фактически - {self.browser.current_url} '
                                             f''
                                             f'для {self.__class__.__name__} {self.take_screenshot_message()}')


    def should_be_correct_title(self, locator_title, expected_title):
        title = locator_title.text
        assert title.lower() == expected_title, (f'Тайтл не верный. Фактический результат - {title.lower()} '
                                                  f'Ожидаемый результат - {expected_title} для '
                                                  f'{self.__class__.__name__}. {self.take_screenshot_message()}')
        return title


    # конвертер форматов цветов (из "#c378e1" в (255, 159, 28) )
    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return (r, g, b)


    def validate_schema_of_response_(self, response, schema):
        try:
            validate(instance=response, schema=schema)
        except SchemaError as e:
            assert False, f"Ответ не соответствует схеме: {e.message}. Ошибка в пути: {list(e.path)}"


class Header(BasePage):

    def should_be_text_in_header(self, locator, expected_text_part1, expected_text_part2=None):
        text_element = self.find_element(*locator)
        assert text_element is not None, (
            f'Заголовок в хедере не найден. '
            f'для {self.__class__.__name__}. '
            f'{self.take_screenshot_message()}'
        )
        self.should_be_true_text(text_element, expected_text_part1)
        if expected_text_part2:
            self.should_be_true_text(text_element, expected_text_part2)
        return text_element


    def should_be_logo_in_header(self):
        return self.should_be_element(HeaderLocators.LOGO_IN_HEADER, 'Логотип страницы в хедере не найден')


    def should_be_button_for_version_unseeing(self):
        return self.should_be_element(HeaderLocators.BUTTON_FOR_VERSION_UNSEEING,
                                      'Кнопка версии для слабовидящих не найдена')


    def should_be_button_in_lk(self):
        return self.should_be_element(HeaderLocators.BUTTON_IN_LK, 'Кнопка меню "Личный Кабинет" не найдена')

    def should_be_link_to_profile(self):
        return self.should_be_element(HeaderLocators.PROFILE, "Кнопка для перехода в 'Мой профиль' не найдена")


    def should_be_link_to_mycompany(self):
        return self.should_be_element(HeaderLocators.MYCOMPANY, "Кнопка для перехода в 'Моя организация' не найдена")


    def should_be_link_to_my_docs(self):
        return self.should_be_element(HeaderLocators.MY_DOSC, "Кнопка для перехода в 'Мои документы' не найдена")


    def should_be_link_to_scientist(self):
        return self.should_be_element(HeaderLocators.SCIENTIST, "Кнопка для перехода в 'Кабинет ученого' не найдена")


    def should_be_link_to_exit(self):
        return self.should_be_element(HeaderLocators.EXIT, "Кнопка 'Выход' не найдена")


    def should_be_module_with_hot_news(self):
        self.should_be_element(HotNewsLocators.MODULE_WITH_HOT_NEWS,
                                      'Модуль с бегущей строкой с новостями не найден')


    def click_logo_in_header(self, locator):
        locator.click()
        current_url = self.browser.current_url
        expected_url = Env.MAIN_LINK
        assert current_url == expected_url, (f'При клике на логотип  в хедере осуществлен переход на URL: {current_url}.'
                                             f' Ожидался URL: {expected_url}. '
                                             f'для {self.__class__.__name__}. '
                                             f'{self.take_screenshot_message()}')


    def should_be_title_text_in_header(self):
        self.should_be_text_in_header(
            HeaderLocators.TITLE_TEXT_IN_HEADER,
            ConstMainPage.title_text_in_header_part1,
            ConstMainPage.title_text_in_header_part2
        )

    def should_be_description_in_header(self):
        self.should_be_text_in_header(
            HeaderLocators.INSCRIPTION_IN_HEADER,
            ConstMainPage.inscription_in_header
        )


    def go_to_version_unseeing_page(self, locator):
        locator.click()
        normal_version = self.find_element(*HeaderLocators.NORMAL_VERSION)
        assert normal_version is not None, (f'Версия для слабовидящих не открывается '
                                            f'для {self.__class__.__name__}. '
                                            f'{self.take_screenshot_message()}')
        normal_version.click()


    def open_up_menu_in_lk(self, locator):
        global open_button_in_lk
        try:
            locator.click()
            open_button_in_lk = self.find_element(*HeaderLocators.OPEN_BUTTON_IN_LK)
            assert open_button_in_lk is not None, (f'Меню личный кабинет не открылось для {self.__class__.__name__}. '
                                                   f'{self.take_screenshot_message()}')
            self.should_be_link_to_profile()
            self.should_be_link_to_mycompany()
            self.should_be_link_to_my_docs()
            self.should_be_link_to_scientist()
            self.should_be_link_to_exit()
        finally:
            open_button_in_lk.click()



class Footer(BasePage):
    def should_be_text_in_footer(self, locator, expected_text_part1, expected_text_part2=None):
        text_element = self.find_element(*locator)
        assert text_element is not None, (
            f'Подпись в футере не найдена. Ожидалось - {expected_text_part1} '
            f'для {self.__class__.__name__}. '
            f'{self.take_screenshot_message()}'
        )
        self.should_be_true_text(text_element, expected_text_part1)
        if expected_text_part2:
            self.should_be_true_text(text_element, expected_text_part2)
        return text_element


    def should_be_true_email(self, link):
        mail = link.get_attribute("href")
        assert mail == ConstMainPage.MAIL_SUPPORT, (
            f'Фича "отправить письмо в ТП" - не верный адрес почты. '
            f'Ожидалось - {ConstMainPage.MAIL_SUPPORT}. Фактические - {mail} для {self.__class__.__name__}'
            f'. {self.take_screenshot_message()}'
        )


    def should_be_logo_csp_in_footer(self):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 2900)
        self.should_be_element(FooterLocators.LOGO_CSP_IN_FOOTER, 'Логотип ЦСП в футере не найден')


    def should_be_logo_fmba_in_footer(self):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 2900)
        self.should_be_element(FooterLocators.LOGO_FMBA_IN_FOOTER, 'Логотип ФМБА в футере не найден')


    def should_be_link_page_release(self):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 2900)
        return self.should_be_element(FooterLocators.LINK_PAGE_REALESE, 'Ссылка на страницу с релизами не найдена')



    def should_be_link_mail_support(self):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 2900)
        link_mail_support = self.should_be_element(FooterLocators.LINK_MAIL_SUPPORT,
                                                   'Фича "отправить письмо в ТП" не найдена')
        return link_mail_support


    def should_be_link_faq(self):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 2900)
        return self.should_be_element(FooterLocators.LINK_FAQ, 'Ссылка на страницу FAQ не найдена')


    def should_be_link_help(self):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 2900)
        return self.should_be_element(FooterLocators.LINK_HELP, 'Ссылка на страницу "Справка ИАС" не найдена')


    def should_be_text_csp_in_footer(self):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 2900)
        self.should_be_text_in_footer(
            FooterLocators.TEXT_CSP_IN_FOOTER,
            ConstMainPage.text_csp_in_footer
        )


    def should_be_text_fmba_in_footer(self):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 2900)
        self.should_be_text_in_footer(
            FooterLocators.TEXT_FMBA_IN_FOOTER,
            ConstMainPage.text_fmba_in_footer_part1,
            ConstMainPage.text_fmba_in_footer_part2
        )


    def should_be_title_and_inscription_in_footer(self):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 2900)
        self.should_be_text_in_footer(
            FooterLocators.TITLE_AND_INSCRIPTION_IN_FOOTER,
            ConstMainPage.title_and_inscription_in_footer_part1,
            ConstMainPage.inscription_in_header)