from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

global driver
global search_field
global serp_list_children

AMOUNT_OF_SEARCH = 5
SEARCH = 'тензор'
LINK = 'tensor.ru'


def setup_module():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()


def teardown_module():
    driver.quit()


def test_search_field_present():
    """Зайти на yandex.ru. Проверить наличие поля поиска"""
    global search_field
    driver.get("https://yandex.ru")
    search_field = driver.find_element(by=By.CLASS_NAME, value="input__control")


def test_popup_shown():
    """Ввести в поиск Тензор. Проверить, что появилась таблица с подсказками (suggest)"""
    search_field.send_keys(SEARCH)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'mini-suggest__popup')))


def test_search_table():
    """При нажатии Enter появляется таблица результатов поиска"""
    search_field.send_keys(Keys.RETURN)
    global serp_list_children
    serp_list_children = driver.find_elements(by=By.CLASS_NAME, value="serp-item")


def test_tensor_present():
    """В первых 5 результатах есть ссылка на tensor.ru (понимаю, как 'обязательно присутствует во всех пяти')"""
    tensor_count = 0
    for i in range(min(AMOUNT_OF_SEARCH, len(serp_list_children))):
        elem = serp_list_children[i].find_element(by=By.CLASS_NAME, value='Link')
        if LINK in elem.get_attribute("href"):
            tensor_count += 1
    assert tensor_count == 5, 'Error - no tensor in the first five results'
