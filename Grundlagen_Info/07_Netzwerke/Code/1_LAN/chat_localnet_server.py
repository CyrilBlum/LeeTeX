import socket

SERVER_IP = "192.168.0.23"  # IP-Adresse des Servers
SERVER_PORT = 12345

# Server-Socket erstellen
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Erstelle einen TCP/IP Socket
server.setsockopt(
    socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
)  # Erlaube die Wiederverwendung des Ports (nützlich beim Neustart des Servers)
server.bind((SERVER_IP, SERVER_PORT))  # Binde den Socket an IP und den definierten Port
server.listen(1)  # Warte auf eingehende Verbindungen (maximal 1 in der Warteschlange)
print("Warte auf Verbindung...")  # Server wartet auf Verbindungen

# Verbindung akzeptieren
conn, addr = server.accept()  # Akzeptiere eine eingehende Verbindung
print(f"Verbunden mit {addr[0]} über Port {addr[1]}")  # Zeige die Adresse und den Port des verbundenen Clients an

# Nachricht vom Client empfangen
nachricht = conn.recv(1024).decode()  # Empfange bis zu 1024 Bytes
print(f"Empfangen: {nachricht}")  # Zeige die empfangene Nachricht an

# Antwort an den Client senden
nachricht = input("Nachricht an den Client eingeben: ")  # Lese eine Nachricht von der Konsole ein
conn.send(nachricht.encode())  # Sende die eingegebene Nachricht an den Client

conn.close()
server.close()
