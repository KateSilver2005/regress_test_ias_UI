from .base_page import Footer
from .locators import ReleasePageLocators
from .const_and_test_data import Const


class PageRelease(Footer):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)


    def should_be_page_release(self):
        title = self.should_be_element(ReleasePageLocators.TITLE, 'Заголовок на странице не найден')
        path_segment = Const.release_path
        expected_string = Const.title_in_release_page
        url = Const.MAIN_LINK + path_segment
        self.should_be_true_url(url, path_segment)
        self.should_be_correct_title(title, expected_string)








