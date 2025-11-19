import socket

SERVER_LOCAL_IP = "192.168.1.18"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Erlaube die Wiederverwendung des Ports (nützlich beim Neustart des Servers)
server.bind((SERVER_LOCAL_IP, 12345))
server.listen(1)
print("Warte auf Verbindung...")

conn, addr = server.accept()
print("Verbunden mit:", addr)

try:
    while True:
        nachricht = conn.recv(1024).decode()
        print("Empfangen:", nachricht)

        antwort = input("Antwort an den Client: ")
        conn.send(antwort.encode())
except KeyboardInterrupt as e:
    print(f"Verbindung zu {addr} getrennt.")
    conn.close()
    server.close()