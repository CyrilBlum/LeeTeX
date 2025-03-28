import numpy as np
import string
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from collections import Counter
from helpers import *
import re


def vigenere(text, key, encrypt=True):
    text = preprocess_text(text)
    text_encrypted = []
    for i in range(len(text)):
        if text[i] != " ":
            k = key[i % len(key)]
            shift = ord(k)-65
            if encrypt:
                new_letter = chr(((shift+ord(text[i])-65) % 26)+65)
            else:
                new_letter = chr(((ord(text[i])-65-shift) % 26)+65)
            text_encrypted.append(new_letter)
        else:
            text_encrypted.append(" ")

    text_encrypted = "".join(text_encrypted)
    return text_encrypted


def display_text_in_groups(text, keylength=3, n_groups=11):
    text_out = ""
    for i in range(len(text)):
        text_out += text[i]
        if (i-keylength+1) % keylength == 0:
            text_out += " "
        if (i-keylength*n_groups+1) % (keylength*n_groups) == 0:
            text_out += "\n"

    print(text_out)


def display_vigenere_all(vige_dec, vige_enc, vige_key, n_chars=10, with_delim=False):
    p_vige_key = vige_key*int(np.ceil(n_chars/len(vige_key)))
    p_vige_key = p_vige_key[:n_chars]
    p_vige_dec = vige_dec[:n_chars]
    p_vige_enc = vige_enc[:n_chars]
    
    if with_delim:
        def insert_dash(string, index, symbol="|"):
            return string[:index] + symbol + string[index:]

        inserted=0
        for i in range(len(vige_key), n_chars, len(vige_key)):
            p_vige_key=insert_dash(p_vige_key, i+inserted)
            p_vige_dec=insert_dash(p_vige_dec, i+inserted)
            p_vige_enc=insert_dash(p_vige_enc, i+inserted)
            inserted+=1
        
        p_vige_key = p_vige_key[:n_chars]
        p_vige_dec = p_vige_dec[:n_chars]
        p_vige_enc = p_vige_enc[:n_chars]
    
    for name, value in zip(["Klartext", "Schlüssel", "Geheimtext"], [p_vige_dec, p_vige_key, p_vige_enc]):
        print(f'{name:>10}: {value}...')

def show_letter_freq(text, show_diff_to_avg=False):
    # @argument show_diff_to_avg: also show difference to expected average of 1/26
    fig, ax = plt.subplots()
    
    # Initialize the dictionary for all letters from A to Z with a count of 0
    c = Counter({letter: 0 for letter in string.ascii_uppercase})
    
    # Count the actual frequencies in the text
    c.update(text)
    freq_perc = [(i, c[i] / len(text)) for i in c]
    freq_perc = np.array(freq_perc)[np.argsort([i[0] for i in freq_perc])]

    ax.bar(freq_perc[:,0], freq_perc[:,1].astype(float)*100, width=.5, color='g')
    if show_diff_to_avg:
        # Expected average frequency (1/26)
        avg_freq = 1 / 26 * 100  # in percentage
        
        # Plot horizontal line at average frequency
        ax.axhline(y=avg_freq, color='r', linestyle='--', label=f'1/26 (≈ {avg_freq:.2f}%)')
        
        # Add double arrows for the difference
        for i, freq in enumerate(freq_perc[:,1].astype(float) * 100):
            letter = freq_perc[i, 0]
            diff = freq - avg_freq
            # Position the arrow slightly above the bar
            y_pos = max(freq, avg_freq) + 0.5
            # Draw double arrow
            ax.annotate(
                '', 
                xy=(letter, freq), 
                xytext=(letter, avg_freq), 
                arrowprops=dict(arrowstyle='-', color='blue', lw=1.2)
            )
            # Annotate difference value
            ax.text(letter, y_pos, f'{diff:+.1f}%', ha='center', va='bottom', fontsize=8, color='blue',rotation=90)
        
        ax.legend() 

    ax.yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))
    return fig, ax

def show_letter_freq_multiple(text_enc, text_dec, add_hline=True):
    fig, ax = plt.subplots()
    c_enc= Counter(text_enc)
    c_enc = {k: c_enc.get(k, 0)/len(text_enc)*100 for k in string.ascii_uppercase}
    
    c_dec= Counter(text_dec)
    c_dec = {k: c_dec.get(k, 0)/len(text_dec)*100 for k in string.ascii_uppercase}

    print(c_dec)
    

    x_axis = np.arange(len(c_dec.keys())) 
                        
    ax.bar(x_axis-.2, c_dec.values(), width=.5, color='cornflowerblue', label='Klartext')
    ax.bar(x_axis+.2, c_enc.values(), width=.5, color='coral', label='Geheimtext')
    ax.set_xticks(x_axis, c_enc.keys()) 
    
    if add_hline:
        plt.axhline(y=1/26*100, color='r', linestyle='-', label=r'$\frac{1}{26}$', linewidth=.75)
    
    ax.legend()
    ax.set_ylim(0,25)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    return fig, ax