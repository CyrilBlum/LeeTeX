def gcd(a, b):
        """Berechnet den größten gemeinsamen Teiler (ggT) mit dem Euklidischen Algorithmus."""
        while b:
            a, b = b, a % b
        return a

def find_coprime(n):
    """Findet die kleinste positive teilerfremde Zahl zu n."""
    candidate = 2  # Start bei 2, weil 1 immer teilerfremd ist
    while gcd(n, candidate) != 1:
        candidate += 1
    return candidate

def extended_gcd(a, b):
    """Berechnet den erweiterten Euklidischen Algorithmus.
    Gibt (gcd, x, y) zurück, sodass a*x + b*y = gcd(a, b).
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(e, phi_n):
    """Berechnet das modulare Inverse von e modulo phi_n."""
    gcd, x, _ = extended_gcd(e, phi_n)
    if gcd != 1:
        raise ValueError("Kein modulares Inverses existiert für e und phi_n.")
    return x % phi_n  
        
    