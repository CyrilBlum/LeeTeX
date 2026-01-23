import socket

# Erstelle einen TCP/IP-Socket (ein Socket ist ein Endpunkt für die Kommunikation). 
# Sockets vs. Ports: Ein Socket ist eine Kombination aus IP-Adresse, Portnummer, und Protokoll (TCP oder UDP), die zusammen einen eindeutigen Endpunkt für die Kommunikation im Netzwerk bilden.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET steht für IPv4, SOCK_STREAM steht für TCP
client.connect(("192.168.0.15", 12345))
client.send("Hallo Server im LAN!".encode())

antwort = client.recv(1024).decode()
print("Antwort vom Server:", antwort)

client.close()
