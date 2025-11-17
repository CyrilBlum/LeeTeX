import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.1.10", 12345))
server.listen(1)
print("Warte auf Verbindung...")

conn, addr = server.accept()
print("Verbunden mit:", addr)

nachricht = conn.recv(1024).decode()
print("Empfangen:", nachricht)

conn.send("Nachricht erhalten!".encode())

conn.close()
server.close()