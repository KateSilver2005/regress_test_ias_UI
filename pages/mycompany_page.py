from .base_page import BasePage
from .locators import InfoAboutProviderPageLocators
from .const_and_test_data import ConstMyCompanyPage, Env


class PageInfoAboutProvider(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)


    def should_be_page_info_about_provider(self):
        title = self.should_be_element(InfoAboutProviderPageLocators.TITLE, 'Заголовок на странице не найден')
        path_segment = ConstMyCompanyPage.my_company_path
        expected_string = ConstMyCompanyPage.title_in_info_about_provider_page
        url = Env.MAIN_LINK + path_segment
        self.should_be_true_url(path_segment)
        self.should_be_correct_title(title, expected_string)

