import time
import datetime
import re

import pytest
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
from .const_and_test_data import Env, Const, ConstMainPage
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
        self.should_be_true_text(title_lk, ConstMainPage.title_lk)

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

    def should_be_slider(self, locator, pixels):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, pixels)
        time.sleep(2)
        self.should_be_element(locator, f"Модуль отсутствует с локатором {locator}")


    def should_be_info_for_users(self, locator):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 1599.75)
        time.sleep(2)
        self.should_be_element(locator, f"Модуль отсутствует с локатором {locator}")


    def should_be_title_for_block(self, locator, const, pixels):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, pixels)
        time.sleep(2)
        title = self.should_be_element(locator, f'В блоке заголовок {locator} не найден')
        self.should_be_correct_title(title, const)

    def should_be_section_news(self):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 750)
        self.should_be_element(MainPageLocators.SECTION_NEWS, 'Раздел новости отсутствует')

    def should_be_title_section(self):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 750)
        title = self.should_be_element(MainPageLocators.TITLE_SECTION_NEWS, 'В разделе новости отсутствует заголовок')
        self.should_be_correct_title(title, ConstMainPage.title_section_news)

    def should_be_content(self):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 750)
        self.should_be_element(MainPageLocators.CONTENT_SECTION_NEWS, 'В разделе новости отсутствуют новости')
        # дописать когда произойдет багфикс - в разделе появятся несколько новостей ИАС

    def should_be_link_on_page_news(self):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 750)
        locator = MainPageLocators.LINK_ON_PAGE_WITH_ALL_NEWS
        link = self.should_be_element(locator, "В разделе новости отсутствует ссылка для перехода "
                                               "на страницу новостей")
        self.should_be_true_text(link, ConstMainPage.text_to_link_in_section_news)
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
            expected_path_picture = Env.MAIN_LINK + f'img/main/graphic/{number[i - 1]}.png'
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
            self.should_be_correct_title(title, ConstMainPage.title_of_slide_in_global_charts[i])
            self.should_be_no_attribute_with_value(locator, "class", "carousel__slide--sliding")
            self.click(MainPageLocators.NEXT_SLIDE_IN_GLOBAL_CHARTS)
            time.sleep(0.5)
        for i in range(17):
            self.should_be_no_attribute_with_value(locator, "class", "carousel__slide--sliding")
            self.should_be_element((By.ID, MainPageLocators.SLIDE_IN_GLOBAL_CHARTS[1].format(16-i)),
                                   f"Отсутствует статистика на {16-i}-слайде")
            self.click(MainPageLocators.PREVIOUS_SLIDE_IN_GLOBAL_CHARTS)
            time.sleep(0.5)




    def can_get_data_global_charts(self):
        try:
            token = self.get_token()
            payload = {'Authorization': 'token ' + str(token)}
            url = Endpoints.Charts_MainPage
            response = requests.get(url, headers=payload, verify=self.cert_path)
            assert response.status_code == 200, (f'Запрос на эндпоинт "Статистика" вернул {response.status_code}-статус-код.'
                                                 f'ОР - статус-код - 200')
            data = response.json()
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



    def should_be_color_element_in_legend(self, data, chart_number_api, element_number_api, chart_number_css, element_number_css):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 1360)
        hex_color = data["results"][chart_number_api]["data"]["datasets"][element_number_api]["backgroundColor"]  # извлекаем код цвета из response ("backgroundColor": "#c378e1")

        assert hex_color is not None, (f'Из бэка не пришло значение цвета для сущности (в response) для '
                                 f'{self.__class__.__name__}. {self.take_screenshot_message()}')

        for i in range(chart_number_api):
            locator_slide = (By.ID, MainPageLocators.SLIDE_IN_GLOBAL_CHARTS[1].format(0))
            self.should_be_no_attribute_with_value(locator_slide, "class", "carousel__slide--sliding")
            self.click(MainPageLocators.NEXT_SLIDE_IN_GLOBAL_CHARTS)
            time.sleep(0.5)
        element = self.should_be_element((By.CSS_SELECTOR,
                                          MainPageLocators.COLOR_OF_ELEMENT_IN_LEGEND_CHART_IN_GLOBAL_CHARTS[1].format(chart_number_css, element_number_css)),
                               f"В легенде статистики отсутствует цветовой индикатор сущности")
        color = element.get_attribute("style") # получаем значение атрибута с цветом элемента

        assert color is not None, (f'В легенде отсутствует значение цвета для сущности (в структуре DOM) для '
                                   f'{self.__class__.__name__}. {self.take_screenshot_message()}')

        match = re.search(r'rgb\((\d+),\s*(\d+),\s*(\d+)\)', color) # извлекаем код цвета из строки (background: rgb(255, 159, 28);)
        rgb = (int(match.group(1)), int(match.group(2)), int(match.group(3))) # создаем кортеж из кода (255, 159, 28)

        assert rgb == self.hex_to_rgb(hex_color), (f'В легенде цвет сущности не совпадает между UI и бэк. В UI цвет указан в '
                                             f'формате rgb - {rgb}, из бэк пришел в формате hex - {hex_color} для'
                                             f'{self.__class__.__name__}. {self.take_screenshot_message()}')



    def should_be_title_of_axes_in_legend(self, data, chart_number, axis, expected):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 1360)
        title = data["results"][chart_number]["options"]["scales"][axis]["title"]["text"]
        assert title == expected, (f'В графике ось-{axis} имеет не верное наименование. Ожидалось - {expected}, '
                                    f'фактически - {title} для {self.__class__.__name__}. '
                                    f'{self.take_screenshot_message()}')


    def should_be_title_element_in_legend(self, chart_number_css, element_number_css):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 1360)
        for i in range(chart_number_css):
            locator_slide = (By.ID, MainPageLocators.SLIDE_IN_GLOBAL_CHARTS[1].format(0))
            self.should_be_no_attribute_with_value(locator_slide, "class", "carousel__slide--sliding")
            self.click(MainPageLocators.NEXT_SLIDE_IN_GLOBAL_CHARTS)
            time.sleep(0.5)
        title_locator = self.should_be_element((By.CSS_SELECTOR,
                                          MainPageLocators.TITLE_OF_ELEMENT_IN_LEGEND_CHART_IN_GLOBAL_CHARTS[1].format(chart_number_css, element_number_css)),
                                               f"В легенде статистики отсутствует наименование сущности")
        if chart_number_css == 0:
            self.should_be_true_text(title_locator,
                                     ConstMainPage.title_of_element_in_legent_chart_in_global_charts[element_number_css-1])

        else:
            self.should_be_true_text(title_locator,
                                     ConstMainPage.title_of_element_in_legent_chart_in_global_charts[chart_number_css-1])


    def deactivate_element_in_legend(self, chart_number_css, element_number_css):
        self.scroll_by_element(MainPageLocators.INFO_FOR_USERS, 1360)
        for i in range(chart_number_css):
            locator_slide = (By.ID, MainPageLocators.SLIDE_IN_GLOBAL_CHARTS[1].format(0))
            self.should_be_no_attribute_with_value(locator_slide, "class", "carousel__slide--sliding")
            self.click(MainPageLocators.NEXT_SLIDE_IN_GLOBAL_CHARTS)
            time.sleep(0.5)
        locator = (By.CSS_SELECTOR, MainPageLocators.TITLE_OF_ELEMENT_IN_LEGEND_CHART_IN_GLOBAL_CHARTS[1].format(chart_number_css, element_number_css)) # chart_number_css, element_number_css
        self.should_be_element(locator, f"В легенде статистики отсутствует цветовой индикатор сущности")
        assert self.should_be_no_attribute_with_value(locator, "style", "text-decoration: line-through"), \
            f'Элемент выключен, данные по нему не показываются в Статистике'
        self.click(locator)
        assert "text-decoration: line-through" in self.should_be_attribute(locator, "style"), \
            f"Элемент не выключен, данные по нему показываются в Статистике"


    def match_of_count_in_api_charts(self, data, num_summary_chart, num_element_summary_chart,
                                     num_single_chart, num_element_single_chart):
        in_summary_chart = data["results"][num_summary_chart]["data"]["datasets"][num_element_summary_chart]["data"]
        in_single_chart = data["results"][num_single_chart]["data"]["datasets"][num_element_single_chart]["data"]
        assert in_summary_chart == in_single_chart, (f'Количество в суммарной Статистике '
                                                     f'не совпадает с количеством в отдельной Статистике по сущности - '
                                                     f'{data["results"][num_single_chart]["data"]["datasets"][num_element_single_chart]["label"]},'
                                                     f'номер слайда в Статистике на Главной - {num_single_chart}')

    def no_regress_in_count_element_for_each_year_in_global_chart(self, data, index, element):
        actual_data = data["results"][0]["data"]["datasets"][index]["data"]
        expected_data = ConstMainPage.dict_global_chart_may_2025[element]
        for year_index in range(len(actual_data)):
            assert actual_data[year_index] >= expected_data[year_index], \
                f"Ошибка: значение для '{element}' в {ConstMainPage.dict_global_chart_may_2025['Год'][year_index]} году " \
                f"меньше ожидаемого. Фактическое: {actual_data[year_index]}, Ожидаемое: {expected_data[year_index]}"

    def scroll_to_elements(self, num_element):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(MainPageLocators.INFO_FOR_USERS)
        )
        time.sleep(0.5)
        title_info_for_users = self.find_element(*MainPageLocators.TITLE_INFO_FOR_USERS)
        self.browser.execute_script("arguments[0].scrollIntoView();", title_info_for_users)
        pixels = -120 if num_element < 10 else (145 if num_element < 13 else 250)
        self.browser.execute_script(f"window.scrollBy(0, {pixels});")
        time.sleep(2)


    def should_be_elements(self, num_element):
        self.scroll_to_elements(num_element)
        self.should_be_element((By.CSS_SELECTOR, MainPageLocators.ELEMENT_IN_INFO_FOR_USERS[1].format(num_element)),
                               'Блок для элемента отсутствует')


    def should_be_icon_of_elements(self, num_element, image):
        self.scroll_to_elements(num_element)
        locator_icon = (By.CSS_SELECTOR, MainPageLocators.ICON_OF_ELEMENT_IN_INFO_FOR_USERS[1].format(num_element))
        self.should_be_element(locator_icon,'Иконка для элемента отсутствует')
        path_to_picture = self.should_be_attribute(locator_icon, 'src')
        expected_path_picture = Env.MAIN_LINK + f"img/main/banner-info/{image}.png"
        assert path_to_picture == expected_path_picture, (f'Путь к иконкам не верный. ОР - {expected_path_picture},'
                                                          f'ФР - {path_to_picture}')


    def should_be_title_of_elements(self, num_element, expected_title):
        self.scroll_to_elements(num_element)
        locator_title = (By.CSS_SELECTOR, MainPageLocators.TITLE_OF_ELEMENT_IN_INFO_FOR_USERS[1].format(num_element))
        titles = self.should_be_element(locator_title, 'Заголовок на странице не найден')
        title_lines = titles.text.splitlines()
        title = title_lines[0].strip()
        assert title == expected_title, (f'Тайтл не верный. Фактический результат - {title.lower()} '
                                                 f'Ожидаемый результат - {expected_title} для '
                                                 f'{self.__class__.__name__}. {self.take_screenshot_message()}')



    def should_be_link_to_site_official(self, num_element):
        self.scroll_to_elements(num_element)
        locator_link = (By.CSS_SELECTOR, MainPageLocators.URL_OF_ELEMENT_IN_INFO_FOR_USERS[1].format(num_element))
        return self.should_be_element(locator_link, 'Отсутствует ссылка для перехода на официальный сайт')


    def should_be_page_official(self, expected_url, ias_page):
        try:
            assert self.url_contain(expected_url), (f'Переход осуществлен не на на официальную страницу ресурса. '
                                                    f'Ожидалось - {expected_url}. '
                                                    f'Фактически - {self.browser.current_url} '
                                                    f'для {self.__class__.__name__} {self.take_screenshot_message()}')
        finally:
            self.browser.close()
            self.browser.switch_to.window(ias_page)


    def check_assert(self, condition, message, error_messages):
        if not condition:
            error_messages.append(f'{message}. {self.take_screenshot_message()}')

    def should_be_description_scipubs(self, num_element):
        self.scroll_to_elements(num_element)
        general_statistics_locator = (By.CSS_SELECTOR, MainPageLocators.TITLE_OF_ELEMENT_IN_INFO_FOR_USERS[1].format(num_element))
        general_statistics = self.should_be_element(general_statistics_locator, 'Статистика для элемента не найдена')
        statistics_list = general_statistics.text.splitlines()
        legend_scipubs, legend_full_texts = statistics_list[1].strip(), statistics_list[3].strip()
        error_messages = []
        self.check_assert(legend_scipubs == ConstMainPage.total_scipubs_in_info_for_users[4],
                          f'Подпись не верная. Фактический результат - {legend_scipubs} '
                          f'Ожидаемый результат - {ConstMainPage.total_scipubs_in_info_for_users[4]} '
                          f'для {self.__class__.__name__}', error_messages)
        self.check_assert(legend_full_texts == ConstMainPage.total_scipubs_in_info_for_users[5],
                          f'Подпись не верная. Фактический результат - {legend_full_texts} '
                          f'Ожидаемый результат - {ConstMainPage.total_scipubs_in_info_for_users[5]} для '
                          f'{self.__class__.__name__}', error_messages)
        if error_messages:
            pytest.fail("\n".join(error_messages))


    def should_be_description_rosrid(self):
        self.scroll_to_elements(4)
        general_statistics_locator = (By.CSS_SELECTOR, MainPageLocators.TITLE_OF_ELEMENT_IN_INFO_FOR_USERS[1].format(4))
        general_statistics = self.should_be_element(general_statistics_locator, 'Статистика для элемента не найдена')
        statistics_list = general_statistics.text.splitlines()
        legend_niokr, legend_rid, legend_ikrbs, legend_diss = (statistics_list[1].strip(), statistics_list[3].strip(),
                                                               statistics_list[5].strip(), statistics_list[7].strip())
        error_messages = []
        self.check_assert(legend_niokr == ConstMainPage.description_rosrid[0],
                     f'Подпись не верная. Фактический результат - {legend_niokr} Ожидаемый результат - '
                     f'{ConstMainPage.description_rosrid[0]} для {self.__class__.__name__}', error_messages)
        self.check_assert(legend_rid == ConstMainPage.description_rosrid[2],
                          f'Подпись не верная. Фактический результат - {legend_rid} Ожидаемый результат - '
                          f'{ConstMainPage.description_rosrid[2]} для {self.__class__.__name__}', error_messages)
        self.check_assert(legend_ikrbs == ConstMainPage.description_rosrid[4],
                          f'Подпись не верная. Фактический результат - {legend_ikrbs} Ожидаемый результат - '
                          f'{ConstMainPage.description_rosrid[4]} для {self.__class__.__name__}', error_messages)
        self.check_assert(legend_diss == ConstMainPage.description_rosrid[6],
                          f'Подпись не верная. Фактический результат - {legend_diss} Ожидаемый результат - '
                          f'{ConstMainPage.description_rosrid[6]} для {self.__class__.__name__}', error_messages)
        if error_messages:
            pytest.fail("\n".join(error_messages))


    def should_be_description_patents(self):
        self.scroll_to_elements(5)
        general_statistics_locator = (By.CSS_SELECTOR, MainPageLocators.TITLE_OF_ELEMENT_IN_INFO_FOR_USERS[1].format(5))
        general_statistics = self.should_be_element(general_statistics_locator, 'Статистика для элемента не найдена')
        statistics_list = general_statistics.text.splitlines()
        legend_patents, legend_full_texts = statistics_list[1].strip(), statistics_list[3].strip()
        error_messages = []
        self.check_assert(legend_patents == ConstMainPage.description_ya_patents[0],
                          f'Подпись не верная. Фактический результат - {legend_patents} '
                          f'Ожидаемый результат - {ConstMainPage.description_ya_patents[0]} '
                          f'для {self.__class__.__name__}', error_messages)
        self.check_assert(legend_full_texts == ConstMainPage.description_ya_patents[2],
                          f'Подпись не верная. Фактический результат - {legend_full_texts} '
                          f'Ожидаемый результат - {ConstMainPage.description_ya_patents[2]} для '
                          f'{self.__class__.__name__}', error_messages)
        if error_messages:
            pytest.fail("\n".join(error_messages))


    def should_be_description_ckp_usu(self):
        self.scroll_to_elements(6)
        general_statistics_locator = (By.CSS_SELECTOR, MainPageLocators.TITLE_OF_ELEMENT_IN_INFO_FOR_USERS[1].format(6))
        general_statistics = self.should_be_element(general_statistics_locator, 'Статистика для элемента не найдена')
        statistics_list = general_statistics.text.splitlines()
        legend_ckp, legend_equipment_ckp, legend_services_ckp, legend_usu, legend_equipment_usu, legend_services_usu = \
            (statistics_list[1].strip(), statistics_list[3].strip(),
             statistics_list[5].strip(), statistics_list[7].strip(),
             statistics_list[9].strip(), statistics_list[11].strip())
        error_messages = []
        self.check_assert(legend_ckp == ConstMainPage.description_ckp_usu[0],
                     f'Подпись не верная. Фактический результат - {legend_ckp} Ожидаемый результат - '
                     f'{ConstMainPage.description_ckp_usu[0]} для {self.__class__.__name__}', error_messages)
        self.check_assert(legend_equipment_ckp == ConstMainPage.description_ckp_usu[2],
                          f'Подпись не верная. Фактический результат - {legend_equipment_ckp} Ожидаемый результат - '
                          f'{ConstMainPage.description_ckp_usu[2]} для {self.__class__.__name__}', error_messages)
        self.check_assert(legend_services_ckp == ConstMainPage.description_ckp_usu[4],
                          f'Подпись не верная. Фактический результат - {legend_services_ckp} Ожидаемый результат - '
                          f'{ConstMainPage.description_ckp_usu[4]} для {self.__class__.__name__}', error_messages)
        self.check_assert(legend_usu == ConstMainPage.description_ckp_usu[6],
                          f'Подпись не верная. Фактический результат - {legend_usu} Ожидаемый результат - '
                          f'{ConstMainPage.description_ckp_usu[6]} для {self.__class__.__name__}', error_messages)
        self.check_assert(legend_equipment_usu == ConstMainPage.description_ckp_usu[8],
                          f'Подпись не верная. Фактический результат - {legend_equipment_usu} Ожидаемый результат - '
                          f'{ConstMainPage.description_ckp_usu[8]} для {self.__class__.__name__}', error_messages)
        self.check_assert(legend_services_usu == ConstMainPage.description_ckp_usu[10],
                          f'Подпись не верная. Фактический результат - {legend_services_usu} Ожидаемый результат - '
                          f'{ConstMainPage.description_ckp_usu[10]} для {self.__class__.__name__}', error_messages)
        if error_messages:
            pytest.fail("\n".join(error_messages))


    def should_be_description_grants(self):
        self.scroll_to_elements(5)
        general_statistics_locator = (By.CSS_SELECTOR, MainPageLocators.TITLE_OF_ELEMENT_IN_INFO_FOR_USERS[1].format(7))
        general_statistics = self.should_be_element(general_statistics_locator, 'Статистика для элемента не найдена')
        statistics_list = general_statistics.text.splitlines()
        legend_grants = statistics_list[1].strip()
        error_messages = []
        self.check_assert(legend_grants == ConstMainPage.description_rnf[0],
                          f'Подпись не верная. Фактический результат - {legend_grants} '
                          f'Ожидаемый результат - {ConstMainPage.description_rnf[0]} '
                          f'для {self.__class__.__name__}', error_messages)
        if error_messages:
            pytest.fail("\n".join(error_messages))


    def should_be_total_scipubs(self, num_element, total_scipubs):
        self.scroll_to_elements(num_element)
        general_statistics_locator = (
        By.CSS_SELECTOR, MainPageLocators.TITLE_OF_ELEMENT_IN_INFO_FOR_USERS[1].format(num_element))
        general_statistics = self.should_be_element(general_statistics_locator, 'Статистика для элемента не найдена')
        statistics_list = general_statistics.text.splitlines()
        count_scipubs, count_full_texts = (int(statistics_list[2].strip().replace(' ', '')),
                                           int(statistics_list[4].strip().replace(' ', '')))
        error_messages = []
        self.check_assert(count_scipubs >= total_scipubs[0],
                          f'Количество публикаций не верное. Фактический результат - {count_scipubs}, '
                          f'ожидаемый результат - {total_scipubs[0]} для {self.__class__.__name__}', error_messages)
        self.check_assert(count_full_texts >= total_scipubs[1],
                          f'Количество полных текстов не верное. Фактический результат - {count_full_texts}, '
                          f'ожидаемый результат - {total_scipubs[1]} для {self.__class__.__name__}', error_messages)
        if error_messages:
            pytest.fail("\n".join(error_messages))


    def should_be_total_rosrid(self):
        self.scroll_to_elements(4)
        general_statistics_locator = (By.CSS_SELECTOR, MainPageLocators.TITLE_OF_ELEMENT_IN_INFO_FOR_USERS[1].format(4))
        general_statistics = self.should_be_element(general_statistics_locator, 'Статистика для элемента не найдена')
        statistics_list = general_statistics.text.splitlines()
        count_niokr, count_rid, count_ikrbs, count_diss = (int(statistics_list[2].strip().replace(' ', '')),
                                                           int(statistics_list[4].strip().replace(' ', '')),
                                                           int(statistics_list[6].strip().replace(' ', '')),
                                                           int(statistics_list[8].strip().replace(' ', '')))
        error_messages = []
        self.check_assert(count_niokr == ConstMainPage.description_rosrid[1],
                          f'Количество НИОКР не верное. Фактический результат - {count_niokr} Ожидаемый результат - '
                          f'{ConstMainPage.description_rosrid[1]} для {self.__class__.__name__}', error_messages)
        self.check_assert(count_rid == ConstMainPage.description_rosrid[3],
                          f'Количество РИД не верное. Фактический результат - {count_rid} Ожидаемый результат - '
                          f'{ConstMainPage.description_rosrid[3]} для {self.__class__.__name__}', error_messages)
        self.check_assert(count_ikrbs == ConstMainPage.description_rosrid[5],
                          f'Количество ИКРБС не верное. Фактический результат - {count_ikrbs} Ожидаемый результат - '
                          f'{ConstMainPage.description_rosrid[5]} для {self.__class__.__name__}', error_messages)
        self.check_assert(count_diss == ConstMainPage.description_rosrid[7],
                          f'Количество Диссератаций не верное. Фактический результат - {count_diss} Ожидаемый результат - '
                          f'{ConstMainPage.description_rosrid[7]} для {self.__class__.__name__}', error_messages)
        if error_messages:
            pytest.fail("\n".join(error_messages))


    def should_be_total_patents(self):
        self.scroll_to_elements(4)
        general_statistics_locator = (By.CSS_SELECTOR, MainPageLocators.TITLE_OF_ELEMENT_IN_INFO_FOR_USERS[1].format(5))
        general_statistics = self.should_be_element(general_statistics_locator, 'Статистика для элемента не найдена')
        statistics_list = general_statistics.text.splitlines()
        count_patents, count_full_texts = (int(statistics_list[2].strip().replace(' ', '')),
                                           int(statistics_list[4].strip().replace(' ', '')))
        error_messages = []
        self.check_assert(count_patents == ConstMainPage.description_ya_patents[1],
                          f'Количество патентов не верное. Фактический результат - {count_patents},'
                          f'Ожидаемый результат - {ConstMainPage.description_ya_patents[1]} для {self.__class__.__name__}',
                          error_messages)
        self.check_assert(count_full_texts == ConstMainPage.description_ya_patents[3],
                          f'Количество полных текстов патентов не верное. Фактический результат - '
                          f'{count_full_texts} Ожидаемый результат - {ConstMainPage.description_ya_patents[3]} для '
                          f'{self.__class__.__name__}', error_messages)
        if error_messages:
            pytest.fail("\n".join(error_messages))


    def should_be_total_ckp_usu(self):
        self.scroll_to_elements(4)
        general_statistics_locator = (By.CSS_SELECTOR, MainPageLocators.TITLE_OF_ELEMENT_IN_INFO_FOR_USERS[1].format(6))
        general_statistics = self.should_be_element(general_statistics_locator, 'Статистика для элемента не найдена')
        statistics_list = general_statistics.text.splitlines()
        count_ckp, count_equipment_ckp, count_services_ckp, count_usu, count_equipment_usu, count_services_usu = \
            (int(statistics_list[2].strip().replace(' ', '')), int(statistics_list[4].strip().replace(' ', '')),
             int(statistics_list[6].strip().replace(' ', '')), int(statistics_list[8].strip().replace(' ', '')),
             int(statistics_list[10].strip().replace(' ', '')), int(statistics_list[12].strip().replace(' ', '')))
        error_messages = []
        self.check_assert(count_ckp == ConstMainPage.description_ckp_usu[1],
                          f'Количество ЦКП не верное. Фактический результат - {count_ckp},'
                          f'Ожидаемый результат - {ConstMainPage.description_ckp_usu[1]} для {self.__class__.__name__}',
                          error_messages)
        self.check_assert(count_equipment_ckp == ConstMainPage.description_ckp_usu[3],
                          f'Количество оборудования ЦКП не верное. Фактический результат - '
                          f'{count_equipment_ckp} Ожидаемый результат - {ConstMainPage.description_ckp_usu[3]} для '
                          f'{self.__class__.__name__}', error_messages)
        self.check_assert(count_services_ckp == ConstMainPage.description_ckp_usu[5],
                          f'Количество услуг ЦПК не верное. Фактический результат - {count_services_ckp},'
                          f'Ожидаемый результат - {ConstMainPage.description_ckp_usu[5]} для {self.__class__.__name__}',
                          error_messages)
        self.check_assert(count_usu == ConstMainPage.description_ckp_usu[7],
                          f'Количество УНУ не верное. Фактический результат - '
                          f'{count_usu} Ожидаемый результат - {ConstMainPage.description_ckp_usu[7]} для '
                          f'{self.__class__.__name__}', error_messages)
        self.check_assert(count_equipment_usu == ConstMainPage.description_ckp_usu[9],
                          f'Количество оборудования УНУ не верное. Фактический результат - {count_equipment_usu},'
                          f'Ожидаемый результат - {ConstMainPage.description_ckp_usu[9]} для {self.__class__.__name__}',
                          error_messages)
        self.check_assert(count_services_usu == ConstMainPage.description_ckp_usu[11],
                          f'Количество услуг УНУ не верное. Фактический результат - '
                          f'{count_services_usu} Ожидаемый результат - {ConstMainPage.description_ckp_usu[11]} для '
                          f'{self.__class__.__name__}', error_messages)
        if error_messages:
            pytest.fail("\n".join(error_messages))


    def should_be_total_grants(self):
        self.scroll_to_elements(4)
        general_statistics_locator = (By.CSS_SELECTOR, MainPageLocators.TITLE_OF_ELEMENT_IN_INFO_FOR_USERS[1].format(7))
        general_statistics = self.should_be_element(general_statistics_locator, 'Статистика для элемента не найдена')
        statistics_list = general_statistics.text.splitlines()
        count_grants = int(statistics_list[2].strip().replace(' ', ''))
        error_messages = []
        self.check_assert(count_grants == ConstMainPage.description_rnf[1],
                          f'Количество патентов не верное. Фактический результат - {count_grants},'
                          f'Ожидаемый результат - {ConstMainPage.description_rnf[1]} для {self.__class__.__name__}',
                          error_messages)
        if error_messages:
            pytest.fail("\n".join(error_messages))



