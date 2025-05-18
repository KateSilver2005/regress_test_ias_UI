import time

import pytest

from .pages.locators import HotNewsLocators
from .pages.login_page import LoginPage
from .pages.news_page import NewsPage
from .pages.main_page import MainPage
from .pages.base_page import Header
from .pages.hot_news_module import HotNewsModule
from .pages.const_and_test_data import Const



@pytest.fixture(scope="session", autouse=True)
def reset_total_count(request):
    request.config.cache.set("total_hot_news_count", 0)


@pytest.mark.hot_news
class TestMainPageHotNews:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, module_browser, request):
        self.login_link = Const.MAIN_LINK
        self.login_page = LoginPage(module_browser, self.login_link)
        self.login_page.open()
        self.login_page.log_in()
        self.login_page.should_be_authorized_user()
        self.hot_news_module = HotNewsModule(module_browser, module_browser.current_url)
        yield
        self.hot_news_module.logout()
        self.login_page.should_not_be_authorized_user()


    @pytest.fixture(scope="class")
    def title_date_icon_link_data(self):
        return {}


    @pytest.mark.dependency(name="module_with_hot_news")
    def test_should_be_module_with_hot_news(self, module_browser):
        hot_news_module = Header(module_browser, module_browser.current_url)
        hot_news_module.should_be_module_with_hot_news()


    @pytest.mark.dependency(depends=["module_with_hot_news"])
    @pytest.mark.parametrize("page", range(1, 56))
    def test_should_be_hot_news(self, module_browser, page, request):
        hot_news_module = HotNewsModule(module_browser, module_browser.current_url)
        pages = hot_news_module.total_pages()
        if page > pages:
            pytest.skip(f"Пропустили тесты на {page}-й странице, так как всего страниц - {pages}.")
        count_hot_news = hot_news_module.should_be_five_hot_news_on_page(page)
        calculated_total_news = request.config.cache.get("total_hot_news_count", 0)  # Берем из кеша
        calculated_total_news += count_hot_news
        request.config.cache.set("total_hot_news_count", calculated_total_news)  # Сохраняем в кеш
        hot_news_module.calculated_total_news = calculated_total_news
        if page < pages:
            hot_news_module.go_to_next_page_in_hot_news()
        if page == pages:
            time.sleep(12)


    @pytest.mark.dependency(depends=["module_with_hot_news"])
    @pytest.mark.parametrize("page, news", [(page, news) for page in range(1, 56) for news in range(1, 6)])
    def test_get_title_date_icon_link_for_each_news(self, page, news, module_browser, title_date_icon_link_data):
        hot_news_module = HotNewsModule(module_browser, module_browser.current_url)
        pages = hot_news_module.total_pages()
        if page > pages:
            pytest.skip(f"Пропустили тесты на {page}-й странице, так как всего страниц - {pages}.")
        hot_news_module.title_date_icon_link_data = title_date_icon_link_data
        hot_news_module.go_to_set_page_in_hot_news_and_get_attributes(page, news, title_date_icon_link_data)



    @pytest.mark.dependency(depends=["module_with_hot_news"])
    @pytest.mark.parametrize("page, news", [(page, news) for page in range(1, 56) for news in range(1, 6)])
    def test_should_be_actual_date_on_each_news_in_hot_news(self, module_browser, page, news, title_date_icon_link_data):
        hot_news_module = HotNewsModule(module_browser, module_browser.current_url)
        pages = hot_news_module.total_pages()
        if page > pages:
            pytest.skip(f"Пропустили тесты на {page}-й странице, так как всего страниц - {pages}.")
        hot_news_module.should_be_actual_date_in_hot_news(title_date_icon_link_data, page,
                                                          news)


    @pytest.mark.dependency(depends=["module_with_hot_news"])
    @pytest.mark.parametrize("page, news", [(page, news) for page in range(1, 56) for news in range(1, 6)])
    def test_should_be_title_on_each_news_in_hot_news(self, module_browser, page, news, title_date_icon_link_data):
        hot_news_module = HotNewsModule(module_browser, module_browser.current_url)
        pages = hot_news_module.total_pages()
        if page > pages:
            pytest.skip(f"Пропустили тесты на {page}-й странице, так как всего страниц - {pages}.")
        hot_news_module.should_be_title_in_hot_news(title_date_icon_link_data, page, news)


    @pytest.mark.dependency(depends=["module_with_hot_news"])
    @pytest.mark.parametrize("page, news", [(page, news) for page in range(1, 56) for news in range(1, 6)])
    def test_should_be_icon_on_each_news_in_hot_news(self, module_browser, page, news, title_date_icon_link_data):
        hot_news_module = HotNewsModule(module_browser, module_browser.current_url)
        pages = hot_news_module.total_pages()
        if page > pages:
            pytest.skip(f"Пропустили тесты на {page}-й странице, так как всего страниц - {pages}.")
        hot_news_module.should_be_icon_in_hot_news(title_date_icon_link_data, page, news)


    @pytest.mark.dependency(depends=["module_with_hot_news"])
    @pytest.mark.parametrize("page, news", [(page, news) for page in range(1, 56) for news in range(1, 6)])
    def should_be_link_on_each_news_in_hot_news(self, module_browser, page, news, title_date_icon_link_data):
        hot_news_module = HotNewsModule(module_browser, module_browser.current_url)
        pages = hot_news_module.total_pages()
        if page > pages:
            pytest.skip(f"Пропустили тесты на {page}-й странице, так как всего страниц - {pages}.")
        hot_news_module.should_be_link_in_hot_news(title_date_icon_link_data, page, news)


    #----------------------------------------------------
    @pytest.mark.dependency(depends=["module_with_hot_news"])
    @pytest.mark.parametrize("page, news", [(page, news) for page in range(1, 56) for news in range(1, 6)])
    def test_should_be_equal_title_in_page_news(self, module_browser, page, news, title_date_icon_link_data):
        hot_news_module = HotNewsModule(module_browser, module_browser.current_url)
        pages = hot_news_module.total_pages()
        if page > pages:
            pytest.skip(f"Пропустили тесты на {page}-й странице, так как всего страниц - {pages}.")
        news_page = NewsPage(module_browser, module_browser.current_url)
        link = news_page.go_to_news_page(title_date_icon_link_data, page, news)
        title_from_page = news_page.should_be_title_on_each_news(link)
        news_page.should_be_title_equal_with_title_in_hot_news(link, title_date_icon_link_data, title_from_page, page, news)




    @pytest.mark.dependency(depends=["module_with_hot_news"])
    @pytest.mark.parametrize("page, news", [(page, news) for page in range(1, 56) for news in range(1, 6)])
    def test_should_be_equal_date_in_page_news(self, module_browser, page, news, title_date_icon_link_data):
        hot_news_module = HotNewsModule(module_browser, module_browser.current_url)
        pages = hot_news_module.total_pages()
        if page > pages:
            pytest.skip(f"Пропустили тесты на {page}-й странице, так как всего страниц - {pages}.")
        news_page = NewsPage(module_browser, module_browser.current_url)
        link = news_page.go_to_news_page(title_date_icon_link_data, page, news)
        date_from_page = news_page.should_be_date(link)
        news_page.should_be_date_equal_with_date_in_hot_news(link, title_date_icon_link_data, date_from_page, page, news)


    @pytest.mark.dependency(depends=["module_with_hot_news"])
    @pytest.mark.parametrize("page, news", [(page, news) for page in range(1, 56) for news in range(1, 6)])
    def test_should_be_equal_type_icon_in_page_news(self, module_browser, page, news, title_date_icon_link_data):
        hot_news_module = HotNewsModule(module_browser, module_browser.current_url)
        pages = hot_news_module.total_pages()
        if page > pages:
            pytest.skip(f"Пропустили тесты на {page}-й странице, так как всего страниц - {pages}.")
        news_page = NewsPage(module_browser, module_browser.current_url)
        link = news_page.go_to_news_page(title_date_icon_link_data, page, news)
        type_icon_from_page = news_page.should_be_type_icon(link)
        news_page.should_be_type_icon_equal_with_type_icon_in_hot_news(link, title_date_icon_link_data, type_icon_from_page,
                                                                       page, news)


    @pytest.mark.dependency(depends=["module_with_hot_news"])
    @pytest.mark.parametrize("page, news", [(page, news) for page in range(1, 56) for news in range(1, 6)])
    def test_should_be_equal_description_icon_in_page_news(self, module_browser, page, news, title_date_icon_link_data):
        hot_news_module = HotNewsModule(module_browser, module_browser.current_url)
        pages = hot_news_module.total_pages()
        if page > pages:
            pytest.skip(f"Пропустили тесты на {page}-й странице, так как всего страниц - {pages}.")
        news_page = NewsPage(module_browser, module_browser.current_url)
        link = news_page.go_to_news_page(title_date_icon_link_data, page, news)
        description_icon = news_page.should_be_description_icon(link)
        news_page.should_be_description_icon_equal_with_description_icon_in_hot_news(link, title_date_icon_link_data,
                                                                                     description_icon, page, news)



    @pytest.mark.dependency(depends=["module_with_hot_news"])
    def test_counter_news_equal_total_news_on_each_page_in_hot_news(self, module_browser, request):
        hot_news_module = HotNewsModule(module_browser, module_browser.current_url)
        static_total_news = hot_news_module.total_news()
        calculated_total_news = request.config.cache.get("total_hot_news_count", 0)
        hot_news_module.can_equal_total_news_on_each_page_in_hot_news(static_total_news, calculated_total_news)


    @pytest.mark.dependency(depends=["module_with_hot_news"])
    def test_can_go_to_page_with_all_news(self, module_browser):
        hot_news_module = HotNewsModule(module_browser, module_browser.current_url)
        link = hot_news_module.should_be_link_on_page_news()
        link.click()
        page_news = NewsPage(module_browser, module_browser.current_url)
        page_news.should_be_page_news()








