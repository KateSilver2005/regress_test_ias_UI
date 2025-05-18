from .base_page import BasePage
from .locators import AnaliticPageLocators
from .const_and_test_data import Const


class PageAnalitic(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)


    def should_be_page_analitic(self):
        title = self.should_be_element(AnaliticPageLocators.TITLE, 'Заголовок на странице не найден')
        path_segment = Const.analitic_path
        expected_title = Const.title_in_analitic_page
        url = Const.MAIN_LINK + path_segment
        self.should_be_true_url(url, path_segment)
        self.should_be_correct_title(title, expected_title)
