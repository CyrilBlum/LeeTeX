import socket
import threading

SERVER_HOST = "192.168.1.23"  # anpassen
SERVER_PORT = 5000

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("Verbindung getrennt.")
                break
            print(data.decode(), end="")
        except:
            break

def main():
    username = input("Benutzername: ")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_HOST, SERVER_PORT))

    # Register name
    s.send(f"/register {username}".encode())

    threading.Thread(target=receive_messages, args=(s,), daemon=True).start()

    print("Nachricht senden (für DM: @name text)")
    print("Mit /quit beenden.")

    while True:
        msg = input()
        if msg == "/quit":
            break
        s.send(msg.encode())

    s.close()

if __name__ == "__main__":
    main()
