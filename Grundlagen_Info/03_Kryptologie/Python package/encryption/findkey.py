from collections import Counter    


def findkey(text_enc, keylength):
    letters_most_common = []
    shifts=[]
    for i in range(keylength):
        txt_sub = text_enc[i::keylength]
        c = Counter(txt_sub)
        letter_most_common = c.most_common()[0][0]
        shift = (26+ord(letter_most_common)-ord("E"))%26
        letters_most_common.append(letter_most_common)
        shifts.append(shift)
        print(chr(65+shift))
    return(letters_most_common, shifts)