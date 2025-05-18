import time

import pytest

from .pages.main_page import MainPage
from .pages.locators import MainPageLocators, AdvancedSearch
from .pages.const_and_test_data import Const
from .pages.login_page import LoginPage
from .pages.release_page import PageRelease
from .pages.faq_page import PageFaq
from .pages.base_page import Header, Footer
from .pages.help_page import PageHelp
from .pages.analitic_page import PageAnalitic
from .pages.services_page import PageServices
from .pages.mycompany_page import PageInfoAboutProvider
from .pages.news_page import NewsPage


# class TestMainPageHeaderFooter:
#     @pytest.fixture(scope="function", autouse=True)
#     def setup(self, browser):
#         self.login_link = Const.MAIN_LINK
#         self.login_page = LoginPage(browser, self.login_link)
#         self.login_page.open()
#         self.login_page.log_in()
#         self.login_page.should_be_authorized_user()
#         self.main_page = MainPage(browser, browser.current_url)
#         yield
#         self.main_page.logout()
#         self.login_page = LoginPage(browser, browser.current_url)
#         self.login_page.should_not_be_authorized_user()
#
#     # header
#     def test_can_click_logo_in_header(self, browser):
#         main_page = Header(browser, browser.current_url)
#         logo_in_header = main_page.should_be_logo_in_header()
#         main_page.click_logo_in_header(logo_in_header)
#
#     def test_should_be_title_text_in_header(self, browser):
#         main_page = Header(browser, browser.current_url)
#         main_page.should_be_title_text_in_header()
#
#     def test_should_be_description_in_header(self, browser):
#         main_page = Header(browser, browser.current_url)
#         main_page.should_be_description_in_header()
#
#     def test_can_go_to_version_unseeing_page(self, browser):
#         main_page = Header(browser, browser.current_url)
#         button_for_version_unseeing = main_page.should_be_button_for_version_unseeing()
#         main_page.go_to_version_unseeing_page(button_for_version_unseeing)
#
#     def test_can_open_up_menu_in_lk(self, browser):
#         main_page = Header(browser, browser.current_url)
#         button_in_lk = main_page.should_be_button_in_lk()
#         main_page.open_up_menu_in_lk(button_in_lk)
#
#     def test_should_be_module_with_hot_news(self, browser):
#         hot_news_module = Header(browser, browser.current_url)
#         hot_news_module.should_be_module_with_hot_news()
#
#         # footer
#     def test_should_be_logo_csp_in_footer(self, browser):
#         main_page = Footer(browser, browser.current_url)
#         main_page.should_be_logo_csp_in_footer()
#
#
#     def test_should_be_text_csp_in_footer(self, browser):
#         main_page = Footer(browser, browser.current_url)
#         main_page.should_be_text_csp_in_footer()
#
#
#     def test_should_be_logo_fmba_in_footer(self, browser):
#         main_page = Footer(browser, browser.current_url)
#         main_page.should_be_logo_fmba_in_footer()
#
#
#     def test_should_be_text_fmba_in_footer(self, browser):
#         main_page = Footer(browser, browser.current_url)
#         main_page.should_be_text_fmba_in_footer()
#
#
#     def test_should_be_inscription_in_footer(self, browser):
#         main_page = Footer(browser, browser.current_url)
#         main_page.should_be_title_and_inscription_in_footer()
#
#
#     def test_can_go_to_realese_page(self, browser):
#         main_page = Footer(browser, browser.current_url)
#         link = main_page.should_be_link_page_release()
#         link.click()
#         release_page = PageRelease(browser, browser.current_url)
#         release_page.should_be_page_release()
#
#
#     def test_can_write_mail_to_support(self, browser):
#         main_page = Footer(browser, browser.current_url)
#         link = main_page.should_be_link_mail_support()
#         main_page.should_be_true_email(link)
#
#
#     def test_can_go_to_faq_page(self, browser):
#         main_page = Footer(browser, browser.current_url)
#         link = main_page.should_be_link_faq()
#         link.click()
#         faq_page = PageFaq(browser, browser.current_url)
#         faq_page.should_be_page_faq()
#
#
#     def test_can_go_to_help_page(self, browser):
#         main_page = Footer(browser, browser.current_url)
#         link = main_page.should_be_link_help()
#         link.click()
#         help_page = PageHelp(browser, browser.current_url)
#         help_page.should_be_page_help()



class TestMainPage:

    response_api_charts = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_link = Const.MAIN_LINK
        self.login_page = LoginPage(browser, self.login_link)
        self.login_page.open()
        self.login_page.log_in()
        self.login_page.should_be_authorized_user()
        self.main_page = MainPage(browser, browser.current_url)
        yield
        self.main_page.logout()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.should_not_be_authorized_user()


    # @pytest.mark.smoke
    # def test_can_go_to_analitic(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     button_analitic = main_page.should_be_button_analitic()
    #     button_analitic.click()
    #     analitic_page = PageAnalitic(browser, browser.current_url)
    #     analitic_page.should_be_page_analitic()
    #
    # @pytest.mark.smoke
    # def test_can_go_to_services(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     button_in_services = main_page.should_be_button_in_services()
    #     button_in_services.click()
    #     services_page = PageServices(browser, browser.current_url)
    #     services_page.should_be_page_services()
    #
    #
    # @pytest.mark.smoke
    # def test_can_go_to_info_about_provider(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     info_about_provider = main_page.should_be_button_info_about_infoprovider()
    #     info_about_provider.click()
    #     info_about_provider_page = PageInfoAboutProvider(browser, browser.current_url)
    #     info_about_provider_page.should_be_page_info_about_provider()
    #
    #
    # @pytest.mark.smoke
    # def test_should_be_title_lk(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.should_be_title_lk()
    #
    #
    # # переключатель поисков: по компетенциям, документам, ученым, организациям
    # @pytest.mark.smoke
    # @pytest.mark.dependency(name="tabs_of_search")
    # def test_should_be_tabs_of_search(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.should_be_tabs_search()
    #
    #
    # @pytest.mark.smoke
    # @pytest.mark.dependency(name="each_tabs_of_search", depends=["tabs_of_search"])
    # @pytest.mark.parametrize("locator", MainPageLocators.TABS, ids=[
    #     "test_should_be_tab_competency",
    #     "test_should_be_tab_doc",
    #     "test_should_be_tab_org",
    #     "test_should_be_tab_person"
    # ])
    # def test_should_be_tabs(self, locator, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     tab = main_page.should_be_tabs(locator)
    #     main_page.click(tab)
    #     main_page.should_be_active(tab)
    #
    #
    # @pytest.mark.smoke
    # @pytest.mark.dependency(name="search_area_in_tabs", depends=["tabs_of_search", "each_tabs_of_search"])
    # @pytest.mark.parametrize("locator, placeholder", MainPageLocators.PLACEHOLDERS_IN_SEARCH_AREA_TABS, ids=[
    #     "test_should_be_search_area_in_tab_competency",
    #     "test_should_be_search_area_in_tab_doc",
    #     "test_should_be_search_area_in_tab_org",
    #     "test_should_be_search_area_in_tab_person"
    # ])
    # def test_should_be_search_area_with_placeholder_of_tabs(self, locator, placeholder, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.click(locator)
    #     search_area = main_page.should_be_search_area()
    #     main_page.should_be_placeholder(search_area, placeholder)
    #
    #
    # @pytest.mark.smoke
    # @pytest.mark.dependency(depends=["tabs_of_search", "search_area_in_tabs", "each_tabs_of_search"])
    # @pytest.mark.parametrize("locator", MainPageLocators.TABS, ids=[
    #     "test_should_be_tab_competency",
    #     "test_should_be_tab_doc",
    #     "test_should_be_tab_org",
    #     "test_should_be_tab_person"
    # ])
    # def test_should_be_clear_button_in_search_area_of_tabs(self, locator, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.click(locator)
    #     main_page.should_be_clear_button()
    #
    #
    # @pytest.mark.smoke
    # @pytest.mark.dependency(depends=["tabs_of_search", "search_area_in_tabs", "each_tabs_of_search"])
    # @pytest.mark.parametrize("locator", MainPageLocators.TABS, ids=[
    #     "test_should_be_tab_competency",
    #     "test_should_be_tab_doc",
    #     "test_should_be_tab_org",
    #     "test_should_be_tab_person"
    # ])
    # def test_should_be_button_search_in_search_area_of_tabs(self, locator, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.click(locator)
    #     search_button = main_page.should_be_button_search()
    #     main_page.should_be_element_is_disabled(search_button)
    #
    #
    # @pytest.mark.smoke
    # @pytest.mark.dependency(name='advanced_search_filter', depends=["tabs_of_search", "search_area_in_tabs", "each_tabs_of_search"])
    # @pytest.mark.parametrize("tab", MainPageLocators.TABS[:2], ids=[
    #     "test_should_be_in_tab_competency",
    #     "test_should_be_in_tab_doc",
    # ])
    # def test_should_be_advanced_search_filter_in_search_area_of_tabs(self, tab, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.click(tab)
    #     main_page.should_be_advanced_search_button()
    #     main_page.can_click_on_advanced_search_button()
    #
    #
    #
    # @pytest.mark.smoke
    # @pytest.mark.dependency(depends=["tabs_of_search", "each_tabs_of_search", "advanced_search_filter"])
    # @pytest.mark.parametrize("tab, checkbox, label, label_text", AdvancedSearch.FILTERS_IN_ADVANCED_SEARCH, ids=[
    #     "test_should_be_in_tab_competency_checkbox_synonym_and_label",
    #     "test_should_be_in_tab_competency_checkbox_fulltext_and_label",
    #     "test_should_be_in_tab_competency_checkbox_distance_and_label",
    #     "test_should_be_in_tab_doc_checkbox_synonym_and_label",
    #     "test_should_be_in_tab_doc_checkbox_fulltext_and_label",
    #     "test_should_be_in_tab_doc_checkbox_distance_and_label"
    # ])
    # def test_should_be_filters_in_advanced_search_of_tabs(self, tab, checkbox, label, label_text, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.click(tab)
    #     main_page.can_click_on_advanced_search_button()
    #     main_page.should_be_checkbox(checkbox)
    #     main_page.should_be_label(label, label_text)
    #
    #
    # @pytest.mark.smoke
    # @pytest.mark.dependency(depends=["tabs_of_search", "each_tabs_of_search", "advanced_search_filter"])
    # @pytest.mark.parametrize("tab, checkbox, dependent_checkbox", AdvancedSearch.CHECKBOX_SYNONYM, ids=[
    #     "test_can_click_in_tab_competency_on_checkbox_synonym_and_checkbox_distance_is_disabled",
    #     "test_can_click_in_tab_doc_on_checkbox_synonym_and_checkbox_distance_is_disabled"
    # ])
    # def test_can_click_on_checkbox_synonym_in_advanced_search_of_tabs(self, tab, checkbox, dependent_checkbox, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.click(tab)
    #     main_page.can_click_on_advanced_search_button()
    #     checkbox_enabled = main_page.should_be_checkbox(dependent_checkbox)
    #     main_page.scroll_and_click(checkbox)
    #     main_page.should_be_element_is_disabled(checkbox_enabled, dependent_checkbox)
    #
    #
    # @pytest.mark.smoke
    # @pytest.mark.dependency(depends=["tabs_of_search", "each_tabs_of_search", "advanced_search_filter"])
    # @pytest.mark.parametrize("tab, checkbox", AdvancedSearch.CHECKBOX_FULLTEXT, ids=[
    #     "test_can_click_in_tab_competency_on_checkbox_fulltext",
    #     "test_can_click_in_tab_doc_on_checkbox_fulltext"
    # ])
    # def test_can_click_on_checkbox_fulltext_in_advanced_search_of_tabs(self, tab, checkbox, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.click(tab)
    #     main_page.can_click_on_advanced_search_button()
    #     main_page.scroll_and_click(checkbox)
    #
    #
    #
    # @pytest.mark.smoke
    # @pytest.mark.dependency(depends=["tabs_of_search", "each_tabs_of_search", "advanced_search_filter"])
    # @pytest.mark.parametrize("tab, distance_checkbox, synonym_checkbox, range_distance, pixsels, steps", AdvancedSearch.CHECKBOX_DISTANCE, ids=[
    #     "test_can_click_in_tab_competency_on_checkbox_distance_change_distance_0_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_competency_on_checkbox_distance_change_distance_1_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_competency_on_checkbox_distance_change_distance_2_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_competency_on_checkbox_distance_change_distance_3_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_competency_on_checkbox_distance_change_distance_4_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_competency_on_checkbox_distance_change_distance_5_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_competency_on_checkbox_distance_change_distance_6_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_competency_on_checkbox_distance_change_distance_7_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_competency_on_checkbox_distance_change_distance_8_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_competency_on_checkbox_distance_change_distance_9_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_competency_on_checkbox_distance_change_distance_10_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_doc_on_checkbox_distance_change_distance_0_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_doc_on_checkbox_distance_change_distance_1_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_doc_on_checkbox_distance_change_distance_2_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_doc_on_checkbox_distance_change_distance_3_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_doc_on_checkbox_distance_change_distance_4_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_doc_on_checkbox_distance_change_distance_5_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_doc_on_checkbox_distance_change_distance_6_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_doc_on_checkbox_distance_change_distance_7_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_doc_on_checkbox_distance_change_distance_8_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_doc_on_checkbox_distance_change_distance_9_and_checkbox_synonym_is_disabled",
    #     "test_can_click_in_tab_doc_on_checkbox_distance_change_distance_10_and_checkbox_synonym_is_disabled"
    # ])
    # def test_can_click_on_checkbox_distance_in_advanced_search_of_tabs(self, tab, distance_checkbox, synonym_checkbox,
    #                                                                    range_distance, pixsels, steps, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.click(tab)
    #     main_page.can_click_on_advanced_search_button()
    #     checkbox_enabled = main_page.should_be_checkbox(synonym_checkbox)
    #     main_page.scroll_and_click(distance_checkbox)
    #     main_page.should_be_element_is_disabled(checkbox_enabled, synonym_checkbox)
    #     element = main_page.should_be_range_distance(range_distance)
    #     main_page.can_change_distance(element, pixsels, range_distance, browser, steps)
    #     main_page.should_be_label_range_distance(steps)
    #
    #
    # @pytest.mark.smoke
    # @pytest.mark.dependency(depends=["tabs_of_search", "each_tabs_of_search", "advanced_search_filter"])
    # @pytest.mark.parametrize("tab, checkbox1, checkbox2, dependent_checkbox",
    #                          AdvancedSearch.CHECKBOX_SYNONYM_AND_FULLTEXT, ids=[
    #     "test_can_click_in_tab_competency_on_checkbox_synonym_and_fulltext",
    #     "test_can_click_in_tab_doc_on_checkbox_synonym_and_fulltext",
    #     "test_can_click_in_tab_competency_on_checkbox_fulltext_and_distance",
    #     "test_can_click_in_tab_doc_on_checkbox_fulltext_and_distance",
    # ])
    # def test_can_click_on_two_checkboxes_in_advanced_search_of_tabs(self, tab, checkbox1, checkbox2,
    #                                                                 dependent_checkbox, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.click(tab)
    #     main_page.can_click_on_advanced_search_button()
    #     checkbox_enabled = main_page.should_be_checkbox(dependent_checkbox)
    #     main_page.scroll_and_click(checkbox1)
    #     main_page.scroll_and_click(checkbox2)
    #     main_page.should_be_element_is_disabled(checkbox_enabled, dependent_checkbox)
    #
    #
    # @pytest.mark.dependency(name="grafic_vneseniya_svedeniy")
    # def test_should_be_grafic_vneseniya_svedeniy(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.should_be_slider(MainPageLocators.GRAFIC_VNESENIYA_SVEDEDIY)
    #
    #
    # @pytest.mark.dependency(depends=["grafic_vneseniya_svedeniy"])
    # def test_should_be_title_grafic_vneseniya_svedeniy(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.should_be_title_for_slider(MainPageLocators.TITLE_GRAFIC_VNESENIYA_SVEDEDIY,
    #                                          Const.title_grafic_vneseniya_svedeniy)
    #
    #
    # @pytest.mark.dependency(depends=["grafic_vneseniya_svedeniy"])
    # def test_should_be_12_slides_in_grafic_vneseniya_svedeniy(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.should_be_slides(MainPageLocators.LIST_SLIDES_IN_GRAFIC_VNESENIYA_SVEDEDIY, 12, 750)
    #
    #
    # @pytest.mark.dependency(name="button_next_slide_in_grafic_vneseniya_svedeniy", depends=["grafic_vneseniya_svedeniy"])
    # def test_should_be_button_next_slide_in_grafic_vneseniya_svedeniy(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.should_be_button_next_slide(MainPageLocators.NEXT_SLIDE_IN_GRAFIC_VNESENIYA_SVEDEDIY, 750)
    #
    #
    # @pytest.mark.dependency(name="button_previous_slide_in_grafic_vneseniya_svedeniy", depends=["grafic_vneseniya_svedeniy"])
    # def test_should_be_button_previous_slide_in_grafic_vneseniya_svedeniy(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.should_be_button_previous_slide(MainPageLocators.PREVIOUS_SLIDE_IN_GRAFIC_VNESENIYA_SVEDEDIY, 750)
    #
    #
    # @pytest.mark.dependency(depends=["grafic_vneseniya_svedeniy",
    #                                  "button_next_slide_in_grafic_vneseniya_svedeniy",
    #                                  "button_previous_slide_in_grafic_vneseniya_svedeniy"])
    # def test_should_be_picture_in_slide_in_grafic_vneseniya_svedeniy(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.should_be_picture_in_slide()
    #
    #
    # @pytest.mark.dependency(name="section_news")
    # def test_should_be_section_news(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.should_be_section_news()
    #
    #
    # @pytest.mark.dependency(depends=["section_news"])
    # def test_should_be_title_in_section_news(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.should_be_title_section()
    #
    #
    # @pytest.mark.dependency(depends=["section_news"])
    # def test_should_be_content_in_section_news(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.should_be_content()
    #
    #
    # @pytest.mark.dependency(depends=["section_news"])
    # def test_can_go_to_page_news_from_section_news(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     link = main_page.should_be_link_on_page_news()
    #     main_page.click(link)
    #     page_news = NewsPage(browser, browser.current_url)
    #     page_news.should_be_page_news()
    #
    #
    @pytest.mark.dependency(name="global_chart")
    def test_should_be_global_charts(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_slider(MainPageLocators.GLOBAL_CHARTS)
        TestMainPage.response_api_charts = main_page.can_get_data_global_charts()

    #
    # @pytest.mark.dependency(depends=["global_chart"])
    # def test_should_be_title_global_charts(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.should_be_title_for_slider(MainPageLocators.TITLE_GLOBAL_CHARTS,
    #                                          Const.title_global_charts)
    #
    #
    # @pytest.mark.dependency(depends=["global_chart"])
    # def test_should_be_17_slides_in_global_charts(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.should_be_slides(MainPageLocators.LIST_SLIDES_IN_GLOBAL_CHARTS, 17, 1360)
    #
    #
    # @pytest.mark.dependency(name="button_next_slide_in_global_charts", depends=["global_chart"])
    # def test_should_be_button_next_slide_in_global_charts(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.should_be_button_next_slide(MainPageLocators.NEXT_SLIDE_IN_GLOBAL_CHARTS, 1360)
    #
    #
    # @pytest.mark.dependency(name="button_previous_slide_in_global_charts", depends=["global_chart"])
    # def test_should_be_button_previous_slide_in_global_charts(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.should_be_button_previous_slide(MainPageLocators.PREVIOUS_SLIDE_IN_GLOBAL_CHARTS, 1360)
    #
    #
    #
    # @pytest.mark.dependency(depends=["global_chart", "button_next_slide_in_global_charts",
    #                                  "button_previous_slide_in_global_charts"])
    # def test_should_be_chart_in_slide_in_global_charts(self, browser):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.should_be_chart_in_slide()

    @pytest.fixture
    def api_charts(self):
        return TestMainPage.response_api_charts


    # @pytest.mark.dependency(depends=["global_chart"])
    # @pytest.mark.parametrize("chart_number", range(8), ids=[
    #     "in_summary_chart",
    #     "in_dissertations_chart",
    #     "in_niokr_chart",
    #     "in_rid_chart",
    #     "in_ikrbs_chart",
    #     "in_grants_chart",
    #     "in_scipubs_chart",
    #     "in_patents_chart",
    # ])
    # def test_should_be_legend_with_years_in_each_chart_of_global_chart(self, browser, api_charts, chart_number):
    #     main_page = MainPage(browser, browser.current_url)
    #     main_page.should_be_years_in_legend(api_charts, chart_number)

    def test_should_be_description_of_x_in_global_chart(self): # ПОДПИСЬ ГОДЫ
    def test_should_be_description_of_y_in_global_chart(self): # ПОДПИСЬ КОЛИЧЕСТВО

    # ТЕСТ НИЖЕ ГОТОВ
    @pytest.mark.dependency(depends=["global_chart"])
    @pytest.mark.parametrize("element_number", range(1,8), ids=[
        "in_dissertations_chart",
        "in_niokr_chart",
        "in_rid_chart",
        "in_ikrbs_chart",
        "in_grants_chart",
        "in_scipubs_chart",
        "in_patents_chart",
    ])
    def test_should_be_color_element_in_legend_of_summary_chart_of_global_chart(self, browser, api_charts, element_number):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_color_element_in_legend(api_charts, element_number)

    # ТЕСТ НИЖЕ НЕ ГОТОВ
    @pytest.mark.dependency(depends=["global_chart"])
    @pytest.mark.parametrize("element_number", range(1,8), ids=[
        "color_diss",
        "color_niokr",
        "color_rid",
        "color_ikrbs",
        "color_grant",
        "color_scipub",
        "color_patent",
    ])
    def test_should_be_color_element_in_legend_of_each_chart_of_global_chart(self, browser, api_charts, element_number):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_color_element_in_legend(api_charts, element_number)

    def test_can_click_on_element_in_legend # могу отключить отображение элементов в статистике
    # ДАЛЕЕ ТЕСТЫ - количество по годам для каждой сущности из первого слайда совпадают со значениями по годам с остальными графиками
    # количество по годам должно быть больше или равно тому что есть сейчас


