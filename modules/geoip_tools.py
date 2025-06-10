import requests

def geoip():
    ip = input("Введите IP для геолокации (или оставьте пустым для собственного IP): ").strip()
    url = f"http://ip-api.com/json/{ip or ''}"
    try:
        r = requests.get(url).json()
        if r['status'] == 'success':
            print(f"Страна: {r.get('country')}")
            print(f"Регион: {r.get('regionName')}")
            print(f"Город: {r.get('city')}")
            print(f"ISP: {r.get('isp')}")
            print(f"Организация: {r.get('org')}")
            print(f"AS: {r.get('as')}")
            print(f"Lat/Lon: {r.get('lat')}, {r.get('lon')}")
        else:
            print("Не удалось получить данные геолокации")
    except Exception as e:
        print(f"Ошибка: {e}")
