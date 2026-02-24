import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("0.0.0.0", 12345))
server.listen()

clients = {}

def handle_client(client):
    while True:
        try:
            nachricht = client.recv(1024).decode()
            if not nachricht:
                break
            empfaenger, nachricht = nachricht.split(":", 1)
            if empfaenger in clients:
                sender_name = [name for name, cl in clients.items() if cl == client][0]
                clients[empfaenger].send(f"{sender_name}: {nachricht}".encode())
            else:
                client.send(f"Empfänger {empfaenger} nicht gefunden.".encode())
        except:
            break
    
    # Cleanup
    name = [name for name, cl in clients.items() if cl == client][0]
    client.close()
    del clients[name]
    print(f"{name} hat die Verbindung getrennt.")

while True:
    client, addr = server.accept()
    name = client.recv(1024).decode()
    clients[name] = client
    print(f"{name} hat sich verbunden.")
    threading.Thread(target=handle_client, args=(client,), daemon=True).start()