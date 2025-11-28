# this file will get the MAC address of the machine, the local IP and the global IP address.
import uuid
import socket
import requests

# Get MAC address
mac = uuid.getnode()
mac_hex = ":".join(f"{(mac >> ele) & 0xff:02x}" for ele in range(40, -1, -8))
print(f"{'MAC-Adresse dieses Geräts:':35} {mac_hex}")

# Get local IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))  # Google DNS, no packets sent
ip_local = s.getsockname()[0]
s.close()
print(f"{'Lokale IP-Adresse dieses Geräts:':35} {ip_local}")

# Get global IP address
ip_global = requests.get("https://api.ipify.org").text
print(f"{'Globale IP-Adresse dieses Geräts:':35} {ip_global}")
