import os
import time
from selenium.webdriver.support import expected_conditions as EC

import requests
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import SearchCompetencyPageLocators, MapLocators, StatisticLocators
from .const_and_test_data import TestData, ConstCompetencyPage, ConstMainPage
from .endpoints import Endpoints
from .for_check_response_api import Map, Statistic


class SearchCompetencyPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(SearchCompetencyPage, self).__init__(*args, **kwargs)
        self.cert_path = os.path.join(os.path.dirname(__file__), '../cert/for_prod_stage.crt')

    def find_search_bar(self):
        search_bar = self.find_element(*SearchCompetencyPageLocators.SEARCH_BAR)
        assert search_bar, f'Поисковая строка не найдена для {self.__class__.__name__}. {self.take_screenshot_message()}'
        return search_bar


    def enter_request(self, search_bar):
        search_bar.send_keys(TestData.SEARCH_COMPETENCY)
        search_button = self.find_element(*SearchCompetencyPageLocators.BUTTON_SEARCH)
        assert search_button, f'Кнопка "Найти" не найдена для {self.__class__.__name__}. {self.take_screenshot_message()}'
        self.click(search_button)

    def enter_request_2(self, search_bar):
        clear_button = self.find_element(*SearchCompetencyPageLocators.BUTTON_CLEAR)
        self.click(clear_button)
        time.sleep(2)
        search_bar.send_keys('crispr')
        search_button = self.find_element(*SearchCompetencyPageLocators.BUTTON_SEARCH)
        assert search_button, f'Кнопка "Найти" не найдена для {self.__class__.__name__}. {self.take_screenshot_message()}'
        self.click(search_button)


    def should_be_module_map(self):
        assert self.find_element(*SearchCompetencyPageLocators.MODULE_MAP), \
            f'Модуль Карта не найден для {self.__class__.__name__}. {self.take_screenshot_message()}'


    def should_be_content_map(self):
        assert self.find_element(*SearchCompetencyPageLocators.CONTENT_MAP), \
            f'Содержимое модуля Карта не найдено для {self.__class__.__name__}. {self.take_screenshot_message()}'


    def should_be_content_map_is_not_null(self):
        try:
            token = self.get_token()
            payload = {'Authorization': 'token ' + str(token)}
            url = Endpoints.Map_CompetencyPage
            params = TestData.SEARCH_PARAM
            response = requests.get(url, params=params, headers=payload, verify=self.cert_path)
            assert response.status_code in [200, 204], (f'Запрос на эндпоинт "Карта" вернул {response.status_code}-статус-код.'
                                                 f'ОР - статус-код - 200')
            if response.status_code == 204:
                return None
            data = response.json()
            print(data)
            return data
        except Exception as err:
            assert False, f"Ошибка: {err}"


    def validate_response_map(self, response):
        self.validate_schema_of_response_(response, Map.schema)


    def should_be_name_map(self):
        title = self.should_be_element(MapLocators.TITLE, 'Название модуля не найдено')
        expected_title = ConstCompetencyPage.title_in_module_map_in_competency_page
        self.should_be_correct_title(title, expected_title)



    def should_be_full_screen_fiture(self):
        button = self.find_element(*MapLocators.BUTTON_FULL_SCREEN)
        assert button, f'Фича на весь экран не найдена для {self.__class__.__name__}. {self.take_screenshot_message()}'
        assert button.text == ConstCompetencyPage.full_screen_in_map, (f'Наименовании фичи не верно. ОР - {Const.full_screen_in_map},'
                                                         f' ФР - {button.text} для '
                                                         f'{self.__class__.__name__}. {self.take_screenshot_message()}')

    def should_be_refresh_button(self):
        button = self.find_element(*MapLocators.BUTTON_REFRESH)
        assert button, (f'В карте отсутствует кнопка "обновить данные в карте для {self.__class__.__name__}. '
                        f'{self.take_screenshot_message()}')

    def should_be_zoomcontrol_body(self):
        zoomcontrol_body = self.find_element(*MapLocators.ZOOMCONTROL_BODY)
        assert zoomcontrol_body, (f'В карте отсутствует функционал изменения зума карты для {self.__class__.__name__}. '
                        f'{self.take_screenshot_message()}')


    def should_be_button_zoomcontrol_out(self):
        button_zoomcontrol_out = self.find_element(*MapLocators.BUTTON_ZOOMCONTROL_OUT)
        assert button_zoomcontrol_out, (f'В карте отсутствует кнопка уменьшения масштаба (зум) карты для '
                                        f'{self.__class__.__name__}. {self.take_screenshot_message()}')


    def should_be_button_zoomcontrol_in(self):
        button_zoomcontrol_in = self.find_element(*MapLocators.BUTTON_ZOOMCONTROL_IN)
        assert button_zoomcontrol_in, (f'В карте отсутствует кнопка цвеличения масштаба (зум) карты для '
                                       f'{self.__class__.__name__}. {self.take_screenshot_message()}')


    def should_be_zoomcontrol_slider(self):
        zoomcontrol_slider = self.find_element(*MapLocators.BUTTON_ZOOMCONTROL_IN)
        assert zoomcontrol_slider, (f'В карте отсутствует кнопка цвеличения масштаба (зум) карты для '
                                       f'{self.__class__.__name__}. {self.take_screenshot_message()}')

    def should_be_zoomcontrol_levels(self, i, level):
        hint = self.should_be_element((By.CSS_SELECTOR, MapLocators.HINTS_ZOOMCONTROL_LEVELS[1].format(i)),
                               f"Отсутствует подсказка({level}) в зуме карты")
        assert hint.text == level, f'Наименование уровня зума в карте не соответвтует ОР. ОР - {level}, ФР - {hint.text}'


    def should_be_change_zoom_in_module_map(self, scale, i):
        locator = By.CSS_SELECTOR, MapLocators.ZOOMCONTROL_LEVELS[1].format(i)
        self.should_be_element(locator,f"Отсутствует кнопка для изменения масштаба в зуме карты")
        self.scroll_and_click(locator)
        assert self.should_be_attribute_with_value(MapLocators.ZOOMCONTROL_SLIDER, 'title', scale), \
            f'Значение масштаба в элементе слайдер зума не верное. Ожидалось - {scale}'
        zoom_text = self.should_be_element(MapLocators.SCALE_VALUE, 'Значение масшатаба не найдено на карте')
        assert zoom_text.text == scale, \
            f'Значение масштаба, указанное на карте не верное. Ожидалось - {scale}. Фактические - {zoom_text.text}'


    def can_open_legal_person_of_each_region(self, response):
        active_regions = []
        regions_params = []
        regions = response['zoom_1']['data']  # Получаем данные регионов
        for region in regions:
            active_regions.append(region["ID_1"])
            params = {
                "search": TestData.SEARCH_COMPETENCY,
                "type_map_obj": region["object"]["type_map_obj"],
                "uid": region["object"]["uid"],
                "ordering": "-curr_summary"
            }
            regions_params.append(params)
        print("Active Regions:", active_regions)

        for index, params in enumerate(regions_params):
            # token = self.get_token()
            # payload = {'Authorization': 'token ' + str(token)}
            # url = Endpoints.RaitingInMap_CompetencyPage
            # param = params
            # response = requests.get(url, params=param, headers=payload, verify=self.cert_path)
            # assert response.status_code == 200, (
            #     f'Запрос на эндпоинт "Карта" вернул {response.status_code}-статус-код.'
            #     f'ОР - статус-код - 200')
            # print(f'response - {response.json()}')
            selector = f'#map g path.region.region-{active_regions[index]}'
            print(f'selector - {selector}')
            # region_locator = self.find_element(By.CSS_SELECTOR, selector)
            region_locator = WebDriverWait(self.browser, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
            )
            time.sleep(80)
            region_locator.click()
            time.sleep(2)
            button_close = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.swal2-confirm.swal2-styled.swal2-default-outline')))
            button_close.click()
            button_close = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-footer button"))
            )
            raiting_region = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal.fade"))
            )
            if 'show' in raiting_region.get_attribute('class'):
                self.browser.execute_script("arguments[0].scrollIntoView();", button_close)
                button_close.click()
                time.sleep(2)



    def should_be_module_statistic(self):
        module_button = self.find_element(*SearchCompetencyPageLocators.MODULE_STATISTICS)
        assert module_button, \
            f'Модуль Статистика не найден для {self.__class__.__name__}. {self.take_screenshot_message()}'
        return module_button


    def should_be_content_statistic(self):
        assert self.find_element(*SearchCompetencyPageLocators.CONTENT_STATISTICS), \
            (f'Содержимое модуля Статистика не найдено для {self.__class__.__name__}. '
             f'{self.take_screenshot_message()}')


    def should_be_content_statistic_is_not_null(self):
        try:
            token = self.get_token()
            payload = {'Authorization': 'token ' + str(token)}
            url = Endpoints.Statistic_CompetencyPage
            params = TestData.SEARCH_PARAM
            response = requests.get(url, params=params, headers=payload, verify=self.cert_path)

            # Проверяем статус код
            assert response.status_code in [200, 206, 204], (
                f'Запрос на эндпоинт "Статистика" вернул {response.status_code}-статус-код.'
                f' ОР - статус-код - 200')
            if response.status_code == 204:
                return None
            data = response.json()
            print(data)
            return data
        except Exception as err:
            assert False, f"Ошибка: {err}"


    def should_be_name_statistic(self, count):
        title = self.should_be_element(StatisticLocators.TITLE, 'Название модуля не найдено')
        expected_title = f"{ConstCompetencyPage.title_in_module_statistic_in_competency_page} ({count})"
        self.should_be_correct_title(title, expected_title)


    def should_be_legends_charts(self, count):
        for i in range(1, count+1):
            legend_locator = By.CSS_SELECTOR, StatisticLocators.LEGEND_CHART[1].format(i)
            self.should_be_element(legend_locator,f"Отсутствует легенда для {i}-гистограммы в Статистике")


    def should_be_quantity_charts(self):
        list_charts = self.browser.find_elements(*StatisticLocators.QUANTITY_CHARTS)
        quantity_charts = len(list_charts)
        return quantity_charts


    def validate_response_statistic(self, response):
        self.validate_schema_of_response_(response, Statistic.schema)


    def should_be_title_of_chart(self, response, i, expected_title):
        if response['results'][i] is not None:
            actual_titile = response['results'][i]['options']['plugins']['title']['text']
            assert actual_titile == expected_title, (f'Наименование гистограммы в Статистике не соответствует ОР. '
                                                     f'ФР - {actual_titile}. ОР - {expected_title} для '
                                                     f'{self.__class__.__name__}.')
        else:
            pytest.skip(f"Тест пропущен, так как в модуле Статистика отсутствуют данные по запросу "
                        f"{TestData.SEARCH_COMPETENCY}")


    def should_be_name_of_axis_in_charts(self, response, i, path, expected_name):
        if response['results'][i] is not None:
            actual_name = response
            for key in path:
                actual_name = actual_name[key]
            assert actual_name == expected_name, (f'Наименование оси гистограммы в Статистике не соответствует ОР.'
                                                  f'ФР - {actual_name}. ОР - {expected_name} для '
                                                  f'{self.__class__.__name__}.')
        else:
            pytest.skip(f"Тест пропущен, так как в модуле Статистика отсутствуют данные по запросу "
                        f"{TestData.SEARCH_COMPETENCY}")


    def should_be_years(self, response, i):
        if response['results'][i] is not None:
            labels = response['results'][0]['data']['labels']
            assert isinstance(labels, list), (f"В графике 'Публикационная и другие виды активности' годы не указаны в "
                                              f"списке для  {self.__class__.__name__}.")
            assert len(labels) >= 1, (f"В графике 'Публикационная и другие виды активности' отсутстует наименование "
                                      f"года/лет для {self.__class__.__name__}.")
            for year in labels:
                assert isinstance(year, int), (f"В графике 'Публикационная и другие виды активности' годы не указаны как "
                                               f"целое число для {self.__class__.__name__}.")
                assert 1000 <= year <= 9999, (f"В графике 'Публикационная и другие виды активности' годы не соответствуют"
                                              f" формату YYYY для {self.__class__.__name__}.")
        else:
            pytest.skip(f"Тест пропущен, так как в модуле Статистика отсутствуют данные по запросу "
                        f"{TestData.SEARCH_COMPETENCY}")


    def should_be_correct_name_entity(self, response, num, names):
        if response['results'][num] is not None:
            entity_activities = response['results'][num]['data']['datasets']
            for i in range(len(entity_activities)):
                assert entity_activities[i]['label'] in names, \
                    (f'В графике неверно указана сущность. '
                     f'ФР - {entity_activities[i]["label"]}, ОР - имя из списка - {names} '
                     f'для {self.__class__.__name__}.')
        else:
            pytest.skip(f"Тест пропущен, так как в модуле Статистика отсутствуют данные по запросу "
                        f"{TestData.SEARCH_COMPETENCY}")


    def should_be_correct_color_entity(self, response, num, colors):
        if response['results'][num] is not None:
            entity_activities = response['results'][num]['data']['datasets']
            for i in range(len(entity_activities)):
                label = entity_activities[i]['label']
                background_color = entity_activities[i]['backgroundColor']
                expected_color = (colors.get(label))
                assert background_color == expected_color, (f'Цвет для сущности "{label}" неверен. '
                                                            f'ФР - {background_color}, ОР - {expected_color} для '
                                                            f'{self.__class__.__name__}.')
        else:
            pytest.skip(f"Тест пропущен, так как в модуле Статистика отсутствуют данные по запросу "
                        f"{TestData.SEARCH_COMPETENCY}")

    def should_be_correct_color_entity_in_chart_niokr(self, response):
        if response['results'][1] is not None:
            entity_activities = response['results'][1]['data']['datasets']
            for i in range(len(entity_activities)):
                label = entity_activities[i]['label']
                background_color = entity_activities[i]['backgroundColor']
                expected_color = (ConstCompetencyPage.color_entity_in_chart_niokr_budjet_in_statistic_in_competency_page
                                  .get(label))
                assert background_color == expected_color, (f'Цвет для сущности "{label}" неверен. '
                                                            f'ФР - {background_color}, ОР - {expected_color} для '
                                                            f'{self.__class__.__name__}.')
        else:
            pytest.skip(f"Тест пропущен, так как в модуле Статистика отсутствуют данные по запросу "
                        f"{TestData.SEARCH_COMPETENCY}")


    def should_be_correct_quantity_entity(self, response, chart):
        if response['results'][chart] is not None:
            entity_activities = response['results'][0]['data']['datasets']
            for i in range(len(entity_activities)):
                data_values = entity_activities[i]['data']
                assert len(data_values) >= 1, \
                    (f'У сущности "{entity_activities[i]["label"]}" не указано количество для '
                     f'{self.__class__.__name__}.')
                for value in data_values:
                    assert value >= 0, \
                        (f'У сущности "{entity_activities[i]["label"]}" количество указано отрицательное для '
                         f'{self.__class__.__name__}.')
        else:
            pytest.skip(f"Тест пропущен, так как в модуле Статистика отсутствуют данные по запросу "
                        f"{TestData.SEARCH_COMPETENCY}")


    def should_be_quantity_entity_in_each_year(self, response, chart):
        if response['results'][chart] is not None:
            len_list_with_years = len(response['results'][0]['data']['labels'])
            entity_activities = response['results'][0]['data']['datasets']
            for i in range(len(entity_activities)):
                len_list_with_count = len(entity_activities[i]['data'])
                assert len_list_with_count == len_list_with_years, (f'Отсутствует количество в одном из году для сущности'
                                                                    f' {entity_activities[i]["label"]} для '
                                                                    f'{self.__class__.__name__}.')
        else:
            pytest.skip(f"Тест пропущен, так как в модуле Статистика отсутствуют данные по запросу "
                        f"{TestData.SEARCH_COMPETENCY}")


    def should_be_should_be_name_in_legend(self, response, chart):
        if response['results'][chart] is not None:
            top_count = len(response['results'][chart]['data']['datasets'])
            for i in range(top_count):
                name = response['results'][chart]['data']['datasets'][i]['label']
                for item in name:
                    assert isinstance(item, str) and item.strip(), f"{i+1}-значение в легенде не указано - ФР - {item}"
        else:
            pytest.skip(f"Тест пропущен, так как в модуле Статистика отсутствуют данные по запросу "
                        f"{TestData.SEARCH_COMPETENCY}")


    def should_be_quantity_of_element(self, response, chart):
        if response['results'][chart] is not None:
            top_count = len(response['results'][chart]['data']['datasets'])
            for i in range(top_count):
                quantity = response['results'][chart]['data']['datasets'][i]['data']
                print(f'name - {quantity}')
                assert len(quantity) > 0, f'Для {i+1}-значения не указано количество'
                assert len(quantity) == 1, (f'Для {i+1}-значения указано количество не как одно число. ФР - указано '
                                            f'{len(quantity)}-значения - {quantity}')
                assert quantity[0] > 0, f'Для {i+1}-значения указано отрицательное количество. ФР - {quantity[0]}'
        else:
            pytest.skip(f"Тест пропущен, так как в модуле Статистика отсутствуют данные по запросу "
                        f"{TestData.SEARCH_COMPETENCY}")


    def should_be_color_of_element(self, response, chart):
        if response['results'][chart] is not None:
            elements = response['results'][chart]['data']['datasets']
            expected_colors = ConstCompetencyPage.color_entity_in_top_5_charts_in_statistic_in_competency_page
            # Хранение уникальных значений backgroundColor
            unique_colors = set()
            for element in elements:
                color_element = element['backgroundColor']
                assert color_element, f"У {element}-элемента отсутствует значение цвета"
                assert color_element in expected_colors, (f"У {element}-элемента цвет указан не из "
                                                          f"ожидаемой палитры: {expected_colors}")
                # Добавляем цвет в множество для проверки уникальности
                unique_colors.add(color_element)
            # Проверка, что все значения backgroundColor уникальны
            are_equal = set(expected_colors) == set(unique_colors)
            assert are_equal, "Некоторые элементы имеют одинаковый цвет"
        else:
            pytest.skip(f"Тест пропущен, так как в модуле Статистика отсутствуют данные по запросу "
                        f"{TestData.SEARCH_COMPETENCY}")


    def should_be_module_graph_ak(self):
        module_button = self.find_element(*SearchCompetencyPageLocators.MODULE_GRAPH_AK)
        assert module_button, \
            (f'Модуль граф авторские коллективы не найдендля {self.__class__.__name__}. '
             f'{self.take_screenshot_message()}')
        return module_button


    def should_be_content_graph_ak(self):
        assert self.find_element(*SearchCompetencyPageLocators.CONTENT_GRAPH_AK), \
            f'Содержимое модуля Графа АК не найдено для {self.__class__.__name__}. {self.take_screenshot_message()}'


    def should_be_module_graph_ko(self):
        module_button = self.find_element(*SearchCompetencyPageLocators.MODULE_GRAPH_KO)
        assert module_button, \
            (f'Модуль граф коллаборации организаций не найден для {self.__class__.__name__}. '
             f'{self.take_screenshot_message()}')
        return module_button


    def should_be_content_graph_ko(self):
        assert self.find_element(*SearchCompetencyPageLocators.CONTENT_GRAPH_KO), \
            f'Содержимое модуля Графа КО не найдено для {self.__class__.__name__}. {self.take_screenshot_message()}'


    def should_be_module_rating(self):
        assert self.find_element(*SearchCompetencyPageLocators.MODULE_RATING), \
            (f'Модуль рейтинг организаций/ученых не найден для {self.__class__.__name__}. '
             f'{self.take_screenshot_message()}')

