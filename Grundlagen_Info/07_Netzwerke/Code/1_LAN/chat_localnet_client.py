import socket

SERVER_IP = "192.168.0.23" # IP-Adresse des Servers im lokalen Netzwerk
SERVER_PORT = 12345

# Client-Socket erstellen und mit dem Server verbinden
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Erstelle einen TCP-IP Socket
client.connect((SERVER_IP, SERVER_PORT)) # Verbinde den Socket mit dem Server

# Nachricht vom Benutzer einlesen und an den Server senden
nachricht = input("Nachricht an den Server eingeben: ")
client.send(nachricht.encode())  # Sende die eingegebene Nachricht an den Server

# Antwort vom Server empfangen
antwort = client.recv(1024).decode()  #  Empfange bis zu 1024 Bytes
print("Antwort vom Server:", antwort)  # Zeige die Antwort des Servers an

client.close()
