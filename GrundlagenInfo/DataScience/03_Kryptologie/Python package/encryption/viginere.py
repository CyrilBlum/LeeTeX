import numpy as np

def viginere(text, key, encrypt=True):
    text = text.upper()
    chars_replace = [" ", ".", ","]
    for c in chars_replace:
        text = text.replace(c, "")
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


def display_viginere_all(vigi_dec, vigi_enc, vigi_key, n_chars=10, with_delim=False):
    p_vigi_key = vigi_key*int(np.ceil(n_chars/len(vigi_key)))
    p_vigi_key = p_vigi_key[:n_chars]
    p_vigi_dec = vigi_dec[:n_chars]
    p_vigi_enc = vigi_enc[:n_chars]
    
    if with_delim:
        def insert_dash(string, index, symbol="|"):
            return string[:index] + symbol + string[index:]

        inserted=0
        for i in range(len(vigi_key), n_chars, len(vigi_key)):
            p_vigi_key=insert_dash(p_vigi_key, i+inserted)
            p_vigi_dec=insert_dash(p_vigi_dec, i+inserted)
            p_vigi_enc=insert_dash(p_vigi_enc, i+inserted)
            inserted+=1
        
        p_vigi_key = p_vigi_key[:n_chars]
        p_vigi_dec = p_vigi_dec[:n_chars]
        p_vigi_enc = p_vigi_enc[:n_chars]
    
    for name, value in zip(["Klartext", "Schlüssel", "Geheimtext"], [p_vigi_dec, p_vigi_key, p_vigi_enc]):
        print(f'{name:>10}: {value}...')
