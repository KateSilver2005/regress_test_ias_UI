import time
import datetime
import re

import requests
import os

from selenium.common import ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException, \
    WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import MainPageLocators, AdvancedSearch, NewsPageLocators
from .const_and_test_data import Const
from .endpoints import Endpoints


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
        self.cert_path = os.path.join(os.path.dirname(__file__), '../cert/trusted_certs.crt')

    def should_be_button_analitic(self):
        return self.should_be_element(MainPageLocators.BUTTON_ANALITIC,
                                      "Кнопка перехода в Аналитику не найдена")

    def should_be_button_in_services(self):
        return self.should_be_element(MainPageLocators.BUTTON_IN_SERVICES,
                                      "Кнопка перехода в Сервисы не найдена")

    def should_be_button_info_about_infoprovider(self):
        return self.should_be_element(MainPageLocators.BUTTON_INFO_ABOUT_INFOPROVIDER,
                                      'Кнопка перехода в "Сведения о поставщике информации" не найдена')

    def should_be_title_lk(self):
        title_lk = self.should_be_element(MainPageLocators.TITLE_LK,
                                          'Элемент "Личный кабинет" не найден')
        self.should_be_true_text(title_lk, Const.title_lk)

    def should_be_tabs_search(self):
        return self.should_be_element(MainPageLocators.TABS_SEARCH,
                                      'Переключатели поисков не найдены')

    def should_be_tabs(self, locator):
        self.should_be_element(locator, 'Переключатель поиска не найден')
        return locator

    def should_be_active(self, active):
        attribute = "class"
        value = "active"
        assert self.is_element_enabled(active, attribute, value), (f"Вкладка поиск по компетенциям не активна "
                                                                   f"для {self.__class__.__name__}. "
                                                                   f"{self.take_screenshot_message()}")

    def should_be_search_area(self):
        return self.should_be_element(MainPageLocators.SEARCH_AREA,
                                      'Поле для ввода поискового запроса не найдено')

    def should_be_placeholder(self, locator, const_placeholder):
        placeholder = locator.get_attribute("placeholder")
        assert placeholder == const_placeholder, (f'В поле для ввода поискового запроса placeholder не '
                                                  f'соответствует вкладке. Ожидалось - {const_placeholder}. '
                                                  f'Фактически - {placeholder} для {self.__class__.__name__}. '
                                                  f'{self.take_screenshot_message()}')

    def should_be_clear_button(self):
        self.should_be_element(MainPageLocators.CLEAR_BUTTON, 'Кнопка "Очистить" не найдена')

    def should_be_advanced_search_button(self):
        return self.should_be_element(AdvancedSearch.ADVANCED_SEARCH_BUTTON,
                                      'Фича "Расширенный поиск" не найден')


    def should_be_checkbox(self, checkbox):
        checkbox_element = self.should_be_element(checkbox, f'Чекбокс {checkbox} не найден')
        return checkbox_element

    def should_be_label(self, label_locator, label_text):
        label = self.should_be_element(label_locator, 'Чекбокс не найден')
        assert label.text == label_text, (f'Наименование чекбокса не соответствует ОР. ОР - {label_text}. '
                                          f'ФР - {label.text} для {self.__class__.__name__}. '
                                          f'{self.take_screenshot_message()}')

    def can_click_on_advanced_search_button(self):
        advanced_search_button = AdvancedSearch.ADVANCED_SEARCH_BUTTON
        advanced_search_area = AdvancedSearch.ADVANCED_SEARCH_AREA
        self.click(advanced_search_button)
        self.browser.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)
        assert self.is_element_enabled(advanced_search_button, 'class', 'collapsed'), \
            f'Расширенный поиск не раскрылся для {self.__class__.__name__}. {self.take_screenshot_message()}'
        self.should_be_element(advanced_search_area, 'Отсутствует блок с чек-боксами по "Расширенному поиску"')


    def should_be_button_search(self):
        return self.should_be_element(AdvancedSearch.SEARCH_BUTTON, 'Кнопка "Найти" не найдена')


    def should_be_range_distance(self, range_distance_locator):
        return self.should_be_element(range_distance_locator, 'Ползунок изменения расстояния между словами не найден')


    def should_be_label_range_distance(self, steps):
        label_locator = AdvancedSearch.LABEL_VALUE_DISTANCE_IN_ADVANCED_SEARCH
        label_text = AdvancedSearch.LABEL_TEXT_VALUE_DISTANCE_IN_ADVANCED_SEARCH + steps
        time.sleep(1)
        label = self.should_be_element(label_locator,
                                       'Наименование для ползунка изменения расстояние между словами не найдено')
        assert label.text == label_text, (f'Наименование чекбокса не соответствует ОР. ОР - {label_text}. ФР - '
                                          f'{label.text} для {self.__class__.__name__}. '
                                          f'{self.take_screenshot_message()}')


    def can_change_distance(self, value_distance, pixsels, range_distance, browser, steps=None):
        actions = ActionChains(browser)
        try:
            # Пытаемся удерживать и перемещать элемент
            actions.click_and_hold(value_distance).move_by_offset(pixsels, 0).release().perform()

            if steps == 5:
                actions.click_and_hold(value_distance).move_by_offset(-10, 0).release().perform()
                time.sleep(1)
                actions.click_and_hold(value_distance).move_by_offset(pixsels, 0).release().perform()

            time.sleep(0.5)
        except (ElementNotInteractableException, NoSuchElementException, WebDriverException) as e:
            assert f"Ошибка при взаимодействии с элементом {range_distance}: {e}"

    def should_be_element_is_disabled(self, element, dependent_checkbox=None):
        is_disabled = element.get_attribute('disabled')
        assert is_disabled == 'true', (f'Элемент с локатором {dependent_checkbox} не заблокирован для '
                                       f'{self.__class__.__name__}. {self.take_screenshot_message()}')

    def should_be_slider(self, locator):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 1360)
        time.sleep(2)
        self.should_be_element(locator, f"Модуль отсутствует с локатором {locator}")

    def should_be_title_for_slider(self, locator, const):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 1360)
        title = self.should_be_element(locator, f'В блоке заголовок {locator} не найден')
        self.should_be_correct_title(title, const)

    def should_be_section_news(self):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 750)
        self.should_be_element(MainPageLocators.SECTION_NEWS, 'Раздел новости отсутствует')

    def should_be_title_section(self):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 750)
        title = self.should_be_element(MainPageLocators.TITLE_SECTION_NEWS, 'В разделе новости отсутствует заголовок')
        self.should_be_correct_title(title, Const.title_section_news)

    def should_be_content(self):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 750)
        self.should_be_element(MainPageLocators.CONTENT_SECTION_NEWS, 'В разделе новости отсутствуют новости')
        # дописать когда произойдет багфикс - в разделе появятся несколько новостей ИАС

    def should_be_link_on_page_news(self):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 750)
        locator = MainPageLocators.LINK_ON_PAGE_WITH_ALL_NEWS
        link = self.should_be_element(locator, "В разделе новости отсутствует ссылка для перехода "
                                               "на страницу новостей")
        self.should_be_true_text(link, Const.text_to_link_in_section_news)
        return locator

    def should_be_slides(self, locator, count_slides, pixel_down):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, pixel_down)
        list_slides = self.browser.find_elements(*locator)
        assert len(list_slides) > 0, (f"Слайды в Графике внесения сведений не найдены для {self.__class__.__name__}. "
                                      f"{self.take_screenshot_message()}")
        assert len(list_slides) == count_slides, (f"В блоке не верное количество слайдов. ОР - {count_slides} слайдов, "
                                                  f"фактически - {len(list_slides)} для {self.__class__.__name__}. "
                                                  f"{self.take_screenshot_message()}")

    def should_be_button_next_slide(self, locator, pixel_down):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, pixel_down)
        return self.should_be_element(locator, f"В блоке кнопка для перехода к следующему слайду не "
                                               f"найдена {locator}")

    def should_be_button_previous_slide(self, locator, pixel_down):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, pixel_down)
        return self.should_be_element(locator, f"В блоке кнопка для перехода к предыдущему слайду не "
                                               f"найдена {locator}")

    def should_be_picture_in_slide(self):
        locator = (By.ID, MainPageLocators.SLIDE_IN_GLOBAL_CHARTS[1].format(0))
        self.scroll_by_element(locator, 750)
        global path_to_picture
        number = ['1', '2', '3', '4-8', '5', '6', '7', '8-4', '9', '10', '11', '12']
        for i in range(1, 13):
            picture = (By.CSS_SELECTOR, MainPageLocators.PICTURE_IN_SLIDE_IN_GRAFIC_VNESENIYA_SVEDEDIY[1].format(i))
            path_to_picture = self.should_be_attribute(picture, 'src')
            expected_path_picture = Const.MAIN_LINK + f'img/main/graphic/{number[i - 1]}.png'
            assert path_to_picture == expected_path_picture, (
                f'В блоке "График внесения сведений" не верное изображение '
                f'на {i}-слайде. Ожидалось {expected_path_picture}, '
                f'фактически {path_to_picture} для '
                f'{self.__class__.__name__}. {self.take_screenshot_message()}')
            self.should_be_no_attribute_with_value(MainPageLocators.LIST_SLIDES_IN_GRAFIC_VNESENIYA_SVEDEDIY,
                                                   "class", "carousel__slide--sliding")
            # next_slide = self.find_element(*MainPageLocators.NEXT_SLIDE_IN_GRAFIC_VNESENIYA_SVEDEDIY)
            # assert next_slide is not None, "Кнопка перехода к следующему слайду не найдена"
            self.click(MainPageLocators.NEXT_SLIDE_IN_GRAFIC_VNESENIYA_SVEDEDIY)
        for i in range(1, 13):
            # previous_slide = self.find_element(*MainPageLocators.PREVIOUS_SLIDE_IN_GRAFIC_VNESENIYA_SVEDEDIY)
            # assert previous_slide is not None, "Кнопка перехода к предыдущему слайду не найдена"
            self.click(MainPageLocators.PREVIOUS_SLIDE_IN_GRAFIC_VNESENIYA_SVEDEDIY)
            self.click(MainPageLocators.PREVIOUS_SLIDE_IN_GRAFIC_VNESENIYA_SVEDEDIY)
            self.should_be_no_attribute_with_value(MainPageLocators.LIST_SLIDES_IN_GRAFIC_VNESENIYA_SVEDEDIY,
                                                   "class", "carousel__slide--sliding")


    def should_be_chart_in_slide(self):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 1360)
        locator = (By.ID, MainPageLocators.SLIDE_IN_GLOBAL_CHARTS[1].format(0))
        for i in range(17):
            self.should_be_element((By.ID, MainPageLocators.SLIDE_IN_GLOBAL_CHARTS[1].format(i)),
                                   f"Отсутствует {i+1}-слайд")
            title = self.should_be_element(
                (By.CSS_SELECTOR, MainPageLocators.TITLE_OF_SLIDE_IN_GLOBAL_CHARTS[1].format(i+1)),
                f'Заголовок на {i+1}-слайде не найден')
            self.should_be_correct_title(title, Const.title_of_slide_in_global_charts[i])
            self.should_be_no_attribute_with_value(locator, "class", "carousel__slide--sliding")
            self.click(MainPageLocators.NEXT_SLIDE_IN_GLOBAL_CHARTS)
            time.sleep(0.5)
        for i in range(17):
            self.should_be_no_attribute_with_value(locator, "class", "carousel__slide--sliding")
            self.should_be_element((By.ID, MainPageLocators.SLIDE_IN_GLOBAL_CHARTS[1].format(16-i)),
                                   f"Отсутствует статистика на {16-i}-слайде")
            self.click(MainPageLocators.PREVIOUS_SLIDE_IN_GLOBAL_CHARTS)
            time.sleep(0.5)


    def request_post(self):
        try:
            token = requests.post(Endpoints.Login, json=Endpoints.params, verify="").json()['token']
            return token
        except Exception as err:
            print(f'Произошла ошибка: {err} во время выполнения запроса на выгрузку')


    def can_get_data_global_charts(self):
        try:
            token = self.request_post()
            payload = {'Authorization': 'token ' + str(token)}
            url = Endpoints.Charts_MainPage
            response = requests.get(url, headers=payload, verify=self.cert_path)

            assert response.status_code == 200, (f'Запрос на эндпоинт "Статистика" вернул {response.status_code}-статус-код.'
                                                 f'ОР - статус-код - 200')
            data = response.json()
            print(data)
            return data
        except Exception as err:
            print(f"Ошибка: {err}")


    def should_be_years_in_legend(self, data, i):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 1360)
        # список текущих лет
        expected_year_list = [datetime.datetime.now().year - year for year in range(16)][::-1]
        # текущий список лет из легенды статистики
        actual_year_list = data["results"][i]["data"]["labels"]

        assert len(expected_year_list) == len(actual_year_list), (f"В легенде Статистики не верное количество периодов "
                                                                  f"по годам Ожидаемый результат - "
                                                                  f"{len(expected_year_list)}-периодов. Фактические - "
                                                                  f"{len(actual_year_list)}-периодов для "
                                                                  f"{self.__class__.__name__}. "
                                                                  f"{self.take_screenshot_message()}")

        # Сравниваем списки
        assert expected_year_list == actual_year_list, (f"В легенде Статистики не верный порядок периодов."
                                                        f" Ожидаемый результат - {expected_year_list}, "
                                                        f"Фактический - {actual_year_list} для "
                                                        f"{self.__class__.__name__}. {self.take_screenshot_message()}")

    def should_be_color_element_in_legend(self, data, element_number):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 1360)
        hex = data["results"][0]["data"]["datasets"][element_number - 1]["backgroundColor"]  # извлекаем код цвета из response ("backgroundColor": "#c378e1")
        assert hex is not None, (f'Из бэка не пришло значение значение цвета для сущности (в response) для '
                                 f'{self.__class__.__name__}. {self.take_screenshot_message()}')
        # print(f'hex - {hex}')

        element = self.should_be_element((By.CSS_SELECTOR, MainPageLocators.COLOR_IN_LEGEND_CHART_1_IN_GLOBAL_CHARTS[1].format(element_number)),
                               f"В легенде статистики отсутствует цветовой индикатор сущности")
        color = element.get_attribute("style") # получаем значение атрибута с цветом элемента
        assert color is not None, (f'В легенде отсутствует значение цвета для сущности (в структуре DOM) для '
                                   f'{self.__class__.__name__}. {self.take_screenshot_message()}')

        match = re.search(r'rgb\((\d+),\s*(\d+),\s*(\d+)\)', color) # извлекаем код цвета из строки (background: rgb(255, 159, 28);)
        rgb = (int(match.group(1)), int(match.group(2)), int(match.group(3))) # создаем кортеж из кода (255, 159, 28)
        # print(f'rgb - {rgb}')
        # print(f'сконвертируемый hex - {self.hex_to_rgb(hex)}')
        assert rgb == self.hex_to_rgb(hex), (f'В легенде цвет сущности не совпадает между UI и бэк. В UI цвет указан в '
                                             f'формате rgb - {rgb}, из бэк пришел в формате hex - {hex} '
                                             f'{self.__class__.__name__}. {self.take_screenshot_message()}')


    # # Проверяем равенство
    # if converted_rgb == rgb_color:
    #     print(f"Цвет {hex_color} равен цвету rgb{rgb_color}.")
    # else:
    #     print(f"Цвет {hex_color} не равен цвету rgb{rgb_color}.")

