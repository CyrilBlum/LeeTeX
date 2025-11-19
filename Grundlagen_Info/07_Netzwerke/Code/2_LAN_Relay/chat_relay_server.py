import socket
import threading
import signal
import sys
import time

clients = {}          # key=IP, value=(socket, msg_count, last_reset)
ip = '0.0.0.0'        # Listen on all interfaces
port = 43223          # Port to listen on
rate_limit = 10.      # Max messages per client per rate_interval
rate_interval = 10.   # Time interval in seconds for rate limiting

intro = [
    "Hallo und herzlich willkommen! Schön, dass du da bist.\n",
    "Deine IP-Adresse ist \"{}\" - damit kannst du nun Nachrichten versenden und empfangen.\n",
    "Möchtest du jemandem eine Nachricht zukommen lassen?\n",
    "Ganz einfach: Schicke mir die Nachricht in diesem Format: \"IP-Adresse:Nachricht\"\n",
    "Zum Beispiel so: \"145.40.192.176:Hallo Alice!\", falls das die IP von Alice ist.\n",
    "Stelle sicher, dass Alice auch online und verbunden ist.\n",
    "Viel Spass beim Chatten!\n"
]


def handle_client(client_socket, client_ip):
    clients[client_ip] = (client_socket, 0, time.time())
    try:
        # Send intro
        for message in intro:
            client_socket.send((message.format(client_ip) + "\x00").encode())

        while True:
            socket_data, msg_count, last_reset = clients[client_ip]
            if time.time() - last_reset > rate_interval:
                msg_count = 0
                last_reset = time.time()

            message = client_socket.recv(1024).decode().strip()
            msg_count += 1

            if msg_count > rate_limit:
                raise Exception("Rate limit exceeded")

            try:
                recipient_ip, msg = message.split(':', 1)
                recipient_ip = recipient_ip.strip()
                if recipient_ip in clients:
                    clients[recipient_ip][0].send(
                        f'From {client_ip}: {msg}\x00'.encode())
                else:
                    client_socket.send(
                        (f"Empfänger {recipient_ip} ist nicht verbunden.\x00").encode())
            except ValueError:
                client_socket.send(
                    ("Deine Nachricht muss das Format \"IP-Adresse:Nachricht\" haben.\x00").encode())
                client_socket.send(
                    (f"Du hast \"{message}\" geschickt.\x00").encode())

            clients[client_ip] = (socket_data, msg_count, last_reset)
    except Exception as error:
        print('Error occurred:', repr(error))
        print(f'Closing connection to {client_ip}')
        try:
            client_socket.send(
                "Du sendest zu viele Nachrichten in kurzer Zeit.\x00".encode())
        except:
            pass
        client_socket.close()
        if client_ip in clients:
            del clients[client_ip]


def accept_clients():
    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Accepted new client: {client_address}, on socket {client_socket}')
        threading.Thread(target=handle_client, args=(
            client_socket, client_address[0]), daemon=True).start()


def shutdown(signum, frame):
    print('Shutting down the server...')
    for sock_tuple in list(clients.values()):
        try:
            sock_tuple[0].close()
        except:
            pass
    try:
        server_socket.close()
    except:
        pass
    sys.exit(0)


signal.signal(signal.SIGINT, shutdown)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((ip, port))
server_socket.listen()
print('Server up')

accept_clients()
