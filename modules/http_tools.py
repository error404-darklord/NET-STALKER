import requests

def http_get():
    url = input("Введите URL для HTTP GET запроса: ").strip()
    try:
        r = requests.get(url)
        print(f"Статус: {r.status_code}")
        print("Первые 500 символов ответа:")
        print(r.text[:500])
    except Exception as e:
        print(f"Ошибка: {e}")

def http_post():
    url = input("Введите URL для HTTP POST запроса: ").strip()
    data = input("Введите данные POST (например, key=value&foo=bar): ")
    try:
        r = requests.post(url, data=data)
        print(f"Статус: {r.status_code}")
        print("Ответ:")
        print(r.text[:500])
    except Exception as e:
        print(f"Ошибка: {e}")
