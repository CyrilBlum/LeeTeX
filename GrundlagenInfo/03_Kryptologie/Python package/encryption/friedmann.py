from collections import Counter    

def friedman(text):
    # Determine the Friedman Characteristic for a given text
    summe = 0
    for letter_freq in freq:
        summe += (letter_freq - (1/26))**2
    return summe
      
def countocc(eingabe):
    # Helper function, used for calculating the Friedman Characteristic
    length = len(eingabe)
    counter = Counter(eingabe)
    alphabet = []
    for i in range(26):
        letter = chr(97+i)
        occ = counter[letter]
        alphabet.append(occ/length)
    return alphabet

def friedmann_slice(text, keylength):
    # Based on a text encrypted with Friedman and a given keylength, determine the average Friedman characteristic for all subgroups of the text.
    i=0
    fc_avg=0
    for i in range(keylength):
        text_slice=text[i::keylength]
        fc = friedman(text_slice)
        fc_avg += fc
        i+=1
    
    fc_avg/=keylength
    
    return fc_avg