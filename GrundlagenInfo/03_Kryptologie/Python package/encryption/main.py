from vigenere import *
from caesar import *
from friedmann import *
from friedmann_aux import *
from monoalphabetic import *
plt.style.use('ggplot')

def caesar_main():
    # kurzer Text (Skript Aufgabe)
    text_kurz = "SIEHABENESGESCHAFFTDIESENTEXTZUKNACKEN"
    text_kurz_c = caesar(text_kurz, 4)
    print(text_kurz_c)
    fig, ax = show_letter_freq(text_kurz_c)
#    plt.show()
    plt.savefig("../../Figures/caesar-freq-exercise.pdf", format="pdf", bbox_inches="tight")

def vigenere_main():
    # langer Text, mit Caesar und Vigenère
    # langer Text einlesen aus .txt-Datei
    text_kurz = "BRAVOGUTGEMACHT"
    text_kurz_v = vigenere(text_kurz, "ABC")
    print("V",text_kurz_v)

    text_lang = open("Texts/Kafka.txt").readlines()[0]
    text_lang = preprocess_text(text_lang)
    text_lang_c = caesar(text_lang, 2)
    fig, ax = show_letter_freq(text_lang_c)
    #plt.show()
    plt.savefig("../../Figures/caesar-freq.pdf", format="pdf", bbox_inches="tight")

    text_lang_v = vigenere(text_lang, "KSLEE")
    print("LANGER TEXT", text_lang_v[:400])
    fig, ax = show_letter_freq(text_lang_v)
    #plt.show()
    plt.savefig("../../Figures/vigenere-freq.pdf", format="pdf", bbox_inches="tight")

    # vigenere frequencies by group

    text_lang_v = vigenere(text_lang, "ICH")
    #fig, ax = show_letter_freq(text_lang_v)
    #plt.show()
    print(text_lang[:20])
    print(text_lang_v[:20])

    print(vigenere("MUZKJLQPAWJUMHYIILLCZAUPMRLZHLSVCMTZBCULGUPCIMPDQGTIPCQILVGYMGUBUJPNBMUZMNAPGYHNPKJLOTHBWSIVPWPKIHB", "ICH", False))

# generate friedman figures
def friedman_main():
    text = "MUZ KJL QPA WJU MHY IIL LCZ AUP MRL ZHL SVC 		MTZ BCU LGU PCI MPD QGT IPC QIL VGY MGU BUJ 		PNB MUZ MNA PGY HNP KJL OTH BWS IVP WPK IHB"
    key = "ICH"
    text = preprocess_text(text)

    # plot letter frequencies for each subgroup (can only be done correctly if true keylength is known)
    keylength=len(key)
    for i in range(keylength):
        text_slice=text[i::keylength]
        # plot letter frequences
        fig, ax = show_letter_freq(text_slice)
        plt.savefig("../../Figures/vigenere-"+str(i+1)+".pdf", format="pdf", bbox_inches="tight")
        plt.close()

    text_lang = open("Texts/Werther.txt").readlines()[0]
    text_lang = preprocess_text(text_lang)
    key = "YEAH"
    text = vigenere(text_lang, key)

    fc = get_friedman_vals(text, 15)
    fig, ax=draw_friedmann(15, fc)
    # plt.show()
    plt.savefig("../../Figures/friedman.pdf", format="pdf", bbox_inches="tight")
        

def monoalphabetic_main():
    cleartext="NENNE DREI ANTIKEN GEHEIMSCHRIFTEN DIE IHNEN GEFALLEN"
    ciphertext="MUMMU XJUQ YMHQOUM SUTUQNGWTJQVHUM XQU QTMUM SUVYPPUM"
    shifts = get_shifts(cleartext,ciphertext)
    cleartext_new="NENNE DREI ANTIKE GEHEIMSCHRIFTEN DIE DIR GEFALLEN"
    ciphertext_new = predict_text(cleartext_new, shifts)
    print(ciphertext_new)
    print(shifts)

caesar_main()