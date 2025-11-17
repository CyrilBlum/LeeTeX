import socket

PORT = 12345

# Client-Socket erstellen und mit dem Server verbinden
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", PORT))

# Nachricht an den Server senden
client.send("Hallo Server, hier ist der Client!".encode())

# Antwort vom Server empfangen
antwort = client.recv(1024).decode()
print("Antwort vom Server:", antwort)

client.close()