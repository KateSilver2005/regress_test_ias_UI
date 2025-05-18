from .base_page import BasePage
from .locators import ServicesPageLocators
from .const_and_test_data import Const


class PageServices(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)


    def should_be_page_services(self):
        title = self.should_be_element(ServicesPageLocators.TITLE, 'Заголовок на странице не найден')
        path_segment = Const.services_path
        expected_string = Const.title_in_services_page
        url = Const.MAIN_LINK + path_segment
        self.should_be_true_url(url, path_segment)
        self.should_be_correct_title(title, expected_string)
