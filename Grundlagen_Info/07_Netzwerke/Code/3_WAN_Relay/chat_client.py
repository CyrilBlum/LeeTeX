import socket
import threading

# Deine Hetzner-IP
server_ip = "88.198.193.239"
port = 43223


def receive(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("Verbindung zum Server verloren.")
                break
            # The server may send multiple messages separated by \x00
            for msg in data.decode().split("\x00"):
                if msg.strip():
                    print("\n[Server] " + msg)
        except Exception as e:
            print("[FEHLER beim Empfangen]", e)
            break


def main():
    my_ip = input("Geben Sie Ihre eigene öffentliche IP ein: ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((server_ip, port))
        print(f"Verbunden mit {server_ip}:{port}")

        # Start thread to receive messagesx§
        threading.Thread(target=receive, args=(sock,), daemon=True).start()

        recipient_ip = input("Empfänger-IP: ")
        while True:
            message = input("Nachricht: ")
            combined = f"{recipient_ip}:{message}"
            sock.sendall(combined.encode())


if __name__ == "__main__":
    main()
