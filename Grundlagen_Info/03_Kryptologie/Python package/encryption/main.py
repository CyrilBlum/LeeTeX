from pathlib import Path
from vigenere import *
from caesar import *
from friedman import *
from monoalphabetic import *

plt.style.use("ggplot")

# Setup paths relative to this script
BASE_DIR = Path(__file__).resolve().parent
FIGURES_DIR = (BASE_DIR / "../../Figures").resolve()
TEXTS_DIR = BASE_DIR / "Texts"


def caesar_main():
    # kurzer Text (Skript Aufgabe)
    text_kurz = "SIEHABENESGESCHAFFTDIESENTEXTZUKNACKEN"
    text_kurz_c = caesar(text_kurz, 4)
    print(text_kurz_c)
    fig, ax = show_letter_freq(text_kurz_c)

    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    plt.savefig(FIGURES_DIR / "caesar-freq-exercise.pdf", format="pdf", bbox_inches="tight")

    text_lang = open(TEXTS_DIR / "Kafka.txt").readlines()[0]
    text_lang = preprocess_text(text_lang)
    text_lang_c = caesar(text_lang, 2)
    fig, ax = show_letter_freq(text_lang_c, ylim=(0, 20))
    # plt.show()
    plt.savefig(FIGURES_DIR / "caesar-freq.pdf", format="pdf", bbox_inches="tight")


def vigenere_main():
    # langer Text, mit Caesar und Vigenère
    # langer Text einlesen aus .txt-Datei
    text_kurz = "SIEVERSTEHENOTP"
    text_kurz_v = vigenere(text_kurz, "SIEHABENESGESCH")
    print("V", text_kurz_v)

    text_lang = open(TEXTS_DIR / "Kafka.txt").readlines()[0]
    text_lang_v = vigenere(text_lang, "ABCDEFG")
    print("LANGER TEXT", text_lang_v[:400])
    fig, ax = show_letter_freq(text_lang_v, ylim=(0, 20))
    # plt.show()
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    plt.savefig(FIGURES_DIR / "vigenere-freq.pdf", format="pdf", bbox_inches="tight")

    # vigenere frequencies by group

    text_lang_v = vigenere(text_lang, "ICH")
    # fig, ax = show_letter_freq(text_lang_v)
    # plt.show()
    print(text_lang[:20])
    print(text_lang_v[:20])

    print(
        vigenere(
            "MUZKJLQPAWJUMHYIILLCZAUPMRLZHLSVCMTZBCULGUPCIMPDQGTIPCQILVGYMGUBUJPNBMUZMNAPGYHNPKJLOTHBWSIVPWPKIHB",
            "ICH",
            False,
        )
    )


# generate friedman figures
def friedman_main(savefig=True):
    text_lang = open(TEXTS_DIR / "Werther.txt").readlines()[0]
    text_lang = preprocess_text(text_lang)
    key = "ICH"
    text = vigenere(text_lang, key)

    print(text)

    # plot letter frequencies for each subgroup (can only be done correctly if true keylength is known)
    keylength = len(key)
    max_keylength = keylength + 2
    for keylen_test in range(max_keylength + 1):
        for i in range(keylen_test):
            text_slice = text[i::keylen_test]
            # calculate friedman'sche Charakteristik
            fc = calculate_fc(text_slice)
            print(
                "Keylength: %2d, Group: %2d, FC_T:%.2f%%" % (keylen_test, i, fc * 100)
            )

            # plot letter frequences
            if i == 0 and keylen_test == keylength:
                fig, ax = show_letter_freq(text_slice, show_diff_to_avg=True)
                ax.set_aspect(0.5)
                if savefig:
                    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
                    filename = f"vigenere-len{keylen_test}-group{i+1}-avg.pdf"
                    plt.savefig(FIGURES_DIR / filename, format="pdf", bbox_inches="tight")
                    plt.close()
                else:
                    plt.show()

            fig, ax = show_letter_freq(text_slice, show_diff_to_avg=False)
            ax.set_title(f"$FC_T: {fc:.2%}%$%")
            if savefig:
                FIGURES_DIR.mkdir(parents=True, exist_ok=True)
                filename = f"vigenere-len{keylen_test}-group{i+1}.pdf"
                plt.savefig(FIGURES_DIR / filename, format="pdf", bbox_inches="tight")
                plt.close()
            else:
                plt.show()

    fc = get_friedman_vals(text, 15)
    fig, ax = draw_friedman(15, fc)
    if savefig:
        FIGURES_DIR.mkdir(parents=True, exist_ok=True)
        plt.savefig(FIGURES_DIR / "friedman.pdf", format="pdf", bbox_inches="tight")
        plt.close()
    else:
        plt.show()


def monoalphabetic_main():
    cleartext = "NENNE DREI ANTIKEN GEHEIMSCHRIFTEN DIE IHNEN GEFALLEN"
    ciphertext = "MUMMU XJUQ YMHQOUM SUTUQNGWTJQVHUM XQU QTMUM SUVYPPUM"
    shifts = get_shifts(cleartext, ciphertext)
    cleartext_new = "NENNE DREI ANTIKE GEHEIMSCHRIFTEN DIE DIR GEFALLEN"
    ciphertext_new = predict_text(cleartext_new, shifts)
    print(ciphertext_new)
    print(shifts)


if __name__ == "__main__":
    caesar_main()
    # friedman_main()
    # monoalphabetic_main()
    vigenere_main()
