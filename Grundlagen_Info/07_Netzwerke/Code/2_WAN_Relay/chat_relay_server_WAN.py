import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 12345))
server.listen()

clients = []
names = []

def handle_client(client):
    while True:
        try:
            nachricht = client.recv(1024).decode()
            if not nachricht:
                break
            empfaenger, nachricht = nachricht.split(":", 1)
            if empfaenger in names:
                index = names.index(empfaenger)
                sender_name = names[clients.index(client)]
                clients[index].send(f"{sender_name}: {nachricht}".encode())
        except:
            break
    
    # Cleanup
    index = clients.index(client)
    name = names[index]
    client.close()
    clients.remove(client)
    names.remove(name)
    print(f"{name} hat die Verbindung getrennt.")

while True:
    client, addr = server.accept()
    name = client.recv(1024).decode()
    clients.append(client)
    names.append(name)
    print(f"{name} hat sich verbunden.")
    threading.Thread(target=handle_client, args=(client,), daemon=True).start()