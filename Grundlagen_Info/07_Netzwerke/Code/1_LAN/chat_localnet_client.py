import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.1.10", 12345))
client.send("Hallo Server im LAN!".encode())

antwort = client.recv(1024).decode()
print("Antwort vom Server:", antwort)

client.close()
