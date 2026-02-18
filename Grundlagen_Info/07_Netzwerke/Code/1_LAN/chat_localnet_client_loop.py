import socket

PORT = 12345
IP_ADDRESS = "10.62.90.171" # IP-Adresse des Servers im lokalen Netzwerk

# Client-Socket erstellen und mit dem Server verbinden
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Erstelle einen TCP-IP Socket
client.connect((IP_ADDRESS, PORT))  # Verbinde den Socket mit dem Server auf localhost und dem definierten Port


try:
    # Endlosschleife für den Nachrichtenaustausch
    while True:
        nachricht = input("Nachricht an den Server: ")
        client.send(nachricht.encode())

        antwort = client.recv(1024).decode()
        print("Antwort vom Server:", antwort)
except KeyboardInterrupt:
    print(f"Verbindung zum Server ({IP_ADDRESS}) wird getrennt.")
    client.close()

