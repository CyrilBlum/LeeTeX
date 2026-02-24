import socket
import threading
import time

SERVER_IP = "172.20.10.5"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, 12345))

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
time.sleep(1)  # Kurze Pause, um sicherzustellen, dass der Empfangsthread gestartet ist

try:
    while True:
        empfaenger = input("Empfänger-IP: ")
        nachricht = input("Nachricht: ")
        client.send(f"{empfaenger}:{nachricht}".encode())
        time.sleep(0.1)  # Kurze Pause, bevor die nächste Nachricht gesendet werden kann
except KeyboardInterrupt:
    print(f"\nVerbindung zum Server ({SERVER_IP}) wird getrennt.")
    client.close()