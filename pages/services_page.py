from .base_page import BasePage
from .locators import ServicesPageLocators
from .const_and_test_data import ConstServicesPage, Env


class PageServices(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)


    def should_be_page_services(self):
        title = self.should_be_element(ServicesPageLocators.TITLE, 'Заголовок на странице не найден')
        path_segment = ConstServicesPage.services_path
        expected_string = ConstServicesPage.title_in_services_page
        url = Env.MAIN_LINK + path_segment
        self.should_be_true_url(path_segment)
        self.should_be_correct_title(title, expected_string)
