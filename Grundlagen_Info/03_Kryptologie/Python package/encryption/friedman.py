import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
from helpers import count_letters

def calculate_fc(text):
    # Determine the Friedman Characteristic for a given text
    summe = 0
    freq = count_letters(text)
    for letter_freq in freq:
        summe += (letter_freq - (1/26))**2
    return summe

def friedman_slice(text, keylength):
    # Based on a text encrypted with Friedman and a given keylength, determine the average Friedman characteristic for all subgroups of the text.
    i=0
    fc_avg=0
    for i in range(keylength):
        text_slice=text[i::keylength]
        fc = calculate_fc(text_slice)
        fc_avg += fc
        i+=1
    
    fc_avg/=keylength
    
    return fc_avg

def get_friedman_vals(text, maxkeylen):
    """
    For a Text text, get the average Friedman Characteristics for key lengths up to maxkeylen
    """
    n=range(1, maxkeylen)
    fc=[]
    for i in n:
        fc.append(friedman_slice(text,i))
    return fc

def draw_friedman(i, fc, turtle=False):
    """
    Draw the friedman Characteristics for various possible key lengths
    """
    if turtle:
        xshift=150
        setPos(-xshift+50, 150)
        label("friedman'sche Charakteristik:")
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
        ax.plot(range(1,i), fc, 'o')
        plt.xticks(np.arange(1, i, 1.0))
        ax.yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0,xmax=1))
        return fig, ax
    
if __name__ == "__main__":
    print(calculate_fc("PAPPERLAPAPP"))
    print(calculate_fc("BACKSTEIN"))