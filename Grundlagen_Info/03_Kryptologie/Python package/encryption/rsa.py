def gcd(a, b):
    """
    Hilfsfunktion:
    Berechnet den grössten gemeinsamen Teiler (ggT) mit dem Euklidischen Algorithmus.
    """
    while b:
        a, b = b, a % b
    return a

def find_coprime(n):
    """
    Hilfsfunktion:
    Findet die kleinste positive teilerfremde Zahl zu n.
    """
    candidate = 2  # Start bei 2, weil 1 immer teilerfremd ist
    while gcd(n, candidate) != 1:
        candidate += 1
    return candidate

def extended_gcd(a, b):
    """
    Hilfsfunktion:
    Berechnet den erweiterten Euklidischen Algorithmus.
    Gibt (gcd, x, y) zurück, sodass a*x + b*y = gcd(a, b).
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(e, phi_n):
    """
    Hilfsfunktion:
    Berechnet das modulare Inverse von e modulo phi_n.
    """
    gcd, x, _ = extended_gcd(e, phi_n)
    if gcd != 1:
        raise ValueError("Kein modulares Inverses existiert für e und phi_n.")
    return x % phi_n  

def rsa_encrypt(text, e, n):
    """
    Verschlüsselt eine Klartext-Nachricht mit dem öffentlichen Schlüssel (e,n)
    """
    # 1. Text in Liste von Zahlen umwandeln
    l_txt = []
    for b in text:
        l_txt.append(ord(b))

    # Liste von Zahlen verschlüsseln (neue Liste verschlüsselter Zahlen erstellen)
    l_enc = []
    for z in l_txt:
        l_enc.append(z ** e % n)
    return l_enc


def convert_numbers_to_text(l_num):
    # 4. Liste von Zahlen in Text umwandeln
    text_dec = ""
    for z in l_num:
        text_dec += chr(z)
    return text_dec

def rsa_decrypt(l_enc, d, n):
    """
    Entschlüsselt eine verschlüsselte Nachricht mit dem privaten Schlüssel (d,n)
    """
    # 3. Liste von Zahlen entschlüsseln (in neuer Liste speichern)
    l_dec = []
    for z in l_enc:
        l_dec.append(z**d % n)

    text_dec = convert_numbers_to_text(l_dec)

    return text_dec


def rsa_keygen(p, q):
    """
    Generiert ausgehend von zwei Primzahlen p und q den
    privaten und öffentlichen Schlüssel (gibt e, d und n zurück).
    """
    n = p*q
    phi_n = (p-1)*(q-1)
    e = find_coprime(phi_n)
    d = modular_inverse(e, phi_n)
    return e, d, n

def main():
    """
    Hier testen wir alle obigen Funktionen!
    """

    # Diesen Beispiel-Text wollen wir ver- und entschlüsseln
    text = "ich bin sehr glücklich, Sie heute zu sehen!"

    # Beliebige Primzahlen (bitte unter 500) von hier beziehen: https://de.wikibooks.org/wiki/Primzahlen:_Tabelle_der_Primzahlen_(2_-_100.000)
    p = 389
    q = 317

    # Schlüssel generieren
    e, d, n = rsa_keygen(p, q)
    print("""
    Der Schlüssel ist:
    Öffentlicher Schlüssel (e,n): (%d, %d),
    Privater Schlüssel (d,n): (%d, %d)"""% (e, n, d, n))

    # Nachricht mit eigenem (öffentlichen) Schlüssel verschlüsseln
    l_enc = rsa_encrypt(text, e, n)
    
    # Nachricht mit eigenem (privaten) Schlüssel entschlüsseln
    l_dec_txt = rsa_decrypt(l_enc, d, n)
    print("Verschlüsselte Nachricht: ", convert_numbers_to_text(l_enc))
    print("Entschlüsselte Nachricht: ", l_dec_txt)

main()