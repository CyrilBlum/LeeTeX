import socket
import threading # wird benötigt, um Nachrichten gleichzeitig senden sowie empfangen zu können.

SERVER_IP = "192.168.1.23"  # IP-Adresse des Relay-Servers im LAN
SERVER_PORT = 43223

# Client-Socket erstellen und mit dem Server verbinden
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Erstelle einen TCP-IP Socket
client.connect((SERVER_IP, SERVER_PORT))  # Verbinde den Socket mit dem Server

EMPFAENGER_IP = input("Empfänger-IP eingeben: ")  # Lese die IP-Adresse des Empfängers von der Konsole ein

def receive_messages(sock):
    while True:
        try:
            nachricht = sock.recv(1024).decode()
            sender_ip, msg = nachricht.split(":", 1)  # Nachricht in Sender-IP und eigentliche Nachricht aufteilen
            if nachricht:
                print(f"\nNachricht erhalten von {sender_ip}: {msg}")
            else:
                print("\nVerbindung zum Server verloren.")
                break
        except Exception as e:
            print(f"\nFehler beim Empfangen der Nachricht: {e}")
            break
# Starte einen separaten Thread, um Nachrichten vom Server zu empfangen, damit der Hauptthread weiterhin Eingaben vom Benutzer akzeptieren kann. Deamon Thread, damit er automatisch beendet wird, wenn der Hauptthread endet.
threading.Thread(target=receive_messages, args=(client), daemon=True).start()

# Starte eine Endlosschleife, um Nachrichten an den Server zu senden. Der Benutzer kann jederzeit mit Strg+C die Verbindung beenden.
try:
    # Endlosschleife für den Nachrichtenaustausch
    while True:
        

        nachricht = input("Nachricht: ")
        nachricht = f"{EMPFAENGER_IP}:{nachricht}"
        client.send(nachricht.encode())

        antwort = client.recv(1024).decode()
        print("Antwort vom Server:", antwort)

except KeyboardInterrupt:
    print(f"Verbindung zum Server ({SERVER_IP}) wird getrennt.")
    client.close()