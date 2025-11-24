import socket

domain = "sbb.ch"
result = socket.gethostbyname(domain)

print(f"{domain} resolves to {result}")
