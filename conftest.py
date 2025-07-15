import pytest
import functools
from selenium import webdriver


@pytest.fixture(scope="function")
def browser(request):  # Фикстура для независимых тестов
    print("\nopen browser..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="class")
def module_browser(request):  # Фикстура для зависимых тестов
    print("\nopen browser..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()
