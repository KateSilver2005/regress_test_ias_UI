import pytest
import time

from .pages.const_and_test_data import Const
from .pages.login_page import LoginPage
from .pages.search_competency_page import SearchCompetencyPage


@pytest.mark.smoke
class TestSearchCompetency:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_link = Const.MAIN_LINK
        self.login_page = LoginPage(browser, self.login_link)
        self.login_page.open()
        self.login_page.log_in()
        self.login_page.should_be_authorized_user()
        time.sleep(2)


    def test_user_can_make_search(self, browser):
        competency_page = SearchCompetencyPage(browser, browser.current_url)
        search_bar = competency_page.find_search_bar()
        competency_page.enter_request(search_bar)
        competency_page.should_be_result()
