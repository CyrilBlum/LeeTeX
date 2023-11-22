#!/usr/bin/env python3

from encryption.viginere import viginere
from encryption.friedmann import *
from encryption.findkey import *

def main():
    # 1. Text hier einfügen
    text_viginere=open('/Users/cyrilwendl/Downloads/encryption/text.txt', ).read()
    print("-",text_viginere)
    # 2. Schlüssel hier einfügen
    key = "KSLEE"

    # folgender code VERschlüsselt den Text
    text_viginere_enc = viginere(text_viginere, key)
    print("Verschlüsselt (Geheimtext): %s" % text_viginere_enc)

    # folgender code ENTschlüsselt den Text
    text_viginere_dec = viginere(text_viginere_enc, key, encrypt=False)
    print("Entschlüsselt (Klartext):   %s" % text_viginere_dec)
    
    n=range(1,10)
    fc=[]
    for i in n:
        fc.append(friedmann_slice(text_viginere_enc,i))
    draw_friedmann(n, fc, turtle=False)
    
    print(findkey(text_viginere_enc, 5))
    
    
        

if __name__ == '__main__':
    main()
