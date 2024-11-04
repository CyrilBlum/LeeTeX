from vigenere import *

def caesar_buchstabe(buchstabe, verschiebung):
    return chr((ord(buchstabe) - ord("A") + verschiebung) % 26 + ord("A"))


def caesar(text, verschiebung):
    text_verschoben = ""

    for buchstabe in text:
        text_verschoben += caesar_buchstabe(buchstabe, verschiebung)

    return text_verschoben

# langer Text einlesen aus .txt-Datei
text_lang = open("text.txt").readlines()[0]
text_lang_c = caesar(text_lang, 3)
fig, ax = show_letter_freq(text_lang_c)
