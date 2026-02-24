import socket
import threading

SERVER_IP = socket.gethostbyname("cblum.ch")
NAME = input("Gib deinen Namen ein: ")
print(f"cblum.ch wird auf der IP-Adresse {SERVER_IP} aufgelöst.")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, 12345))
client.send(NAME.encode())

def receive_messages():
    while True:
        try:
            nachricht = client.recv(1024).decode()
            if nachricht:
                print(f"\n{nachricht}")
            else:
                print("\nVerbindung zum Server verloren.")
                break
        except:
            break

threading.Thread(target=receive_messages, daemon=True).start()

try:
    while True:
        empfaenger = input("Empfänger: ")
        nachricht = input("Nachricht: ")
        client.send(f"{empfaenger}:{nachricht}".encode())
except KeyboardInterrupt:
    print(f"\nVerbindung zum Server ({SERVER_IP}) wird getrennt.")
    client.close()