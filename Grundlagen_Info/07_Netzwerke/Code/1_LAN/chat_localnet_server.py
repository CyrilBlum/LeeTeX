import socket

PORT = 12345
IP_ADDRESS = "localhost"

# Erstelle einen TCP/IP-Socket (ein Socket ist ein Endpunkt für die Kommunikation). 
# Sockets vs. Ports: Ein Socket ist eine Kombination aus IP-Adresse, Portnummer, und Protokoll (TCP oder UDP), die zusammen einen eindeutigen Endpunkt für die Kommunikation im Netzwerk bilden.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET steht für IPv4, SOCK_STREAM steht für TCP
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Erlaube die Wiederverwendung des Ports (nützlich beim Neustart des Servers), ansonsten bleibt der Port für eine Weile blockiert
server.bind((IP_ADDRESS, PORT))
server.listen(1)
print("Warte auf Verbindung...")

conn, addr = server.accept()
print("Verbunden mit:", addr)

nachricht = conn.recv(1024).decode()
print("Empfangen:", nachricht)

nachricht = input("Nachricht an den Client eingeben: ")
conn.send(nachricht.encode())

conn.close()
server.close()
