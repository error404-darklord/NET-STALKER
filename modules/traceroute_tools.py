import subprocess

def traceroute():
    host = input("Введите IP или домен для трассировки: ").strip()
    print(f"Трассировка маршрута до {host}...")
    try:
        subprocess.run(['traceroute', host])
    except Exception as e:
        print(f"Ошибка: {e}")
