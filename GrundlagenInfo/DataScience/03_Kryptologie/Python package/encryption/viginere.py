def viginere(text, key, encrypt=True):
    text=text.upper()
    chars_replace=[" ", ".", ","]
    for c in chars_replace:
        text=text.replace(c, "")
    text_encrypted = []
    for i in range(len(text)):
        if text[i]!=" ":
            k=key[i%len(key)]
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
