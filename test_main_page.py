import time

import pytest

from .pages.main_page import MainPage
from .pages.locators import MainPageLocators, AdvancedSearch
from .pages.const_and_test_data import Const, Env, ConstMainPage
from .pages.login_page import LoginPage
from .pages.release_page import PageRelease
from .pages.faq_page import PageFaq
from .pages.base_page import Header, Footer
from .pages.help_page import PageHelp
from .pages.analitic_page import PageAnalitic
from .pages.services_page import PageServices
from .pages.mycompany_page import PageInfoAboutProvider
from .pages.news_page import NewsPage


@pytest.mark.main_page_header_footer
class TestMainPageHeaderFooter:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_link = Env.MAIN_LINK
        self.login_page = LoginPage(browser, self.login_link)
        self.login_page.open()
        self.login_page.log_in()
        self.login_page.should_be_authorized_user()
        self.main_page = MainPage(browser, browser.current_url)
        yield
        self.main_page.logout()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.should_not_be_authorized_user()

    # header
    def test_can_click_logo_in_header(self, browser):
        main_page = Header(browser, browser.current_url)
        logo_in_header = main_page.should_be_logo_in_header()
        main_page.click_logo_in_header(logo_in_header)

    def test_should_be_title_text_in_header(self, browser):
        main_page = Header(browser, browser.current_url)
        main_page.should_be_title_text_in_header()

    def test_should_be_description_in_header(self, browser):
        main_page = Header(browser, browser.current_url)
        main_page.should_be_description_in_header()

    def test_can_go_to_version_unseeing_page(self, browser):
        main_page = Header(browser, browser.current_url)
        button_for_version_unseeing = main_page.should_be_button_for_version_unseeing()
        main_page.go_to_version_unseeing_page(button_for_version_unseeing)

    def test_can_open_up_menu_in_lk(self, browser):
        main_page = Header(browser, browser.current_url)
        button_in_lk = main_page.should_be_button_in_lk()
        main_page.open_up_menu_in_lk(button_in_lk)

    def test_should_be_module_with_hot_news(self, browser):
        hot_news_module = Header(browser, browser.current_url)
        hot_news_module.should_be_module_with_hot_news()

        # footer
    def test_should_be_logo_csp_in_footer(self, browser):
        main_page = Footer(browser, browser.current_url)
        main_page.should_be_logo_csp_in_footer()


    def test_should_be_text_csp_in_footer(self, browser):
        main_page = Footer(browser, browser.current_url)
        main_page.should_be_text_csp_in_footer()


    def test_should_be_logo_fmba_in_footer(self, browser):
        main_page = Footer(browser, browser.current_url)
        main_page.should_be_logo_fmba_in_footer()


    def test_should_be_text_fmba_in_footer(self, browser):
        main_page = Footer(browser, browser.current_url)
        main_page.should_be_text_fmba_in_footer()


    def test_should_be_inscription_in_footer(self, browser):
        main_page = Footer(browser, browser.current_url)
        main_page.should_be_title_and_inscription_in_footer()


    def test_can_go_to_realese_page(self, browser):
        main_page = Footer(browser, browser.current_url)
        link = main_page.should_be_link_page_release()
        link.click()
        release_page = PageRelease(browser, browser.current_url)
        release_page.should_be_page_release()


    def test_can_write_mail_to_support(self, browser):
        main_page = Footer(browser, browser.current_url)
        link = main_page.should_be_link_mail_support()
        main_page.should_be_true_email(link)


    def test_can_go_to_faq_page(self, browser):
        main_page = Footer(browser, browser.current_url)
        link = main_page.should_be_link_faq()
        link.click()
        faq_page = PageFaq(browser, browser.current_url)
        faq_page.should_be_page_faq()


    def test_can_go_to_help_page(self, browser):
        main_page = Footer(browser, browser.current_url)
        link = main_page.should_be_link_help()
        link.click()
        help_page = PageHelp(browser, browser.current_url)
        help_page.should_be_page_help()



class TestMainPage:

    response_api_charts = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_link = Env.MAIN_LINK
        self.login_page = LoginPage(browser, self.login_link)
        self.login_page.open()
        self.login_page.log_in()
        self.login_page.should_be_authorized_user()
        self.main_page = MainPage(browser, browser.current_url)
        yield
        self.main_page.logout()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.should_not_be_authorized_user()


    @pytest.mark.smoke
    def test_can_go_to_analitic(self, browser):
        main_page = MainPage(browser, browser.current_url)
        button_analitic = main_page.should_be_button_analitic()
        button_analitic.click()
        analitic_page = PageAnalitic(browser, browser.current_url)
        analitic_page.should_be_page_analitic()

    @pytest.mark.smoke
    def test_can_go_to_services(self, browser):
        main_page = MainPage(browser, browser.current_url)
        button_in_services = main_page.should_be_button_in_services()
        button_in_services.click()
        services_page = PageServices(browser, browser.current_url)
        services_page.should_be_page_services()


    @pytest.mark.smoke
    def test_can_go_to_info_about_provider(self, browser):
        main_page = MainPage(browser, browser.current_url)
        info_about_provider = main_page.should_be_button_info_about_infoprovider()
        info_about_provider.click()
        info_about_provider_page = PageInfoAboutProvider(browser, browser.current_url)
        info_about_provider_page.should_be_page_info_about_provider()


    @pytest.mark.smoke
    def test_should_be_title_lk(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_title_lk()


    # переключатель поисков: по компетенциям, документам, ученым, организациям
    @pytest.mark.smoke
    @pytest.mark.dependency(name="tabs_of_search")
    def test_should_be_tabs_of_search(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_tabs_search()


    @pytest.mark.smoke
    @pytest.mark.dependency(name="each_tabs_of_search", depends=["tabs_of_search"])
    @pytest.mark.parametrize("locator", MainPageLocators.TABS, ids=[
        "tab_competency",
        "tab_doc",
        "tab_org",
        "tab_person"
    ])
    def test_should_be_tabs(self, locator, browser):
        main_page = MainPage(browser, browser.current_url)
        tab = main_page.should_be_tabs(locator)
        main_page.click(tab)
        main_page.should_be_active(tab)


    @pytest.mark.smoke
    @pytest.mark.dependency(name="search_area_in_tabs", depends=["tabs_of_search", "each_tabs_of_search"])
    @pytest.mark.parametrize("locator, placeholder", MainPageLocators.PLACEHOLDERS_IN_SEARCH_AREA_TABS, ids=[
        "in_tab_competency",
        "in_tab_doc",
        "in_tab_org",
        "in_tab_person"
    ])
    def test_should_be_search_area_with_placeholder_of_tabs(self, locator, placeholder, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.click(locator)
        search_area = main_page.should_be_search_area()
        main_page.should_be_placeholder(search_area, placeholder)


    @pytest.mark.smoke
    @pytest.mark.dependency(depends=["tabs_of_search", "search_area_in_tabs", "each_tabs_of_search"])
    @pytest.mark.parametrize("locator", MainPageLocators.TABS, ids=[
        "in_tab_competency",
        "in_tab_doc",
        "in_tab_org",
        "in_tab_person"
    ])
    def test_should_be_clear_button_in_search_area_of_tabs(self, locator, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.click(locator)
        main_page.should_be_clear_button()


    @pytest.mark.smoke
    @pytest.mark.dependency(depends=["tabs_of_search", "search_area_in_tabs", "each_tabs_of_search"])
    @pytest.mark.parametrize("locator", MainPageLocators.TABS, ids=[
        "in_tab_competency",
        "in_tab_doc",
        "in_tab_org",
        "in_tab_person"
    ])
    def test_should_be_button_search_in_search_area_of_tabs(self, locator, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.click(locator)
        search_button = main_page.should_be_button_search()
        main_page.should_be_element_is_disabled(search_button)


    @pytest.mark.smoke
    @pytest.mark.dependency(name='advanced_search_filter', depends=["tabs_of_search", "search_area_in_tabs", "each_tabs_of_search"])
    @pytest.mark.parametrize("tab", MainPageLocators.TABS[:2], ids=[
        "in_tab_competency",
        "in_tab_doc",
    ])
    def test_should_be_advanced_search_filter_in_search_area_of_tabs(self, tab, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.click(tab)
        main_page.should_be_advanced_search_button()
        main_page.can_click_on_advanced_search_button()



    @pytest.mark.smoke
    @pytest.mark.dependency(depends=["tabs_of_search", "each_tabs_of_search", "advanced_search_filter"])
    @pytest.mark.parametrize("tab, checkbox, label, label_text", AdvancedSearch.FILTERS_IN_ADVANCED_SEARCH, ids=[
        "in_tab_competency_checkbox_synonym_and_label",
        "in_tab_competency_checkbox_fulltext_and_label",
        "in_tab_competency_checkbox_distance_and_label",
        "in_tab_doc_checkbox_synonym_and_label",
        "in_tab_doc_checkbox_fulltext_and_label",
        "in_tab_doc_checkbox_distance_and_label"
    ])
    def test_should_be_filters_in_advanced_search_of_tabs(self, tab, checkbox, label, label_text, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.click(tab)
        main_page.can_click_on_advanced_search_button()
        main_page.should_be_checkbox(checkbox)
        main_page.should_be_label(label, label_text)


    @pytest.mark.smoke
    @pytest.mark.dependency(depends=["tabs_of_search", "each_tabs_of_search", "advanced_search_filter"])
    @pytest.mark.parametrize("tab, checkbox, dependent_checkbox", AdvancedSearch.CHECKBOX_SYNONYM, ids=[
        "in_tab_competency",
        "in_tab_doc"
    ])
    def test_can_click_on_checkbox_synonym_in_advanced_search_of_tabs_and_checkbox_distance_is_disabled(self, tab, checkbox, dependent_checkbox, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.click(tab)
        main_page.can_click_on_advanced_search_button()
        checkbox_enabled = main_page.should_be_checkbox(dependent_checkbox)
        main_page.scroll_and_click(checkbox)
        main_page.should_be_element_is_disabled(checkbox_enabled, dependent_checkbox)


    @pytest.mark.smoke
    @pytest.mark.dependency(depends=["tabs_of_search", "each_tabs_of_search", "advanced_search_filter"])
    @pytest.mark.parametrize("tab, checkbox", AdvancedSearch.CHECKBOX_FULLTEXT, ids=[
        "in_tab_competency",
        "in_tab_doc"
    ])
    def test_can_click_on_checkbox_fulltext_in_advanced_search_of_tabs(self, tab, checkbox, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.click(tab)
        main_page.can_click_on_advanced_search_button()
        main_page.scroll_and_click(checkbox)


    @pytest.mark.smoke
    @pytest.mark.dependency(depends=["tabs_of_search", "each_tabs_of_search", "advanced_search_filter"])
    @pytest.mark.parametrize("tab, distance_checkbox, synonym_checkbox, range_distance, pixsels, steps", AdvancedSearch.CHECKBOX_DISTANCE, ids=[
        "in_tab_competency_on_checkbox_distance_change_distance_0_and_checkbox_synonym_is_disabled",
        "in_tab_competency_on_checkbox_distance_change_distance_1_and_checkbox_synonym_is_disabled",
        "in_tab_competency_on_checkbox_distance_change_distance_2_and_checkbox_synonym_is_disabled",
        "in_tab_competency_on_checkbox_distance_change_distance_3_and_checkbox_synonym_is_disabled",
        "in_tab_competency_on_checkbox_distance_change_distance_4_and_checkbox_synonym_is_disabled",
        "in_tab_competency_on_checkbox_distance_change_distance_5_and_checkbox_synonym_is_disabled",
        "in_tab_competency_on_checkbox_distance_change_distance_6_and_checkbox_synonym_is_disabled",
        "in_tab_competency_on_checkbox_distance_change_distance_7_and_checkbox_synonym_is_disabled",
        "in_tab_competency_on_checkbox_distance_change_distance_8_and_checkbox_synonym_is_disabled",
        "in_tab_competency_on_checkbox_distance_change_distance_9_and_checkbox_synonym_is_disabled",
        "in_tab_competency_on_checkbox_distance_change_distance_10_and_checkbox_synonym_is_disabled",
        "in_tab_doc_on_checkbox_distance_change_distance_0_and_checkbox_synonym_is_disabled",
        "in_tab_doc_on_checkbox_distance_change_distance_1_and_checkbox_synonym_is_disabled",
        "in_tab_doc_on_checkbox_distance_change_distance_2_and_checkbox_synonym_is_disabled",
        "in_tab_doc_on_checkbox_distance_change_distance_3_and_checkbox_synonym_is_disabled",
        "in_tab_doc_on_checkbox_distance_change_distance_4_and_checkbox_synonym_is_disabled",
        "in_tab_doc_on_checkbox_distance_change_distance_5_and_checkbox_synonym_is_disabled",
        "in_tab_doc_on_checkbox_distance_change_distance_6_and_checkbox_synonym_is_disabled",
        "in_tab_doc_on_checkbox_distance_change_distance_7_and_checkbox_synonym_is_disabled",
        "in_tab_doc_on_checkbox_distance_change_distance_8_and_checkbox_synonym_is_disabled",
        "in_tab_doc_on_checkbox_distance_change_distance_9_and_checkbox_synonym_is_disabled",
        "in_tab_doc_on_checkbox_distance_change_distance_10_and_checkbox_synonym_is_disabled"
    ])
    def test_can_click_on_checkbox_distance_in_advanced_search_of_tabs(self, tab, distance_checkbox, synonym_checkbox,
                                                                       range_distance, pixsels, steps, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.click(tab)
        main_page.can_click_on_advanced_search_button()
        checkbox_enabled = main_page.should_be_checkbox(synonym_checkbox)
        main_page.scroll_and_click(distance_checkbox)
        main_page.should_be_element_is_disabled(checkbox_enabled, synonym_checkbox)
        element = main_page.should_be_range_distance(range_distance)
        main_page.can_change_distance(element, pixsels, range_distance, browser, steps)
        main_page.should_be_label_range_distance(steps)


    @pytest.mark.smoke
    @pytest.mark.dependency(depends=["tabs_of_search", "each_tabs_of_search", "advanced_search_filter"])
    @pytest.mark.parametrize("tab, checkbox1, checkbox2, dependent_checkbox",
                             AdvancedSearch.CHECKBOX_SYNONYM_AND_FULLTEXT, ids=[
        "in_tab_competency_on_checkbox_synonym_and_fulltext",
        "in_tab_doc_on_checkbox_synonym_and_fulltext",
        "in_tab_competency_on_checkbox_fulltext_and_distance",
        "in_tab_doc_on_checkbox_fulltext_and_distance",
    ])
    def test_can_click_on_two_checkboxes_in_advanced_search_of_tabs(self, tab, checkbox1, checkbox2,
                                                                    dependent_checkbox, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.click(tab)
        main_page.can_click_on_advanced_search_button()
        checkbox_enabled = main_page.should_be_checkbox(dependent_checkbox)
        main_page.scroll_and_click(checkbox1)
        main_page.scroll_and_click(checkbox2)
        main_page.should_be_element_is_disabled(checkbox_enabled, dependent_checkbox)


    @pytest.mark.smoke
    @pytest.mark.dependency(name="grafic_vneseniya_svedeniy")
    def test_should_be_grafic_vneseniya_svedeniy(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_slider(MainPageLocators.GRAFIC_VNESENIYA_SVEDEDIY, 750)


    @pytest.mark.grafic_vneseniya_svedeniy
    @pytest.mark.dependency(depends=["grafic_vneseniya_svedeniy"])
    def test_should_be_title_grafic_vneseniya_svedeniy(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_title_for_block(MainPageLocators.TITLE_GRAFIC_VNESENIYA_SVEDEDIY,
                                             ConstMainPage.title_grafic_vneseniya_svedeniy, 750)


    @pytest.mark.grafic_vneseniya_svedeniy
    @pytest.mark.dependency(depends=["grafic_vneseniya_svedeniy"])
    def test_should_be_12_slides_in_grafic_vneseniya_svedeniy(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_slides(MainPageLocators.LIST_SLIDES_IN_GRAFIC_VNESENIYA_SVEDEDIY, 12, 750)


    @pytest.mark.grafic_vneseniya_svedeniy
    @pytest.mark.dependency(name="button_next_slide_in_grafic_vneseniya_svedeniy", depends=["grafic_vneseniya_svedeniy"])
    def test_should_be_button_next_slide_in_grafic_vneseniya_svedeniy(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_button_next_slide(MainPageLocators.NEXT_SLIDE_IN_GRAFIC_VNESENIYA_SVEDEDIY, 750)


    @pytest.mark.grafic_vneseniya_svedeniy
    @pytest.mark.dependency(name="button_previous_slide_in_grafic_vneseniya_svedeniy", depends=["grafic_vneseniya_svedeniy"])
    def test_should_be_button_previous_slide_in_grafic_vneseniya_svedeniy(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_button_previous_slide(MainPageLocators.PREVIOUS_SLIDE_IN_GRAFIC_VNESENIYA_SVEDEDIY, 750)


    @pytest.mark.grafic_vneseniya_svedeniy
    @pytest.mark.dependency(depends=["grafic_vneseniya_svedeniy",
                                     "button_next_slide_in_grafic_vneseniya_svedeniy",
                                     "button_previous_slide_in_grafic_vneseniya_svedeniy"])
    def test_should_be_picture_in_slide_in_grafic_vneseniya_svedeniy(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_picture_in_slide()


    @pytest.mark.section_news
    @pytest.mark.dependency(name="section_news")
    def test_should_be_section_news(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_section_news()


    @pytest.mark.section_news
    @pytest.mark.dependency(depends=["section_news"])
    def test_should_be_title_in_section_news(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_title_section()


    @pytest.mark.section_news
    @pytest.mark.dependency(depends=["section_news"])
    def test_should_be_content_in_section_news(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_content()


    @pytest.mark.section_news
    @pytest.mark.dependency(depends=["section_news"])
    def test_can_go_to_page_news_from_section_news(self, browser):
        main_page = MainPage(browser, browser.current_url)
        link = main_page.should_be_link_on_page_news()
        main_page.click(link)
        page_news = NewsPage(browser, browser.current_url)
        page_news.should_be_page_news()


    @pytest.mark.global_charts
    @pytest.mark.dependency(name="global_chart")
    def test_should_be_global_charts(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_slider(MainPageLocators.GLOBAL_CHARTS, 1360)
        TestMainPage.response_api_charts = main_page.can_get_data_global_charts()


    @pytest.mark.global_charts
    @pytest.mark.dependency(depends=["global_chart"])
    def test_should_be_title_global_charts(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_title_for_block(MainPageLocators.TITLE_GLOBAL_CHARTS,
                                             ConstMainPage.title_global_charts, 1360)


    @pytest.mark.global_charts
    @pytest.mark.dependency(depends=["global_chart"])
    def test_should_be_17_slides_in_global_charts(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_slides(MainPageLocators.LIST_SLIDES_IN_GLOBAL_CHARTS, 17, 1360)


    @pytest.mark.global_charts
    @pytest.mark.dependency(name="button_next_slide_in_global_charts", depends=["global_chart"])
    def test_should_be_button_next_slide_in_global_charts(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_button_next_slide(MainPageLocators.NEXT_SLIDE_IN_GLOBAL_CHARTS, 1360)


    @pytest.mark.global_charts
    @pytest.mark.dependency(name="button_previous_slide_in_global_charts", depends=["global_chart"])
    def test_should_be_button_previous_slide_in_global_charts(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_button_previous_slide(MainPageLocators.PREVIOUS_SLIDE_IN_GLOBAL_CHARTS, 1360)


    @pytest.mark.global_charts
    @pytest.mark.dependency(name="chart_in_slide_in_global_charts",
                            depends=["global_chart", "button_next_slide_in_global_charts",
                                     "button_previous_slide_in_global_charts"])
    def test_should_be_chart_in_slide_in_global_charts(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_chart_in_slide()


    @pytest.mark.global_charts
    @pytest.fixture
    def api_charts(self):
        return TestMainPage.response_api_charts


    @pytest.mark.global_charts
    @pytest.mark.dependency(depends=["global_chart"])
    @pytest.mark.parametrize("chart_number, axis, expected_text",
                             [(i, axis, 'Годы' if axis == 'x' else 'Количество') for i in range(8) for axis in ['x', 'y']],
                             ids=[
                                 'in_summary_chart_x-axis', 'in_summary_chart_y-axis',
                                 'in_dissertations_chart_x-axis', 'in_dissertations_chart_y-axis',
                                 'in_niokr_chart_x-axis', 'in_niokr_chart_y-axis',
                                 'in_rid_chart_x-axis', 'in_rid_chart_y-axis',
                                 'in_ikrbs_chart_x-axis', 'in_ikrbs_chart_y-axis',
                                 'in_grants_chart_x-axis', 'in_grants_chart_y-axis',
                                 'in_scipubs_chart_x-axis', 'in_scipubs_chart_y-axis',
                                 'in_patents_chart_x-axis', 'in_patents_chart_y-axis',
                             ])
    def test_should_be_title_of_axes_in_global_chart(self, browser, api_charts, chart_number, axis, expected_text):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_title_of_axes_in_legend(api_charts, chart_number, axis, expected_text)


    @pytest.mark.global_charts
    @pytest.mark.dependency(depends=["global_chart"])
    @pytest.mark.parametrize("chart_number", range(8), ids=[
        "in_summary_chart",
        "in_dissertations_chart",
        "in_niokr_chart",
        "in_rid_chart",
        "in_ikrbs_chart",
        "in_grants_chart",
        "in_scipubs_chart",
        "in_patents_chart",
    ])
    def test_should_be_legend_with_years_in_each_chart_of_global_chart(self, browser, api_charts, chart_number):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_years_in_legend(api_charts, chart_number)


    @pytest.mark.global_charts
    @pytest.mark.dependency(depends=["global_chart", "chart_in_slide_in_global_charts"])
    @pytest.mark.parametrize(
        "chart_number_api, element_number_api, chart_number_css, element_number_css",
        [(0, i, 0, i + 1) for i in range(7)] +
        [(i, 0, i, 1) for i in range(1, 8)],
        ids=[
        "dissertations_color_in_summary_chart",
        "niokr_color_in_summary_chart",
        "rid_color_in_summary_chart",
        "ikrbs_color_in_summary_chart",
        "grants_color_in_summary_chart",
        "scipubs_color_in_summary_chart",
        "patents_color_in_summary_chart",
        "color_in_dissertations_chart",
        "color_in_niokr_chart",
        "color_in_rid_chart",
        "color_in_ikrbs_chart",
        "color_in_grants_chart",
        "color_in_scipubs_chart",
        "color_in_patents_chart",
    ])
    def test_should_be_color_element_in_legend_for_each_chart_of_global_chart(self, browser, api_charts,
                                                                                chart_number_api, element_number_api,
                                                                                chart_number_css, element_number_css):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_color_element_in_legend(api_charts, chart_number_api, element_number_api,
                                                    chart_number_css, element_number_css)


    @pytest.mark.global_charts
    @pytest.mark.dependency(name='title_element_in_legend_for_each_chart_of_global_chart', depends=["global_chart", "chart_in_slide_in_global_charts"])
    @pytest.mark.parametrize(
        "chart_number_css, element_number_css",
        [(0, i + 1) for i in range(7)] +
        [(i, 1) for i in range(1, 8)],
        ids=[
        "dissertations_title_in_summary_chart",
        "niokr_title_in_summary_chart",
        "rid_title_in_summary_chart",
        "ikrbs_title_in_summary_chart",
        "grants_title_in_summary_chart",
        "scipubs_title_in_summary_chart",
        "patents_title_in_summary_chart",
        "title_in_dissertations_chart",
        "title_in_niokr_chart",
        "title_in_rid_chart",
        "title_in_ikrbs_chart",
        "title_in_grants_chart",
        "title_in_scipubs_chart",
        "title_in_patents_chart",
    ])
    def test_should_be_title_element_in_legend_for_each_chart_of_global_chart(self, browser, chart_number_css,
                                                                              element_number_css):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_title_element_in_legend(chart_number_css, element_number_css)


    @pytest.mark.global_charts
    @pytest.mark.dependency(depends=["title_element_in_legend_for_each_chart_of_global_chart"])
    @pytest.mark.parametrize(
        "chart_number_css, element_number_css",
        [(0, i + 1) for i in range(7)]+
        [(i, 1) for i in range(1, 8)],
        ids=[
        "deactivate_dissertations_in_summary_chart",
        "deactivate_niokr_in_summary_chart",
        "deactivate_rid_in_summary_chart",
        "deactivate_ikrbs_in_summary_chart",
        "deactivate_grants_in_summary_chart",
        "deactivate_scipubs_in_summary_chart",
        "deactivate_patents_in_summary_chart",
        "deactivate_element_in_dissertations_chart",
        "deactivate_element_in_niokr_chart",
        "deactivate_element_in_rid_chart",
        "deactivate_element_in_ikrbs_chart",
        "deactivate_element_in_grants_chart",
        "deactivate_element_in_scipubs_chart",
        "deactivate_element_in_patents_chart",
    ])
    def test_in_global_chart_can_not_show_data_of_element_in_global_chart_and_deactivate_element_in_legend(self, browser, chart_number_css, element_number_css):
        main_page = MainPage(browser, browser.current_url)
        main_page.deactivate_element_in_legend(chart_number_css, element_number_css)


    @pytest.mark.global_charts
    @pytest.mark.dependency(depends=["global_chart"])
    @pytest.mark.parametrize(
        "num_summary_chart, num_element_summary_chart, num_single_chart, num_element_single_chart",
        [(0, 0, 1, 0), (0, 1, 2, 0), (0, 2, 3, 0), (0, 3, 4, 0), (0, 4, 5, 0), (0, 5, 6, 0), (0, 6, 7, 0)],
        ids=[
        "count_dissertations",
        "count_niokr",
        "count_rid",
        "count_ikrbs",
        "count_grants",
        "count_scipubs",
        "count_patents"
    ])
    def test_in_global_chart_should_be_match_of_count_of_elements_in_summary_chart_with_count_of_element_in_single_chart(self, browser,
                                                                                                         api_charts,
                                                                                                         num_summary_chart,
                                                                                                         num_element_summary_chart,
                                                                                                         num_single_chart,
                                                                                                         num_element_single_chart):
        main_page = MainPage(browser, browser.current_url)
        main_page.match_of_count_in_api_charts(api_charts, num_summary_chart,
                                               num_element_summary_chart, num_single_chart, num_element_single_chart)


    @pytest.mark.global_charts
    @pytest.mark.dependency(depends=["global_chart"])
    @pytest.mark.parametrize(
        "index, element",
        [(0, "Диссертации"), (1, "НИОКР"), (2, "РИД"), (3, "ИКРБС"), (4, "Гранты РНФ"), (5, "Публикации"), (6, "Патенты")],
        ids=[
        "dissertations",
        "niokr",
        "rid",
        "ikrbs",
        "grants",
        "scipubs",
        "patents"
        ])
    def test_should_be_no_regress_in_count_element_for_each_year_in_global_chart(self, browser, api_charts, index, element):
        main_page = MainPage(browser, browser.current_url)
        main_page.no_regress_in_count_element_for_each_year_in_global_chart(api_charts, index, element)


    @pytest.mark.info_for_users
    @pytest.mark.dependency(name="info_for_users")
    def test_should_be_info_for_users(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_info_for_users(MainPageLocators.INFO_FOR_USERS)


    @pytest.mark.info_for_users
    @pytest.mark.dependency(depends=["info_for_users"])
    def test_should_be_title_info_for_users(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_title_for_block(MainPageLocators.TITLE_INFO_FOR_USERS,
                                             ConstMainPage.title_info_users, 1599.75)


    @pytest.mark.info_for_users
    @pytest.mark.dependency(name='elements_in_info_for_users', depends=["info_for_users"])
    @pytest.mark.parametrize('num_element', range(1, 17),
                             ids=[
                                 'Elibrary',
                                 'Pubmed',
                                 'PMC',
                                 'Rosrid',
                                 'Yandex Patents',
                                 'CKP_USU',
                                 'RNF',
                                 'Scopus',
                                 'RFFI',
                                 'EIS Zakupki',
                                 'Registry of medical drugs ',
                                 'United registry licenses',
                                 'Clinical research',
                                 'Google Academy',
                                 'Google Patents',
                                 'Web of Science'])
    def test_should_be_elements_in_info_for_users(self, browser, num_element):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_elements(num_element)



    @pytest.mark.info_for_users
    @pytest.mark.dependency(depends=["info_for_users", "elements_in_info_for_users"])
    @pytest.mark.parametrize('num_element, image', zip(list(range(1, 17)), ConstMainPage.images_in_info_for_users,),
                             ids=[
                                 'Elibrary',
                                 'Pubmed',
                                 'PMC',
                                 'Rosrid',
                                 'Yandex Patents',
                                 'CKP_USU',
                                 'RNF',
                                 'Scopus',
                                 'RFFI',
                                 'EIS Zakupki',
                                 'Registry of medical drugs ',
                                 'United registry licenses',
                                 'Clinical research',
                                 'Google Academy',
                                 'Google Patents',
                                 'Web of Science'])
    def test_should_be_icon_of_elements_in_info_for_users(self, browser, num_element, image):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_icon_of_elements(num_element, image)


    @pytest.mark.info_for_users
    @pytest.mark.dependency(depends=["info_for_users", "elements_in_info_for_users"])
    @pytest.mark.parametrize('num_element, expected_title', zip(list(range(1, 17)), ConstMainPage.titles_in_info_for_users),
                             ids=[
                                 'Elibrary',
                                 'Pubmed',
                                 'PMC',
                                 'Rosrid',
                                 'Yandex Patents',
                                 'CKP_USU',
                                 'RNF',
                                 'Scopus',
                                 'RFFI',
                                 'EIS Zakupki',
                                 'Registry of medical drugs ',
                                 'United registry licenses',
                                 'Clinical research',
                                 'Google Academy',
                                 'Google Patents',
                                 'Web of Science'])
    def test_should_be_title_of_elements_in_info_for_users(self, browser, num_element, expected_title):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_title_of_elements(num_element, expected_title)


    @pytest.mark.info_for_users
    @pytest.mark.dependency(depends=["info_for_users", "elements_in_info_for_users"])
    @pytest.mark.parametrize('num_element, expected_url', zip(list(range(1, 17)), ConstMainPage.urls_in_info_for_users),
                             ids=[
                                 'Elibrary',
                                 'Pubmed',
                                 'PMC',
                                 'Rosrid',
                                 'Yandex Patents',
                                 'CKP_USU',
                                 'RNF',
                                 'Scopus',
                                 'RFFI',
                                 'EIS Zakupki',
                                 'Registry of medical drugs ',
                                 'United registry licenses',
                                 'Clinical research',
                                 'Google Academy',
                                 'Google Patents',
                                 'Web of Science'])
    def test_should_be_page_official_of_element_in_info_for_users(self, browser, num_element, expected_url):
        main_page = MainPage(browser, browser.current_url)
        ias_page = browser.current_window_handle
        link = main_page.should_be_link_to_site_official(num_element)
        link.click()
        site_official = [window for window in browser.window_handles if window != ias_page][0]
        browser.switch_to.window(site_official)
        source_page = MainPage(browser, browser.current_url)
        source_page.should_be_page_official(expected_url, ias_page)


    @pytest.mark.info_for_users
    @pytest.mark.dependency(depends=["info_for_users", "elements_in_info_for_users"])
    @pytest.mark.parametrize('num_element, total_scipubs', zip([1, 2, 3, 8], ConstMainPage.total_scipubs_in_info_for_users),
                             ids=['Elibrary',
                                 'Pubmed',
                                 'PMC',
                                 'Scopus'])
    def test_should_be_description_and_total_sci_pubs_in_info_for_users(self, browser, num_element, total_scipubs):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_total_scipubs(num_element, total_scipubs)
        main_page.should_be_description_scipubs(num_element)


    @pytest.mark.info_for_users
    @pytest.mark.dependency(depends=["info_for_users", "elements_in_info_for_users"])
    def test_should_be_description_and_total_rosrid(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_total_rosrid()
        main_page.should_be_description_rosrid()


    @pytest.mark.info_for_users
    @pytest.mark.dependency(depends=["info_for_users", "elements_in_info_for_users"])
    def test_should_be_description_and_total_yandex_patents(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_total_patents()
        main_page.should_be_description_patents()


    @pytest.mark.info_for_users
    @pytest.mark.dependency(depends=["info_for_users", "elements_in_info_for_users"])
    def test_should_be_description_and_total_ckp_usu(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_total_ckp_usu()
        main_page.should_be_description_ckp_usu()


    @pytest.mark.info_for_users
    @pytest.mark.dependency(depends=["info_for_users", "elements_in_info_for_users"])
    def test_should_be_description_and_total_grants(self, browser):
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_total_grants()
        main_page.should_be_description_grants()

