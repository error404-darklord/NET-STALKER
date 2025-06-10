from urllib.parse import urlparse

def url_info():
    url = input("Введите URL для разбора: ").strip()
    parsed = urlparse(url)
    print(f"Схема: {parsed.scheme}")
    print(f"Хост: {parsed.hostname}")
    print(f"Порт: {parsed.port}")
    print(f"Путь: {parsed.path}")
    print(f"Параметры: {parsed.params}")
    print(f"Запрос: {parsed.query}")
    print(f"Фрагмент: {parsed.fragment}")
    print(f"Пользователь: {parsed.username}")
    print(f"Пароль: {parsed.password}")
