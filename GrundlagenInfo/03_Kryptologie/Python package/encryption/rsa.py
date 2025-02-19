from rsa_aux import *

def rsa_encrypt(text, e, n):
    # 1. Text in Liste von Zahlen umwandeln
    l_txt = []
    for b in text:
        l_txt.append(ord(b)-64)

    print(l_txt)

    # Liste von Zahlen verschlüsseln (neue Liste verschlüsselter Zahlen erstellen)
    l_enc = []
    for z in l_txt:
        l_enc.append(z ** e % n)
    return l_enc


def rsa_decrypt(l_enc, d, n):
    # 3. Liste von Zahlen entschlüsseln (in neuer Liste speichern)
    l_dec = []
    for z in l_enc:
        l_dec.append(z**d % n)

    print(l_dec)

    # 4. Liste entschlüsselter Zahlen in entschlüsselten Text umwandeln
    text_dec = ""
    for z in l_dec:
        text_dec += chr(z+64)

    return text_dec

def rsa_keygen(p, q):
    n = p*q
    phi_n = (p-1)*(q-1)
    e = find_coprime(phi_n)
    d = modular_inverse(e, phi_n)
    return e, d, n

# e, d, n = rsa_keygen(89,97)
e, d, n = rsa_keygen(3,11)
#e, d, n = rsa_keygen(3,11)
print(e,d,n)

text = "ICHBINSEHRGLUECKLICKSIEHEUTEZUSEHEN"
#e = 7 # public key
#d = 3 # private key
#n = 33
l_enc = rsa_encrypt(text, e, n)
l_dec_txt = rsa_decrypt(l_enc, d, n)
print(l_enc)
print(l_dec_txt)