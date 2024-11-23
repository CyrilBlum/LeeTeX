from vigenere import *
from caesar import *
plt.style.use('ggplot')

# kurzer Text (Skript Aufgabe)
text_kurz = "SIEHABENESGESCHAFFTDIESENTEXTZUKNACKEN"
text_kurz_c = caesar(text_kurz, 2)
fig, ax = show_letter_freq(text_kurz_c)
#plt.show()
plt.savefig("../../Figures/caesar-freq-exercise.pdf", format="pdf", bbox_inches="tight")

# langer Text, mit Caesar und Vigenère
# langer Text einlesen aus .txt-Datei
text_lang = open("text.txt").readlines()[0]
text_lang = preprocess_text(text_lang)
text_lang_c = caesar(text_lang, 2)
fig, ax = show_letter_freq(text_lang_c)
#plt.show()
plt.savefig("../../Figures/caesar-freq.pdf", format="pdf", bbox_inches="tight")

text_lang_v = vigenere(text_lang, "KEY")
fig, ax = show_letter_freq(text_lang_v)
#plt.show()
plt.savefig("../../Figures/vigenere-freq.pdf", format="pdf", bbox_inches="tight")
