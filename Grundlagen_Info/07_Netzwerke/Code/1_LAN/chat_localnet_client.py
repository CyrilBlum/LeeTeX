import socket

PORT = 12345
IP_ADDRESS = "10.62.90.171" # IP-Adresse des Servers im lokalen Netzwerk

# Client-Socket erstellen und mit dem Server verbinden
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Erstelle einen TCP-IP Socket
client.connect((IP_ADDRESS, PORT))  # Verbinde den Socket mit dem Server auf localhost und dem definierten Port

# Nachricht vom Benutzer einlesen und an den Server senden
nachricht = input("Nachricht an den Server eingeben: ")
client.send(nachricht.encode())  # Sende die eingegebene Nachricht an den Server

# Antwort vom Server empfangen
antwort = client.recv(1024).decode()  #  Empfange bis zu 1024 Bytes
print("Antwort vom Server:", antwort)  # Zeige die Antwort des Servers an

client.close()
