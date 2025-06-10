import socket

def port_scan():
    host = input("Введите IP или домен для сканирования портов: ").strip()
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]
    print(f"Сканирование портов на {host} (популярные порты)...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Порт {port} открыт")
        sock.close()
