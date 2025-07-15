from .base_page import BasePage
from .locators import NewsPageLocators
from .const_and_test_data import ConstNewsPage, Env

class NewsPage(BasePage):

    def should_be_page_news(self):
        title = self.should_be_element(NewsPageLocators.TITLE_MAIN_PAGE, 'Заголовок на странице не найден')
        path_segment = ConstNewsPage.news_path
        expected_string = ConstNewsPage.title_in_news_page
        url = Env.MAIN_LINK + path_segment
        self.should_be_true_url(path_segment)
        self.should_be_correct_title(title, expected_string)


    def go_to_news_page(self, title_date_icon_link_data, page, news):
        try:
            assert page in title_date_icon_link_data, (f'Модуль бегущей строки новостей. {page}-страница отсутствует в'
                                                       f' контейнере фикстуры title_date_icon_link_data. '
                                                       f'Перейти на страницы новостей с {page}-страницы модуля '
                                                       f'бегущей строки невозможно. для {self.__class__.__name__}. '
                                                       f'{self.take_screenshot_message()}')
            news_attributes = title_date_icon_link_data[page].get(news)
            assert news_attributes is not None, (f'Модуль бегущей строки новостей. Данные для {news}-новости на странице'
                                                 f' {page} отсутствует в контейнере фикстуры title_date_icon_link_data.'
                                                 f'Перейти на страницу новости из модуля бегущей строки невозможно. '
                                                 f'для {self.__class__.__name__}. {self.take_screenshot_message()}')
            link = news_attributes.get("link")
            assert link, (f'Модуль бегущей строки новостей. На {page}-странице для {news}-новости отсутствует ссылка в '
                          f'контейнере фикстуры title_date_icon_link_data. Перейти на страницу новости из модуля '
                          f'бегущей строки невозможно для {self.__class__.__name__}. {self.take_screenshot_message()}')
            self.browser.get(link)
        except Exception as e:
            print(f"Ошибка при переходе на страницу новостей: {e}, {type(e)}")
        else:
            return link



    def should_be_date(self, link):
        try:
            date = self.find_element(*NewsPageLocators.DATE)
            assert date.text.strip() is not None, (f'На странице новости {link} отсутствует дата для '
                                                   f'{self.__class__.__name__}. {self.take_screenshot_message()}')
        except Exception as e:
            print(f"Ошибка при проверке даты новости на ее странице: {e}, {type(e)}")
        else:
            return date.text.strip()


    def should_be_type_icon(self, link):
        try:
            locator_icon = self.find_element(*NewsPageLocators.ICON)
            type_icon = locator_icon.get_attribute('class')
            assert type_icon is not None, (f'На странице новости {link} отсутствует значок типа новости для '
                                           f'{self.__class__.__name__}. {self.take_screenshot_message()}')
        except Exception as e:
            print(f"Ошибка при проверке типа новости на ее странице: {e}, {type(e)}")
        else:
            return type_icon


    def should_be_description_icon(self, link):
        try:
            description_icon = self.find_element(*NewsPageLocators.DESCRIPTION_ICON)
            assert description_icon.text is not None, (f'На странице новости {link} отсутствует описание типа новости '
                                                       f'для {self.__class__.__name__}. '
                                                       f'{self.take_screenshot_message()}')
        except Exception as e:
            print(f"Ошибка при проверке описания к типу новости на ее странице: {e}, {type(e)}")
        else:
            return description_icon.text


    def should_be_title_on_each_news(self, link):
        try:
            title = self.find_element(*NewsPageLocators.TITLE)
            assert title.text is not None, (f'На странице новости {link} отсутствует заголовок (тест -'
                                            f'для {self.__class__.__name__}. {self.take_screenshot_message()}')
        except Exception as e:
            print(f"Ошибка при проверке заголовка новости на ее странице: {e}, {type(e)}")
        else:
            return title.text.lower().replace("<b>", "").replace("</b>", "")


    def should_be_title_equal_with_title_in_hot_news(self, link, title_date_icon_link_data, title_from_page, page, news):
        try:
            title_from_hot_news = title_date_icon_link_data.get(page, {}).get(news, {}).get('title')
            assert title_from_page == title_from_hot_news, (f'Заголовки новостей: из бегущей строки ({page}-страница, '
                                                        f'{news}-новость) и на странице самой новости ({link}) не '
                                                        f'совпадают. Заголовок на странице новости - {title_from_page},'
                                                        f' заголовок в бегущей строке - {title_from_hot_news}. '
                                                        f'{self.take_screenshot_message()}')
        except Exception as e:
            print(f"Ошибка при проверке заголовков (новости из бегущей строки и на странице новости): {e}, {type(e)}")


    def should_be_date_equal_with_date_in_hot_news(self, link, title_date_icon_link_data, date_from_page, page, news):
        try:
            date_from_hot_news = title_date_icon_link_data.get(page, {}).get(news, {}).get('date')
            assert date_from_page == date_from_hot_news, (
                f'Дата у новостей: из бегущей строки ({page}-страница, {news}-новость) и на '
                f'странице самой новости ({link}) не совпадает. Дата на странице новости - '
                f'{date_from_page}, дата в бегущей строке - {date_from_hot_news} '
                f'{self.take_screenshot_message()}')
        except Exception as e:
            print(f"Ошибка при проверке даты (новости из бегущей строки и на странице новости): {e}, {type(e)}")


    def should_be_type_icon_equal_with_type_icon_in_hot_news(self, link, title_date_icon_link_data, type_icon_from_page,
                                                             page, news):
        try:
            icon = {
                'fal fa-microscope': ConstNewsPage.title_icon_scipub_in_hot_news,
                'fal fa-newspaper': ConstNewsPage.title_icon_smi_in_hot_news
            }
            type_icon_page = icon.get(type_icon_from_page, 'Неизвестный тип')
            type_icon_from_hot_news = title_date_icon_link_data.get(page, {}).get(news, {}).get('type')
            type_icon_hot_news = icon.get(type_icon_from_hot_news, 'Неизвестный тип')
            assert type_icon_from_page == type_icon_from_hot_news, (
                f'Значок типа новостей: у новости из бегущей строки ({page}-страница, {news}-новость) и на '
                f'странице самой новости ({link}) не совпадает. Тип новости на странице новости - '
                f'{type_icon_page}, тип новости в бегущей строке - {type_icon_hot_news}. '
                f'{self.take_screenshot_message()}'
            )
        except Exception as e:
            print(f"Ошибка при проверке типа новости (новости из бегущей строки и на странице новости): {e}, {type(e)}")


    def should_be_description_icon_equal_with_description_icon_in_hot_news(self, link, title_date_icon_link_data,
                                                                           description_icon, page, news):
        try:
            description = {
                'Горячие новости': ConstNewsPage.description_icon_smi_in_hot_news,
                'Публикации': ConstNewsPage.description_icon_scipub_in_hot_news
            }
            description_icon_on_page = description.get(description_icon, 'Неизвестное описание')
            description_icon_from_hot_news = (title_date_icon_link_data.get(page, {})
                                              .get(news, {}).get('description_icon'))
            assert description_icon_on_page == description_icon_from_hot_news, (
                f'Описание типа новостей: у новости из бегущей строки ({page}-страница, {news}-новость) и на '
                f'странице самой новости ({link}) не совпадает. Тип новости на странице новости - '
                f'{description_icon} ({description_icon_on_page}), тип новости в бегущей строке - '
                f'{description_icon_from_hot_news}. {self.take_screenshot_message()}'
            )
        except Exception as e:
            print(f"Ошибка при проверке описания к типу новости (новости из бегущей строки и на странице новости): {e}, "
                  f"{type(e)}")





