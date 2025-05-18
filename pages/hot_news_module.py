import inspect
import time
from datetime import datetime, timedelta
import re

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from .locators import HotNewsLocators
from .base_page import BasePage
from .const_and_test_data import Const


class HotNewsModule(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)


    def total_pages(self):
        try:
            counter_hot_news = self.find_element(*HotNewsLocators.COUNTER_NEWS).text
            total_pages = int(re.search(r'из (\d+)', counter_hot_news).group(1))
            assert total_pages > 0, (f"В модуле бегущей строки новостей общее количество страниц должно быть больше 0. "
                                     f" для {self.__class__.__name__}"
                                     f"{self.take_screenshot_message()}")
        except Exception as e:
            print(f"Ошибка при подсчете количества cтраниц в модуле бегущей строки новостей: {e}, {type(e)}")
        else:
            return total_pages


    def total_news(self):
        try:
            counter_hot_news = self.find_element(*HotNewsLocators.COUNTER_NEWS).text
            total_news = int(re.search(r'Всего:\s*(\d+)', counter_hot_news).group(1))
            assert total_news > 0, (f"В модуле бегущей строки новостей общее количество новостей должно быть больше 0. "
                                     f" для {self.__class__.__name__}"
                                     f"{self.take_screenshot_message()}")
        except Exception as e:
            print(f"Ошибка при подсчете общего количества новостей в модуле бегущей строки новостей: {e}, {type(e)}")
        else:
            return total_news


    def should_be_five_hot_news_on_page(self, page):
        try:
            list_news = self.browser.find_elements(*HotNewsLocators.LIST_NEWS)
            count_hot_news = len(list_news)
            assert count_hot_news == 5, (f"В модуле бегущей строки новостей на {page}-странице количество новостей "
                                         f"не равно 5-ти. ФР - {count_hot_news}. "
                                         f" для {self.__class__.__name__}"
                                         f"{self.take_screenshot_message()}")
        except Exception as e:
            print(f"Ошибка при подсчете количества новостей на странице в модуле бегущей строки: {e}, {type(e)}")
        else:
            return count_hot_news


    def go_to_next_page_in_hot_news(self):
        try:
            next_page_hot_news = self.find_element(*HotNewsLocators.NEXT_HOT_NEWS)
            self.should_be_no_attribute_with_value(HotNewsLocators.NEXT_HOT_NEWS, "class", "opacity-50")
            next_page_hot_news.click()
        except Exception as e:
            print(f"Ошибка при переходе на следующую страницу в модуле бегущей строки новостей: {e}, {type(e)}")


    def go_to_set_page_in_hot_news_and_get_attributes(self, page, news, dict_data):
        try:
            while True:
                counter_hot_news = self.find_element(*HotNewsLocators.COUNTER_NEWS).text
                if f"Страница {page} из " in counter_hot_news:
                    locator_title_hot_news = self.find_element(By.CSS_SELECTOR, HotNewsLocators.TITLE_OF_NEWS[1].format(news))
                    title_hot_news_lower = locator_title_hot_news.get_attribute('title').lower()
                    title_hot_news = title_hot_news_lower.replace("<b>", "").replace("</b>", "")

                    link = locator_title_hot_news.get_attribute("href")

                    locator_date_of_each_news = self.find_element(By.CSS_SELECTOR,
                                                                  HotNewsLocators.DATE_OF_NEWS[1].format(news))
                    date_of_each_news = locator_date_of_each_news.text.strip()

                    locator_icon = self.find_element(By.CSS_SELECTOR, HotNewsLocators.ICON[1].format(news))
                    description_icon = locator_icon.get_attribute('title')
                    type_icon = locator_icon.get_attribute('class')

                    page_data = dict_data.setdefault(page, {})
                    page_data[news] = {"title": title_hot_news, "date": date_of_each_news,
                                       "type": type_icon, "description_icon": description_icon, "link": link}
                    print(dict_data)
                    break
                else:
                    next_page_hot_news = WebDriverWait(self.browser, 5).until(
                        EC.visibility_of_element_located(HotNewsLocators.NEXT_HOT_NEWS)
                    )

                    if 'opacity-50' not in next_page_hot_news.get_attribute('class'):
                        next_page_hot_news.click()
                        time.sleep(2)
                        # WebDriverWait(self.browser, 5).until_not(
                        #     EC.presence_of_element_located((By.CSS_SELECTOR, "ul.hotnews.loading-rtl"))
                        # )
        except Exception as e:
            print(f"Ошибка при переходе на следующую страницу {page + 1}: {e}")


    def should_be_actual_date_in_hot_news(self, title_date_and_icon_data, page, news):
        try:
            attributes = title_date_and_icon_data.get(page, {}).get(news)
            # print(f"title_date_and_icon_data: {title_date_and_icon_data}")
            date = attributes.get("date")
            icon = attributes.get("description_icon")
            assert icon, (f"В модуле бегущей строки новостей Тип новости на {page}-странице у {news}-новости отсутствует.")
            if icon == Const.icon_scipub:
                pytest.skip(f"Пропустили тесты для {news}-новости, так как у нее тип новости - Публикации.")
            elif icon == Const.icon_smi:
                date.strip()
                assert date.strip(), (f"В модуле бегущей новостей строки Дата на {page}-странице у {news}-новости "
                                      f"отсутствует. ФР - {date.strip()}")
                try:
                    date_with_format = datetime.strptime(date.strip(), "%d.%m.%Y")
                except ValueError:
                    raise AssertionError(f"Некорректный формат даты: {date}. Дата без пробелов - {date.strip()}. "
                                         f"Дата по формату - {date_with_format}. Ожидался формат 'дд.мм.гггг'.")
                get_current_date = datetime.now().strftime("%d.%m.%Y")
                current_date = datetime.strptime(get_current_date, "%d.%m.%Y")
                delta = current_date - timedelta(days=5)
                assert date_with_format >= delta, (f"В модуле бегущей строки новости СМИ не актуальны. "
                                                   f"{news}-новость на {page}-й странице имеет дату -"
                                                   f"{date_with_format}.  Текущая дата {current_date}. "
                                                   f"(тест -для "
                                                   f"{self.__class__.__name__}"
                                                    f"{self.take_screenshot_message()}.")
        except Exception as e:
            print(f"Ошибка при проверке актуальности даты новости в модуле бегущей строки новостей: {e}, {type(e)}")


    def should_be_title_in_hot_news(self, title_date_icon_data, page, news):
        try:
            attributes = title_date_icon_data.get(page, {}).get(news)
            title = attributes.get("title")
            assert title, (f'В модуле бегущей строки новостей Заголовок на {page}-странице у {news}-новости '
                                   f'отсутствует (тест -для '
                                       f'{self.__class__.__name__}. {self.take_screenshot_message()}')
        except Exception as e:
            print(f"Ошибка при проверке наличия заголовка новости в модуле бегущей строки новостей: {e}, {type(e)}")


    def should_be_icon_in_hot_news(self, title_date_icon_data, page, news):
        try:
            attributes = title_date_icon_data.get(page, {}).get(news)
            icon = attributes.get("type")
            assert icon, (f'В модуле бегущей строки новостей Тип новости на {page}-странице у {news}-новости '
                          f'отсутствует для {self.__class__.__name__}. {self.take_screenshot_message()}')
        except Exception as e:
            print(f"Ошибка при проверке наличия иконки типа новости в модуле бегущей строки новостей: {e}, {type(e)}")


    def should_be_link_in_hot_news(self, title_date_icon_data, page, news):
        try:
            attributes = title_date_icon_data.get(page, {}).get(news)
            link = attributes.get("link")
            assert link, (f'В модуле бегущей строки новостей Ссылка для перехода на {page}-страницу у {news}-новости '
                          f'отсутствует для {self.__class__.__name__}. '
                          f'{self.take_screenshot_message()}')
        except Exception as e:
            print(f"Ошибка при проверке наличия ссылки на страницу новости в модуле бегущей строки новостей: {e}, "
                  f"{type(e)}")

    def should_be_link_on_page_news(self):
        try:
            link = self.should_be_element(HotNewsLocators.LINK_ON_PAGE_WITH_ALL_NEWS,
                                                  'В модуле бегущей строки новостей отсутствует ссылка для '
                                                  'перехода на страницу новостей')
        except Exception as e:
            print(f"Ошибка при проверке наличия ссылки на раздел с  новостями в модуле бегущей строки новостей: {e}, "
                  f"{type(e)}")
        else:
            return link


    def should_be_page_news(self):
        try:
            assert (self.browser.current_url in
                    Const.EACH_NEWS_PAGE), (
                f"Переход осуществлен не на страницу 'Новости Медицины' (тест -"
                f"для {self.__class__.__name__}. "
                f"Фактический урл - {self.browser.current_url}. "
                f"Ожидаемый - {Const.EACH_NEWS_PAGE}. "
                f" {self.take_screenshot_message()}")
        except Exception as e:
            print(f"Ошибка при переходе на раздел с новостями из модуля бегущей строки новостей: {e}, {type(e)}")

    def should_be_text_link_on_news_page(self, link):
        try:
            sucsess_text = 'НОВОСТИ МЕДИЦИНЫ'
            assert link.text == sucsess_text, (f'В модуле бегущей строки новостей Текст в ссылке для перехода на страницу '
                                               f'новостей неверный: ожидалось - {sucsess_text}, фактически - {link.text} '
                                               f'для {self.__class__.__name__}. {self.take_screenshot_message()}')
        except Exception as e:
            print(f"Ошибка при проверке текста в ссылке на раздел с новостями в модуле бегущей строки новостей: {e}, "
                  f"{type(e)}")



    def can_equal_total_news_on_each_page_in_hot_news(self, static_total_news, calculated_total_news):
        assert calculated_total_news == 1 * static_total_news, (f'В модуле бегущей строки общее количество новостей '
                                                                    f'не совпадает. В модуле указано - {static_total_news}, '
                                                                    f'фактически подсчитанный результат - '
                                                                    f'{calculated_total_news}'
                                                                    f' для {self.__class__.__name__}. '
                                                                    f'{self.take_screenshot_message()}"')



