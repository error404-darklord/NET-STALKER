from modules import (
    http_tools,
    ping_tools,
    traceroute_tools,
    portscan_tools,
    parse_tools,
    geoip_tools,
    url_tools,
)

ascii_art = r"""
 /$$$$$$$   /$$$$$$  /$$$$$$$  /$$   /$$       /$$        /$$$$$$  /$$$$$$$  /$$$$$$$ 
| $$__  $$ /$$__  $$| $$__  $$| $$  /$$/      | $$       /$$__  $$| $$__  $$| $$__  $$
| $$  \ $$| $$  \ $$| $$  \ $$| $$ /$$/       | $$      | $$  \ $$| $$  \ $$| $$  \ $$
| $$  | $$| $$$$$$$$| $$$$$$$/| $$$$$/        | $$      | $$  | $$| $$$$$$$/| $$  | $$
| $$  | $$| $$__  $$| $$__  $$| $$  $$        | $$      | $$  | $$| $$__  $$| $$  | $$
| $$  | $$| $$  | $$| $$  \ $$| $$\  $$       | $$      | $$  | $$| $$  \ $$| $$  | $$
| $$$$$$$/| $$  | $$| $$  | $$| $$ \  $$      | $$$$$$$$|  $$$$$$/| $$  | $$| $$$$$$$/
|_______/ |__/  |__/|__/  |__/|__/  \__/      |________/ \______/ |__/  |__/|_______/
"""

def main():
    print(ascii_art)
    while True:
        print("☰☰☰  DARK LORD MENU  ☰☰☰")
        print("1. HTTP GET запрос")
        print("2. HTTP POST запрос")
        print("3. Пинг хоста")
        print("4. Трассировка маршрута")
        print("5. Сканирование портов")
        print("6. Парсинг HTML (заголовок и ссылки)")
        print("7. Геолокация IP")
        print("8. Разбор URL")
        print("9. Выход")

        choice = input("Выберите опцию: ").strip()
        if choice == '1':
            http_tools.http_get()
        elif choice == '2':
            http_tools.http_post()
        elif choice == '3':
            ping_tools.ping()
        elif choice == '4':
            traceroute_tools.traceroute()
        elif choice == '5':
            portscan_tools.port_scan()
        elif choice == '6':
            parse_tools.parse_html()
        elif choice == '7':
            geoip_tools.geoip()
        elif choice == '8':
            url_tools.url_info()
        elif choice == '9':
            print("Выход...")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
