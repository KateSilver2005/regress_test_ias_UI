import inspect

from ..utils import take_screenshot
from .base_page import BasePage
from .locators import SearchCompetencyPageLocators
from .const_and_test_data import TestData


class SearchCompetencyPage(BasePage):
    def find_search_bar(self):
        search_bar = self.find_element(*SearchCompetencyPageLocators.SEARCH_BAR)
        assert search_bar, (f'Поисковая строка не найдена в {self.__class__.__name__}. '
                            f'Скриншот: {take_screenshot(self.browser, inspect.currentframe().f_code.co_name)}')
        return search_bar

    def enter_request(self, search_bar):
        search_bar.send_keys(TestData.SEARCH_COMPETENCY)
        search_button = self.find_element(*SearchCompetencyPageLocators.BUTTON_SEARCH)
        assert search_button, (f'Кнопка "Поиск" не найдена в {self.__class__.__name__}. '
                               f'Скриншот: {take_screenshot(self.browser, inspect.currentframe().f_code.co_name)}')
        search_button.click()

    def should_be_result(self):
        self.should_be_module_map()
        self.should_be_content_map()
        self.should_be_module_statistics()
        self.should_be_content_statistics()
        self.should_be_module_graph_ak()
        self.should_be_module_graph_ko()
        self.should_be_module_rating()
        self.should_be_content_rating()


    def should_be_module_map(self):
        assert self.find_element(*SearchCompetencyPageLocators.MODULE_MAP), \
            (f'Модуль Карта не найден в {self.__class__.__name__}. '
             f'Скриншот: {take_screenshot(self.browser, inspect.currentframe().f_code.co_name)}')


    def should_be_content_map(self):
        assert self.find_element(*SearchCompetencyPageLocators.CONTENT_MAP), \
            (f'Содержимое модуля Карта не найдено в {self.__class__.__name__}. '
             f'Скриншот: {take_screenshot(self.browser, inspect.currentframe().f_code.co_name)}')


    def should_be_module_statistics(self):
        assert self.find_element(*SearchCompetencyPageLocators.MODULE_STATISTICS), \
            (f'Модуль Статистика не найден в {self.__class__.__name__}. '
             f'Скриншот: {take_screenshot(self.browser, inspect.currentframe().f_code.co_name)}')


    def should_be_content_statistics(self):
        assert self.find_element(*SearchCompetencyPageLocators.CONTENT_STATISTICS), \
            (f'Содержимое модуля Статистика не найдено в {self.__class__.__name__}. '
             f'Скриншот: {take_screenshot(self.browser, inspect.currentframe().f_code.co_name)}')


    def should_be_module_graph_ak(self):
        assert self.find_element(*SearchCompetencyPageLocators.MODULE_GRAPH_AK), \
            (f'Модуль граф авторсике коллективы не найден в {self.__class__.__name__}. '
             f'Скриншот: {take_screenshot(self.browser, inspect.currentframe().f_code.co_name)}')


    def should_be_module_graph_ko(self):
        assert self.find_element(*SearchCompetencyPageLocators.MODULE_GRAPH_KO), \
            (f'Модуль граф коллаборации организаций не найден в {self.__class__.__name__}. '
             f'Скриншот: {take_screenshot(self.browser, inspect.currentframe().f_code.co_name)}')


    def should_be_module_rating(self):
        assert self.find_element(*SearchCompetencyPageLocators.CONTENT_RATING), \
            (f'Модуль рейтинг организаций/ученых не найден в {self.__class__.__name__}. '
             f'Скриншот: {take_screenshot(self.browser, inspect.currentframe().f_code.co_name)}')


    def should_be_content_rating(self):
        assert self.find_element(*SearchCompetencyPageLocators.MODULE_RATING), \
            (f'Содержимое модуля рейтинг организаций/ученых не найдено в {self.__class__.__name__}. '
             f'Скриншот: {take_screenshot(self.browser, inspect.currentframe().f_code.co_name)}')
