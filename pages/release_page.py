from .base_page import Footer
from .locators import ReleasePageLocators
from .const_and_test_data import ConstRealesePage, Env


class PageRelease(Footer):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)


    def should_be_page_release(self):
        title = self.should_be_element(ReleasePageLocators.TITLE, 'Заголовок на странице не найден')
        path_segment = ConstRealesePage.release_path
        expected_string = ConstRealesePage.title_in_release_page
        url = Env.MAIN_LINK + path_segment
        self.should_be_true_url(path_segment)
        self.should_be_correct_title(title, expected_string)








