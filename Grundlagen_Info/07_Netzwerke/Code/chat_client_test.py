import socket

def send_message(server_ip, port, message):
    with socket.socket() as s:
        s.connect((server_ip, port))
        s.sendall(message.encode())
        data = s.recv(1024)
        print('Antwort vom Server:', data.decode())

server_ip = "88.198.193.239"
port = 43223
send_message(server_ip, port, "Testnachricht von Client")