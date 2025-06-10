import requests
from bs4 import BeautifulSoup

def parse_html():
    url = input("Введите URL для парсинга HTML: ").strip()
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        print("Заголовок страницы:", soup.title.string if soup.title else "Нет заголовка")
        print("Все ссылки на странице:")
        for link in soup.find_all('a', href=True):
            print(link['href'])
    except Exception as e:
        print(f"Ошибка: {e}")
