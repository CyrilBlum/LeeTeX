import socket

PORT = 12345

# Client-Socket erstellen und mit dem Server verbinden
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Erstelle einen TCP/IP Socket
client.connect(("localhost", PORT)) # Verbinde den Socket mit dem Server auf localhost und dem definierten Port

# Nachricht an den Server senden
client.send("Hallo Server, hier ist der Client!".encode()) # Sende eine Nachricht an den Server

# Antwort vom Server empfangen
antwort = client.recv(1024).decode() #  Empfange bis zu 1024 Bytes
print("Antwort vom Server:", antwort) # Zeige die Antwort des Servers an

client.close()