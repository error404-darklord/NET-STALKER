import subprocess

def ping():
    host = input("Введите IP или домен для пинга: ").strip()
    print(f"Пинг {host}...")
    try:
        subprocess.run(['ping', '-c', '4', host])
    except Exception as e:
        print(f"Ошибка: {e}")
