#!/usr/bin/env python3

from encryption.viginere import *
from encryption.friedmann import *
from encryption.findkey import *


def main():
    # 1. Text hier einfügen
    text_viginere = open('./encryption/text.txt', ).read()
    # 2. Schlüssel hier einfügen
    key = "IMLEE"

    # folgender code VERschlüsselt den Text
    text_viginere_enc = viginere(text_viginere, key)
    print("Verschlüsselt (Geheimtext): %s" % text_viginere_enc)

    # folgender code ENTschlüsselt den Text
    text_viginere_dec = viginere(text_viginere_enc, key, encrypt=False)
    print("Entschlüsselt (Klartext):   %s" % text_viginere_dec)

    n = range(1, 10)
    fc = []
    for i in n:
        fc.append(friedmann_slice(text_viginere_enc, i))
    plt.style.use('ggplot')

    fig, ax = draw_friedmann(n, fc, turtle=False)
    #define y-unit to x-unit ratio
    ratio = 0.3

    #get x and y limits
    x_left, x_right = ax.get_xlim()
    y_low, y_high = ax.get_ylim()

    #set aspect ratio
    ax.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio)

    fig.savefig("friedmann2.pdf", bbox_inches='tight')

    letters_most_common, shifts = findkey(text_viginere_enc, len(key))
    print(letters_most_common, shifts)

    # the function below shows the crypto text in blocks
    display_text_in_groups(text_viginere_enc, len(key), 11)

    # the function below shows the cleartext, key and cryptotext in a readable format
    display_viginere_all(text_viginere_dec, text_viginere_enc,
                         key, n_chars=30, with_delim=True)


if __name__ == '__main__':
    main()
