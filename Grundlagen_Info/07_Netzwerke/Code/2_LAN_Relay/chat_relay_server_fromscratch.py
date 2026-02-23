import socket
import threading # NEW

SERVER_IP = "192.168.0.23"  # IP-Adresse des Servers
SERVER_PORT = 12345

clients = {}  # Dictionary, um verbundene Clients zu speichern (IP-Adresse als Schlüssel und Socket als Wert)

# Server-Socket erstellen
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Erstelle einen TCP/IP Socket
server.setsockopt(
    socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
)  # Erlaube die Wiederverwendung des Ports (nützlich beim Neustart des Servers)
server.bind((SERVER_IP, SERVER_PORT))  # Binde den Socket an IP und den definierten Port
server.listen()  # Warte auf eingehende Verbindungen
print("Warte auf Verbindung...")  # Server wartet auf Verbindungen


def handle_client(conn, addr):
    clients[addr[0]] = conn  # Speichere die Verbindung des Clients im Dictionary
    # Endlosschleife für den Nachrichtenaustausch
    try:
        while True:
            nachricht = conn.recv(1024).decode()
            try:
                print("Empfangen:", nachricht)
                recipient_ip, message = nachricht.split(":", 1)  # Nachricht in Empfänger-IP und eigentliche Nachricht aufteilen
                if recipient_ip in clients:
                    clients[recipient_ip].send(message.encode())  # Nachricht an den Empfänger senden
                else:
                    conn.send(f"Empfänger {recipient_ip} nicht gefunden.".encode())  # Fehlermeldung zurück an den Sender
            except ValueError:
                conn.send("Ungültiges Nachrichtenformat. Bitte verwenden Sie 'Empfänger-IP:Nachricht'.".encode())  # Fehlermeldung bei ungültigem Format
        
    except Exception as e:
        # wenn ein Fehler auftritt (z.B. Client-Verbindung verloren), entferne den Client aus dem Dictionary und schliesse die Verbindung
        print(f"Verbindung zu {addr} getrennt.")
        if addr[0] in clients:
            del clients[addr[0]]
        conn.close()

def accept_clients():
    while True:
        conn, addr = server.accept()  # Akzeptiere eine eingehende Verbindung
        print(f"Verbunden mit {addr[0]} über Port {addr[1]}")  # Zeige die Adresse und den Port des verbundenen Clients an
        threading.Thread(target=handle_client, args=(conn, addr)).start()  # Starte einen neuen Thread für die Client-Verbindung

# Verbindung akzeptieren
conn, addr = server.accept()  # Akzeptiere eine eingehende Verbindung
print(f"Verbunden mit {addr[0]} über Port {addr[1]}")  # Zeige die Adresse und den Port des verbundenen Clients an


server.close()

