#!/usr/bin/env python3

from encryption.viginere import *
from encryption.friedmann import *
from encryption.findkey import *
from encryption.helpers import *

def main():
    # 1. Text hier einfügen
    text_viginere=open('./encryption/text.txt', ).read()
    print("-",text_viginere)
    # 2. Schlüssel hier einfügen
    key = "YES"

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
    plt.style.use('ggplot')

    fig, ax = draw_friedmann(n, fc, turtle=False)
    #define y-unit to x-unit ratio
    ratio = 0.3
    
    #get x and y limits
    x_left, x_right = ax.get_xlim()
    y_low, y_high = ax.get_ylim()
    
    #set aspect ratio
    ax.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio)

    fig.savefig ("friedmann2.pdf",bbox_inches='tight')

    display_text_in_groups(text_viginere_enc, 33, 1)
    
    display_text_in_groups(text_viginere_enc, 3, 11)
    
    #fig.show()
    
    letters_most_common, shifts = findkey(text_viginere_enc, len(key))
    print(letters_most_common, shifts)
    
    
        

if __name__ == '__main__':
    main()
