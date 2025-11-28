import uuid

mac = uuid.getnode()
mac_hex = ":".join(f"{(mac >> ele) & 0xff:02x}" for ele in range(40, -1, -8))

print(mac_hex)
