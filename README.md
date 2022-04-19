# Тестирование страницы Яндекс при помощи Selenium

Проверялось на Windows10x64, Chrome 100.0.4896.88 x64

# Подготовка

1. Установить Python3: https://www.python.org/downloads/
2. Установить Chrome
3. Скачать chromedriver: https://chromedriver.storage.googleapis.com/index.html?path=100.0.4896.60/ 
4. Открыть консоль в директории репозитория
5. Установить selenium, pytest, pytest-html: pip install selenium pytest pytest-html

# Запуск

pytest --html=report.html

# Просмотр отчета

Открыть сформированный отчет report.html

# Анализ результатов

Успешным является выполнение всех тестов, кроме test_tensor_present (т.к это соответствует условию задачи - "В первых 5 результатах есть ссылка на tensor.ru")