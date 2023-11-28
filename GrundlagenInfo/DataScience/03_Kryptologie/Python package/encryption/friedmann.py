from collections import Counter    
#from gturtle import *
#makeTurtle()
#hideTurtle()
import matplotlib.pyplot as plt
import numpy as np

def friedman(text):
    freq = countocc(text.lower())
    summe = 0
    for letter_freq in freq:
        summe += (letter_freq - (1/26))**2
    return summe
      
def countocc(eingabe):
    length = len(eingabe)
    counter = Counter(eingabe)
    alphabet = []
    for i in range(26):
        letter = chr(97+i)
        occ = counter[letter]
        alphabet.append(occ/length)
    return alphabet

def friedmann_slice(text, keylength):
    i=0
    fc_avg=0
    for i in range(keylength):
        text_slice=text[i::keylength]
        fc = friedman(text_slice)
        fc_avg += fc
        i+=1
    
    fc_avg/=keylength
    
    return fc_avg
    
def draw_friedmann(i, fc, turtle=False):
    if turtle:
        xshift=150
        setPos(-xshift+50, 150)
        label("Friedmann'sche Charakteristik:")
        setPos(-xshift,0)
        pd()
        fd(200)
        bk(200)
        rt(90)
        fd(400)
        bk(400)
        
        for  i in n:
            setPos(i*40-xshift, fc[i-1]*1000)
            dot(10)
            setPos(i*40-xshift, fc[i-1]*1000+40)
            label(i)
    else:
        fig, ax = plt.subplots()
        ax.plot(i, fc, 'o')
        return fig, ax
