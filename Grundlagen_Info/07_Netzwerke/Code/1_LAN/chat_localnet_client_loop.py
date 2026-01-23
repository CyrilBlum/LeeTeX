import socket

SERVER_LOCAL_IP = "192.168.0.15"

# Erstelle einen TCP/IP-Socket (ein Socket ist ein Endpunkt für die Kommunikation). 
# Sockets vs. Ports: Ein Socket ist eine Kombination aus IP-Adresse, Portnummer, und Protokoll (TCP oder UDP), die zusammen einen eindeutigen Endpunkt für die Kommunikation im Netzwerk bilden.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(
    socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
)  # Erlaube die Wiederverwendung des Ports (nützlich beim Neustart des Servers)
client.connect((SERVER_LOCAL_IP, 12345))

try:
    while True:
        nachricht = input("Nachricht an den Server: ")
        client.send(nachricht.encode())

        antwort = client.recv(1024).decode()
        print("Antwort vom Server:", antwort)
except KeyboardInterrupt:
    print(f"Verbindung zum Server ({SERVER_LOCAL_IP}) wird getrennt.")
    client.close()
