import socket

PORT = 12345

# Server-Socket erstellen
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("localhost", PORT))
server.listen(1)
print("Warte auf Verbindung...")

# Verbindung akzeptieren
conn, addr = server.accept()
print(f"Verbunden mit {addr[0]} über Port {addr[1]}")

# Nachricht vom Client empfangen
nachricht = conn.recv(1024).decode()
print(f"Empfangen: {nachricht}")

# Antwort an den Client senden
conn.send("Hallo Client, hier ist der Server!".encode())

conn.close()
server.close()