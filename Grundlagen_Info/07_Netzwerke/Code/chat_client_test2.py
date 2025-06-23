import socket

server_ip = "88.198.193.239"
port = 43223

while True:
    ip = input("Empfänger-IP: ")
    message = input("Nachricht: ")
    combined = ip + ":" + message
    with socket.socket() as s:
        s.connect((server_ip, port))
        s.sendall(combined.encode())
        data = s.recv(1024)
        print('Antwort vom Server:', data.decode())