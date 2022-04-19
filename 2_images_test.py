from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

global driver
global services
global actual_image
global src


def setup_module():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()


def teardown_module():
    driver.quit()


def test_images_link_present():
    """Зайти на yandex.ru. Ссылка «Картинки» присутствует на странице"""
    driver.get("https://yandex.ru")
    global services
    services = driver.find_element(by=By.XPATH,
                                   value="//div[@class='services-new__item-title' and contains(text(),'Картинки')]")


def test_images_redirect():
    """Кликаем на ссылку. Проверить, что перешли на url https://yandex.ru/images/"""
    services.click()
    sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    assert "https://yandex.ru/images" in driver.current_url


def test_first_category_redirect():
    """Открыть 1 категорию, проверить, что открылась, в поиске верный текст"""
    first_category = driver.find_element(by=By.XPATH, value="//div[@class='PopularRequestList-SearchText']")
    first_category.click()
    text_in_search_field = driver.find_element(by=By.CLASS_NAME, value="input__control")
    assert first_category.text == text_in_search_field.get_attribute('value')
    sleep(5)


def test_open_first_image():
    """Открыть 1 картинку , проверить что открылась"""
    first_image = driver.find_element(by=By.CLASS_NAME, value="serp-item__preview")
    first_image.click()
    global actual_image
    actual_image = driver.find_element(by=By.XPATH, value="//img[@class='MMImage-Origin']")
    sleep(1)  # Ждем пока загрузится полная версия изображения
    width = actual_image.get_attribute("naturalWidth")
    height = actual_image.get_attribute("naturalHeight")
    global src
    src = actual_image.get_attribute("src")
    assert width != 0 and height != 0


def test_next_button_image_change():
    """При нажатии кнопки вперед картинка изменяется"""
    driver.find_element(by=By.CLASS_NAME, value="CircleButton_type_next").click()
    assert actual_image.get_attribute("src") != src


def test_previous_button_image_same():
    """При нажатии кнопки назад картинка изменяется на изображение из шага 6 Необходимо проверить,
    что это то же изображение."""
    driver.find_element(by=By.CLASS_NAME, value="CircleButton_type_prev").click()
    assert actual_image.get_attribute("src") == src
