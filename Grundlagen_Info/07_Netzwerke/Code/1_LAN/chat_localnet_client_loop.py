import socket

SERVER_IP = "192.168.0.23" # IP-Adresse des Servers im lokalen Netzwerk
SERVER_PORT = 12345

# Client-Socket erstellen und mit dem Server verbinden
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Erstelle einen TCP-IP Socket
client.connect((SERVER_IP, SERVER_PORT))  # Verbinde den Socket mit dem Server

try:
    # Endlosschleife für den Nachrichtenaustausch
    while True:
        nachricht = input("Nachricht an den Server: ")
        client.send(nachricht.encode())

        antwort = client.recv(1024).decode()
        print("Antwort vom Server:", antwort)
except KeyboardInterrupt:
    print(f"Verbindung zum Server ({SERVER_IP}) wird getrennt.")
    client.close()

