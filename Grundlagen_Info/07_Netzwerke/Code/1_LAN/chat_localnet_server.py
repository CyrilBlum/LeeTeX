import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Erlaube die Wiederverwendung des Ports (nützlich beim Neustart des Servers)
server.bind(("192.168.1.18", 12345))
server.listen(1)
print("Warte auf Verbindung...")

conn, addr = server.accept()
print("Verbunden mit:", addr)

nachricht = conn.recv(1024).decode()
print("Empfangen:", nachricht)

conn.send("Nachricht erhalten!".encode())

conn.close()
server.close()