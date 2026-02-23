import socket
import threading # wird benötigt, um Nachrichten gleichzeitig senden sowie empfangen zu können.
# library importieren, um verzögerung (abwarten) zu ermöglichen, damit der Server Zeit hat, die Nachricht zu verarbeiten und zu senden, bevor der Client versucht, sie zu empfangen.
import time

SERVER_IP = "192.168.1.18"  # IP-Adresse des Relay-Servers im LAN
SERVER_PORT = 12345

# Client-Socket erstellen und mit dem Server verbinden
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Erstelle einen TCP-IP Socket
client.connect((SERVER_IP, SERVER_PORT))  # Verbinde den Socket mit dem Server

def receive_messages():
    while True:
        try:
            nachricht = client.recv(1024).decode()
            if nachricht:
                # Prüfe ob die Nachricht vom Format "From IP: msg" ist (echte Chat-Nachricht)
                if nachricht.startswith("From "):
                    # Entferne "From " am Anfang und splitte bei erstem ":"
                    nachricht = nachricht[5:]  # Entferne "From "
                    sender_ip, msg = nachricht.split(":", 1)
                    print(f"\nNachricht erhalten von {sender_ip.strip()}: {msg.strip()}")
                else:
                    # Server-Nachricht (Intro, Fehler, etc.)
                    print(f"\n{nachricht}")
            else:
                print("\nVerbindung zum Server verloren.")
                break
        except Exception as e:
            print(f"\nFehler beim Empfangen der Nachricht: {e}")
            break
# Starte einen separaten Thread, um Nachrichten vom Server zu empfangen, damit der Hauptthread weiterhin Eingaben vom Benutzer akzeptieren kann. Deamon Thread, damit er automatisch beendet wird, wenn der Hauptthread endet.
threading.Thread(target=receive_messages, daemon=True).start()
time.sleep(1)  # Kurze Verzögerung, damit der Empfangsthread Zeit hat, die Einführungsnachrichten zu empfangen und anzuzeigen, bevor der Benutzer zur Eingabe aufgefordert wird.

# Starte eine Endlosschleife, um Nachrichten an den Server zu senden. Der Benutzer kann jederzeit mit Strg+C die Verbindung beenden.
try:
    # Endlosschleife für den Nachrichtenaustausch
    while True:
        empfaenger_ip = input("Empfänger-IP eingeben: ")

        nachricht = input("Nachricht: ")
        client.send(f"{empfaenger_ip}:{nachricht}".encode())
        # Antworten vom Server werden vom receive_messages Thread empfangen
        time.sleep(1)  # Kurze Verzögerung, damit der Empfangsthread Zeit hat, die Antwort zu empfangen und anzuzeigen, bevor der Benutzer zur nächsten Eingabe aufgefordert wird.

except KeyboardInterrupt:
    print(f"Verbindung zum Server ({SERVER_IP}) wird getrennt.")
    client.close()