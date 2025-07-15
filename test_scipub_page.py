import pytest
import psycopg2


from .pages.scipub_page import SciPubPage
from .pages.const_and_test_data import Const
from .pages.login_page import LoginPage

class Test_BD:

    def test_connect_to_bd(self):
    # Параметры подключения к БД
        db_params = {
            'dbname': 'ias_data',
            'user': 'ealekseeva',
            'password': 'vrn86SilveR@',
            'host': 'an.nir.pak-cspmz.ru',  # или другой хост
            'port': '5432'        # стандартный порт для PostgreSQL
        }
        try:
            # Подключение к базе данных
            connection = psycopg2.connect(**db_params)
            cursor = connection.cursor()

            # Выполнение SQL-запроса
            query = "SELECT sp.id FROM data_mart.sci_pubs sp;"
            cursor.execute(query)
            # Получение данных
            results = cursor.fetchall()
            # Формирование списка из полученных данных
            id_list = [row[0] for row in results]
            # Вывод списка
            print(id_list)
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        finally:
            # Закрытие курсора и соединения
            if cursor:
                cursor.close()
            if connection:
                connection.close()

# @pytest.mark.scipub_page
# class TestSciPubPage:
#     @pytest.fixture(scope="class", autouse=True)
#     def setup(self, module_browser, request):
#         self.login_link = Const.MAIN_LINK
#         self.login_page = LoginPage(module_browser, self.login_link)
#         self.login_page.open()
#         self.login_page.log_in()
#         self.login_page.should_be_authorized_user()
#         self.scipubs = SciPubPage(module_browser, module_browser.current_url)
#         yield
#         self.scipubs.logout()
#         self.scipubs.should_not_be_authorized_user()


