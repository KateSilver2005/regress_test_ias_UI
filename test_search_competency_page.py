import pytest
import time

from .pages.const_and_test_data import ConstCompetencyPage, Env
from .pages.login_page import LoginPage
from .pages.search_competency_page import SearchCompetencyPage



class TestSearchCompetency:

    response_api_map = None
    response_api_statistic = None

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, module_browser, request):
        self.login_link = Env.MAIN_LINK
        self.login_page = LoginPage(module_browser, self.login_link)
        self.login_page.open()
        self.login_page.log_in()
        self.login_page.should_be_authorized_user()
        self.competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
        self.search_bar = self.competency_page.find_search_bar()
        self.competency_page.enter_request(self.search_bar)
        '''Если после поиска по запросу ввести новый запрос, то мы не разлогиниваемся (две строки кода ниже закоменченны)'''
        # self.search_bar2 = self.competency_page.find_search_bar()
        # self.competency_page.enter_request_2(self.search_bar2)
        yield
        self.competency_page.logout()
        self.competency_page.should_not_be_authorized_user()


    @pytest.mark.smoke
    @pytest.mark.map
    @pytest.mark.dependency(name='map')
    def test_user_can_make_search_and_get_result_in_map(self, module_browser):
        competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
        competency_page.should_be_module_map()
        TestSearchCompetency.response_api_map = competency_page.should_be_content_map_is_not_null()


    @pytest.mark.map
    @pytest.fixture
    def api_map(self):
        return TestSearchCompetency.response_api_map
    #
    #
    # @pytest.mark.smoke
    # @pytest.mark.map
    # @pytest.mark.dependency(depends=["map"])
    # def test_should_be_content_map(self, module_browser, api_map):
    #     if api_map is None:
    #         pytest.skip("Тест пропущен, так как в модуле Карта отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_content_map()
    #
    #
    # @pytest.mark.dependency(depends=["map"])
    # @pytest.mark.map
    # def test_should_be_name_map_in_module_map(self, module_browser):
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_name_map()
    #
    #
    # @pytest.mark.dependency(depends=["map"])
    # @pytest.mark.map
    # def test_should_be_full_screen_fiture_in_module_map(self, module_browser):
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_full_screen_fiture()
    #
    #
    # @pytest.mark.dependency(depends=["map"])
    # @pytest.mark.map
    # def test_should_be_refresh_button_in_module_map(self, module_browser):
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_refresh_button()
    #
    #
    # @pytest.mark.dependency(name='zoomcontrol_body', depends=["map"])
    # @pytest.mark.map
    # def test_should_be_zoomcontrol_body_in_module_map(self, module_browser, api_map):
    #     if api_map is None:
    #         pytest.skip("Тест пропущен, так как в модуле Карта отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_zoomcontrol_body()
    #
    #
    # @pytest.mark.dependency(name='button_zoomcontrol_out', depends=["map"])
    # @pytest.mark.map
    # def test_should_be_button_zoomcontrol_out_in_module_map(self, module_browser, api_map):
    #     if api_map is None:
    #         pytest.skip("Тест пропущен, так как в модуле Карта отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_button_zoomcontrol_out()
    #
    #
    # @pytest.mark.dependency(name='button_zoomcontrol_in', depends=["map"])
    # @pytest.mark.map
    # def test_should_be_button_zoomcontrol_in_in_module_map(self, module_browser, api_map):
    #     if api_map is None:
    #         pytest.skip("Тест пропущен, так как в модуле Карта отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_button_zoomcontrol_in()
    #
    #
    # @pytest.mark.dependency(name='zoomcontrol_slider', depends=["map"])
    # @pytest.mark.map
    # def test_should_be_zoomcontrol_slider_in_module_map(self, module_browser, api_map):
    #     if api_map is None:
    #         pytest.skip("Тест пропущен, так как в модуле Карта отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_zoomcontrol_slider()
    #
    #
    # @pytest.mark.dependency(name='zoomcontrol_level', depends=["map"])
    # @pytest.mark.map
    # @pytest.mark.parametrize("num, level", ConstCompetencyPage.hints_zoomcontrol_level_in_map, ids=[
    #     "level_regions",
    #     "level_aglomirations",
    #     "level_towns"
    # ])
    # def test_should_be_zoomcontrol_levels_in_module_map(self, module_browser, num, level, api_map):
    #     if api_map is None:
    #         pytest.skip("Тест пропущен, так как в модуле Карта отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_zoomcontrol_levels(num, level)
    #
    #
    # @pytest.mark.dependency(depends=["zoomcontrol_slider", "zoomcontrol_level"])
    # @pytest.mark.map
    # @pytest.mark.parametrize("scale, num", ConstCompetencyPage.zoomcontrol_level_in_map, ids=[
    #     "scale_regions",
    #     "scale_aglomirations",
    #     "scale_towns"
    # ])
    # def test_should_be_change_zoom_in_module_map(self, module_browser, scale, num, api_map):
    #     if api_map is None:
    #         pytest.skip("Тест пропущен, так как в модуле Карта отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_change_zoom_in_module_map(scale, num)
    #
    #
    # @pytest.mark.smoke
    # @pytest.mark.dependency(depends=["map"])
    # @pytest.mark.map
    # def test_validate_response_map(self, module_browser, api_map):
    #     if api_map is None:
    #         pytest.skip("Тест пропущен, так как в модуле Карта отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.validate_response_map(api_map)


    @pytest.mark.smoke
    @pytest.mark.dependency(depends=["map"])
    @pytest.mark.map
    def test_can_open_raiting_of_each_region(self, module_browser, api_map):
        if api_map is None:
            pytest.skip("Тест пропущен, так как в модуле Карта отсутствуют данные")
        competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
        competency_page.can_open_legal_person_of_each_region(api_map)


    # @pytest.mark.smoke
    # @pytest.mark.statistic
    # @pytest.mark.dependency(name='statistic')
    # def test_user_can_make_search_and_get_result_in_statistic(self, module_browser):
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     show_content = competency_page.should_be_module_statistic()
    #     show_content.click()
    #     competency_page.should_be_content_statistic()
    #     TestSearchCompetency.response_api_statistic = competency_page.should_be_content_statistic_is_not_null()
    #
    #
    # @pytest.mark.statistic
    # @pytest.fixture
    # def api_statistic(self):
    #     return TestSearchCompetency.response_api_statistic


    # @pytest.mark.dependency(depends=["statistic"])
    # @pytest.mark.statistic
    # def test_should_be_name_statistic_in_module_statistic(self, module_browser):
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     quantity = competency_page.should_be_quantity_charts()
    #     competency_page.should_be_name_statistic(quantity)


    # @pytest.mark.dependency(depends=["statistic"])
    # @pytest.mark.statistic
    # def test_should_be_legends_charts_in_module_statistic(self, module_browser, api_statistic):
    #     if api_statistic is None:
    #         pytest.skip("Тест пропущен, так как в модуле Статистика отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     quantity = competency_page.should_be_quantity_charts()
    #     competency_page.should_be_legends_charts(quantity)


    # @pytest.mark.smoke
    # @pytest.mark.dependency(name="validate_schema", depends=["statistic"])
    # @pytest.mark.statistic
    # def test_validate_response_statistic(self, module_browser, api_statistic):
    #     if api_statistic is None:
    #         pytest.skip("Тест пропущен, так как в модуле Статистика отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.validate_response_statistic(api_statistic)


    # @pytest.mark.dependency(depends=["statistic", "validate_schema"])
    # @pytest.mark.statistic
    # @pytest.mark.parametrize("chart_num, expected_title", ConstCompetencyPage.titles_chart_in_statistic_in_competency_page, ids=[
    #     "activites",
    #     "total_money_NIOKR",
    #     "TOP-5_journals",
    #     "TOP-5_persons",
    #     "TOP-5_organizations"
    # ])
    # def test_should_be_title_of_chart(self, module_browser, api_statistic, chart_num, expected_title):
    #     if api_statistic is None:
    #         pytest.skip("Тест пропущен, так как в модуле Статистика отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_title_of_chart(api_statistic, chart_num, expected_title)
    #
    #
    #
    # @pytest.mark.dependency(depends=["statistic", "validate_schema"])
    # @pytest.mark.statistic
    # @pytest.mark.parametrize("num_chart, path_in_response, expected_name",
    #                          ConstCompetencyPage.name_aixis_of_charts_in_statistic_in_competency_page, ids=["activites-X-axis",
    #                                                                                           "activites-Y-axis",
    #                                                                                           "total_money_NIOKR-X-axis",
    #                                                                                           "total_money_NIOKR-Y-axis",
    #                                                                                           "TOP-5_journals-X-axis",
    #                                                                                           "TOP-5_persons-X-axis",
    #                                                                                           "TOP-5_organizations-X-axis"
    #                                                                                           ])
    # def test_should_be_name_of_axis_in_charts(self, module_browser, api_statistic, num_chart, path_in_response, expected_name):
    #     if api_statistic is None:
    #         pytest.skip("Тест пропущен, так как в модуле Статистика отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_name_of_axis_in_charts(api_statistic, num_chart, path_in_response, expected_name)


    # @pytest.mark.dependency(depends=["statistic", "validate_schema"])
    # @pytest.mark.statistic
    # @pytest.mark.parametrize("num_chart", [0,1], ids=["chart_activites", "chart_NIOKR_budget"])
    # def test_should_be_years(self, module_browser, api_statistic, num_chart):
    #     if api_statistic is None:
    #         pytest.skip("Тест пропущен, так как в модуле Статистика отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_years(api_statistic, num_chart)


    # @pytest.mark.dependency(depends=["statistic", "validate_schema"])
    # @pytest.mark.statistic
    # @pytest.mark.parametrize("num_chart, expected_names", ConstCompetencyPage.correct_name_entity_in_charts,
    #                          ids=["chart_activites", "chart_NIOKR_budget"])
    # def test_should_be_correct_name_entity(self, module_browser, api_statistic, num_chart, expected_names):
    #     if api_statistic is None:
    #         pytest.skip("Тест пропущен, так как в модуле Статистика отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_correct_name_entity(api_statistic, num_chart, expected_names)


    # @pytest.mark.dependency(depends=["statistic", "validate_schema"])
    # @pytest.mark.statistic
    # @pytest.mark.parametrize("num_chart, expected_color", ConstCompetencyPage.correct_color_entity_in_charts,
    #                          ids=["chart_activites", "chart_NIOKR_budget"])
    # def test_should_be_correct_color_entity(self, module_browser, api_statistic, num_chart, expected_color):
    #     if api_statistic is None:
    #         pytest.skip("Тест пропущен, так как в модуле Статистика отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_correct_color_entity(api_statistic, num_chart, expected_color)


    # @pytest.mark.dependency(name="correct_quantity_entity", depends=["statistic", "validate_schema"])
    # @pytest.mark.statistic
    # @pytest.mark.parametrize("num_chart", [0,1],
    #                          ids=["chart_activites", "chart_NIOKR_budget"])
    # def test_should_be_correct_quantity_entity(self, module_browser, api_statistic, num_chart):
    #     if api_statistic is None:
    #         pytest.skip("Тест пропущен, так как в модуле Статистика отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_correct_quantity_entity(api_statistic, num_chart)
    #
    #
    # @pytest.mark.dependency(depends=["statistic", "validate_schema", "correct_quantity_entity"])
    # @pytest.mark.statistic
    # @pytest.mark.parametrize("num_chart", [0,1],
    #                          ids=["chart_activites", "chart_NIOKR_budget"])
    # def test_should_be_quantity_entity_in_each_year(self, module_browser, api_statistic, num_chart):
    #     if api_statistic is None:
    #         pytest.skip("Тест пропущен, так как в модуле Статистика отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_quantity_entity_in_each_year(api_statistic, num_chart)


    # @pytest.mark.dependency(depends=["statistic", "validate_schema"])
    # @pytest.mark.statistic
    # @pytest.mark.parametrize("num_chart",range(2,5),
    #                          ids=["chart_top_journals", "chart_top_persons", "chart_top_organizations"])
    # def test_should_be_name_in_legend(self, module_browser, api_statistic, num_chart):
    #     if api_statistic is None:
    #         pytest.skip("Тест пропущен, так как в модуле Статистика отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_should_be_name_in_legend(api_statistic, num_chart)


    # @pytest.mark.dependency(depends=["statistic", "validate_schema"])
    # @pytest.mark.statistic
    # @pytest.mark.parametrize("num_chart",range(2,5),
    #                          ids=["chart_top_journals", "chart_top_persons", "chart_top_organizations"])
    # def test_should_be_quantity_of_element(self, module_browser, api_statistic, num_chart):
    #     if api_statistic is None:
    #         pytest.skip("Тест пропущен, так как в модуле Статистика отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_quantity_of_element(api_statistic, num_chart)


    # @pytest.mark.dependency(depends=["statistic", "validate_schema"])
    # @pytest.mark.statistic
    # @pytest.mark.parametrize("num_chart",range(2,5),
    #                          ids=["chart_top_journals", "chart_top_persons", "chart_top_organizations"])
    # def test_should_be_color_of_element(self, module_browser, api_statistic, num_chart):
    #     if api_statistic is None:
    #         pytest.skip("Тест пропущен, так как в модуле Статистика отсутствуют данные")
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_color_of_element(api_statistic, num_chart)


    #
    #
    # @pytest.mark.smoke
    # def test_user_can_make_search_and_get_result_in_graph_ak(self, module_browser):
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     show_content = competency_page.should_be_module_graph_ak()
    #     show_content.click()
    #     competency_page.should_be_content_graph_ak()
    #
    #
    # @pytest.mark.smoke
    # def test_user_can_make_search_and_get_result_in_graph_ko(self, module_browser):
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     show_content = competency_page.should_be_module_graph_ko()
    #     show_content.click()
    #     competency_page.should_be_content_graph_ko()
    #
    #
    # @pytest.mark.smoke
    # def test_user_can_make_search_and_get_result_in_rating(self, module_browser):
    #     competency_page = SearchCompetencyPage(module_browser, module_browser.current_url)
    #     competency_page.should_be_module_rating()
