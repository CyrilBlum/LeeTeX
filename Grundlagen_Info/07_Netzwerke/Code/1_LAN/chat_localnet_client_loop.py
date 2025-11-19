import socket

SERVER_LOCAL_IP = "192.168.1.18"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.1.10", 12345))
try:
    while True:
         nachricht = input("Nachricht an den Server: ")
         client.send(nachricht.encode())
         
         antwort = client.recv(1024).decode()
         print("Antwort vom Server:", antwort)
except KeyboardInterrupt:
    print(f"Verbindung zum Server ({SERVER_LOCAL_IP}) wird getrennt.")
    client.close()