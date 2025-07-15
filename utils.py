import os
import datetime

# Функция для захвата скриншота
def take_screenshot(browser, test_name):
    # Создаем директорию для скриншотов, если она не существует
    screenshots_dir = r"C:\Users\ealekseeva\PycharmProjects\regress_test_ias_UI\screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    # Генерируем имя файла для скриншота
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_file = os.path.join(screenshots_dir, f"{timestamp}.png")

    # Сохраняем скриншот
    browser.save_screenshot(screenshot_file)
    print(f"Screenshot saved: {screenshot_file}")

    return screenshot_file


# Хук для обработки результатов тестов
def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        # Если тест не прошел, делаем скриншот
        browser = item.funcargs['browser']  # Получаем драйвер из фикстуры
        take_screenshot(browser, item.name)

