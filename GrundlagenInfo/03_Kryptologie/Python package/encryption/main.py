from vigenere import *
from caesar import *
# langer Text einlesen aus .txt-Datei
text_lang = open("text.txt").readlines()[0]
text_lang = preprocess_text(text_lang)
text_lang_c = caesar(text_lang, 2)
plt.style.use('ggplot')
fig, ax = show_letter_freq(text_lang_c)
#plt.show()
plt.savefig("../../Figures/caesar-freq.pdf", format="pdf", bbox_inches="tight")

