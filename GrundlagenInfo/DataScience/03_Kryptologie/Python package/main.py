#!/usr/bin/env python3

from encryption.viginere import *
from encryption.friedmann import *
from encryption.findkey import *


def set_aspect_ratio(ax, ratio=.3):
    #get x and y limits
    x_left, x_right = ax.get_xlim()
    y_low, y_high = ax.get_ylim()

    #set aspect ratio
    ax.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio)
    return(ax)

def main():
    # 1. Text hier einfügen
    text_viginere = open('./encryption/text.txt', ).read()
    # 2. Schlüssel hier einfügen
    key = "ICH"

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
    ax = set_aspect_ratio(ax)

    fig.savefig("friedmann.pdf", bbox_inches='tight')

    letters_most_common, shifts = findkey(text_viginere_enc, len(key))
    print(letters_most_common, shifts)

    # the function below shows the crypto text in blocks
    display_text_in_groups(text_viginere_enc, len(key), 11)

    # the function below shows the cleartext, key and cryptotext in a readable format
    display_viginere_all(text_viginere_dec, text_viginere_enc,
                         key, n_chars=30, with_delim=True)
    
    letters_most_common, shifts = findkey(text_viginere_enc[:30], len(key))
    print(letters_most_common, shifts)
    letters_most_common, shifts = findkey(text_viginere_dec[:30], len(key))
    print(letters_most_common, shifts)
    
    
    
    fig, ax=show_letter_freq(text_viginere_enc[1::len(key)])
    ax = set_aspect_ratio(ax)
    fig.savefig("letterfreq_enc.pdf", bbox_inches='tight')
    fig, ax=show_letter_freq(text_viginere_dec)
    ax = set_aspect_ratio(ax)
    fig.savefig("letterfreq_dec.pdf", bbox_inches='tight')
    
    for i in range(3):
        fig, ax=show_letter_freq_multiple(text_viginere_enc[i::len(key)], text_viginere_dec)
        ax = set_aspect_ratio(ax,ratio=.4)
        fig.savefig("letterfreq_end_dec"+str(i)+".pdf", bbox_inches='tight')
        
    fig, ax=show_letter_freq_multiple(text_viginere_enc, text_viginere_dec)
    ax = set_aspect_ratio(ax,ratio=.4)
    fig.savefig("letterfreq_end_dec_alletters.pdf", bbox_inches='tight')

if __name__ == '__main__':
    main()
