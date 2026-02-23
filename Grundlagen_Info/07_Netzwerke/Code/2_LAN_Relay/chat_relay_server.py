import socket # Zum Erstellen von Server- und Client-Sockets
import threading # Zum Verwalten mehrerer Clients gleichzeitig
import signal # Zum sauberen Beenden des Servers mit Strg+C
import sys # Zum Beenden des Servers mit sys.exit()

# Ein einfacher Chat-Relay-Server, der Nachrichten von einem Client empfängt und an einen anderen Client weiterleitet.
clients = {}  # verwaltet verbundene Clients: {IP: socket}
ip = "0.0.0.0"  # Auf allen Schnittstellen (interfaces) lauschen
port = 12345  # Port, auf dem der Server läuft

# Einführungstexte, die an neue Clients gesendet werden
intro = [
    "Hallo und herzlich willkommen! Schön, dass du da bist.\n",
    'Deine IP-Adresse ist "{}" - damit kannst du nun Nachrichten versenden und empfangen.\n',
    "Möchtest du jemandem eine Nachricht zukommen lassen?\n",
    'Ganz einfach: Schicke mir die Nachricht in diesem Format: "IP-Adresse:Nachricht"\n',
    'Zum Beispiel so: "192.168.0.22:Hallo Alice!", falls das die IP von Alice ist.\n',
    "Stelle sicher, dass Alice auch online und verbunden ist.\n",
    "Viel Spass beim Chatten!\n",
]


def handle_client(client_socket, client_ip):
    """
    Verarbeitet die Kommunikation mit einem einzelnen Client.
    """
    # Registriere den neuen Client mit seiner IP-Adresse und dem Socket
    clients[client_ip] = client_socket
    try:
        # Sende die Einführungstexte an den neuen Client, formatiert mit seiner IP-Adresse und einem Null-Byte als Trennzeichen
        for message in intro:
            client_socket.send((message.format(client_ip)).encode())

        # Hauptschleife zum Empfangen von Nachrichten vom Client und Weiterleiten an den Empfänger
        while True:
            message = client_socket.recv(1024).decode().strip()

            try:
                # Versuche, die Nachricht im Format "IP-Adresse:Nachricht" zu parsen
                recipient_ip, msg = message.split(":", 1)
                recipient_ip = recipient_ip.strip()
                if recipient_ip in clients:
                    # Sende die Nachricht an den Empfänger, formatiert mit der IP-Adresse des Absenders und einem Null-Byte als Trennzeichen
                    clients[recipient_ip].send(f"From {client_ip}: {msg}".encode())
                else:
                    client_socket.send((f"Empfänger {recipient_ip} ist nicht verbunden.").encode())
            except ValueError:
                # Wenn die Nachricht nicht im erwarteten Format ist, sende eine Fehlermeldung zurück an den Client
                client_socket.send(
                    (
                        'Deine Nachricht muss das Format "IP-Adresse:Nachricht" haben.\x00'
                    ).encode()
                )
                client_socket.send((f'Du hast "{message}" geschickt.\x00').encode())
    except Exception as error:
        print("Error occurred:", repr(error))
        print(f"Closing connection to {client_ip}")
        client_socket.close()
        if client_ip in clients:
            del clients[client_ip]


def accept_clients():
    while True:
        # Akzeptiere eine neue Verbindung von einem Client und starte einen neuen Thread, um die Kommunikation mit diesem Client zu verwalten
        client_socket, client_address = server_socket.accept()
        print(f"Neuer client akzeptiert: {client_address}, auf Socket {client_socket}")
        threading.Thread(
            target=handle_client, args=(client_socket, client_address[0]), daemon=True
        ).start()


def shutdown(signum, frame):
    print("Shutting down the server...")
    for client_socket in list(clients.values()):
        try:
            client_socket.close()
        except:
            pass
    try:
        server_socket.close()
    except:
        pass
    sys.exit(0)


# Registriere die Signalbehandlung für SIGINT (Strg+C), um den Server sauber herunterzufahren
signal.signal(signal.SIGINT, shutdown)

# Erstelle den Server-Socket, binde ihn an die IP-Adresse und den Port, und starte das Akzeptieren von Clients
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Setze die Option SO_REUSEADDR, um die Wiederverwendung des Ports zu ermöglichen, falls der Server neu gestartet wird
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binde den Socket an die IP-Adresse und den Port, und starte das Lauschen auf eingehende Verbindungen
server_socket.bind((ip, port))

# Starte das Akzeptieren von Clients in einem separaten Thread, damit der Hauptthread weiterhin Verbindungsanfragen akzeptieren kann
server_socket.listen()
print("Server up")

# Akzeptiere Clients in einer Endlosschleife, bis der Server mit Strg+C heruntergefahren wird
accept_clients()

# NOTE: Was ist ein Thread? Ein Thread ist ein leichter Ausführungsstrang innerhalb eines Prozesses. Er ermöglicht es, mehrere Aufgaben gleichzeitig auszuführen, ohne dass sie sich gegenseitig blockieren. In diesem Server wird für jeden verbundenen Client ein eigener Thread gestartet, um die Kommunikation mit diesem Client zu verwalten, während der Hauptthread weiterhin neue Verbindungsanfragen akzeptieren kann.