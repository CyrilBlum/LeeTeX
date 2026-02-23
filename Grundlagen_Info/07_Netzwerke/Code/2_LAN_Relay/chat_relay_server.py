import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 12345))
server.listen()

clients = []
ips = []

def handle_client(client):
    while True:
        try:
            nachricht = client.recv(1024).decode()
            if not nachricht:
                break
            empfaenger, nachricht = nachricht.split(":", 1)
            if empfaenger in ips:
                index = ips.index(empfaenger)
                sender_ip = ips[clients.index(client)]
                clients[index].send(f"{sender_ip}: {nachricht}".encode())
        except:
            break
    
    # Cleanup
    index = clients.index(client)
    ip = ips[index]
    client.close()
    clients.remove(client)
    ips.remove(ip)
    print(f"{ip} hat die Verbindung getrennt.")

while True:
    client, addr = server.accept()
    client_ip = addr[0]
    clients.append(client)
    ips.append(client_ip)
    print(f"{client_ip} hat sich verbunden.")
    threading.Thread(target=handle_client, args=(client,), daemon=True).start()