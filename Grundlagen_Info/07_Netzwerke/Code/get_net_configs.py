"""
Dieses Skript sammelt und zeigt die Netzwerkkonfigurationen eines Geräts an, einschließlich der MAC-Adresse, der lokalen IP-Adresse und der globalen IP-Adresse. Es verwendet die `uuid`-Bibliothek, um die MAC-Adresse zu ermitteln, die `socket`-Bibliothek, um die lokale IP-Adresse zu erhalten, und die `requests`-Bibliothek, um die globale IP-Adresse von einem externen Dienst abzurufen.
"""


# Gibt die MAC-Adresse, lokale und globale IP-Adresse des Geräts aus.
import uuid
import socket
import requests

# Gibt die MAC-Adresse dieses Geräts aus
mac = uuid.getnode()
mac_hex = ":".join(f"{(mac >> ele) & 0xff:02x}" for ele in range(40, -1, -8))
print(f"{'MAC-Adresse dieses Geräts:':35} {mac_hex}")

# Gibt die lokale IP-Adresse dieses Geräts aus
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))  # Google DNS-Server, kein Datenaustausch
ip_local = s.getsockname()[0]
s.close()
print(f"{'Lokale IP-Adresse dieses Geräts:':35} {ip_local}")

# Gibt die globale IP-Adresse dieses Geräts aus
ip_global = requests.get("https://api.ipify.org").text
print(f"{'Globale IP-Adresse dieses Geräts:':35} {ip_global}")
