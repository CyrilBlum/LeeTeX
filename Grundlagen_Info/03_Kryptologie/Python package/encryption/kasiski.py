import re
from collections import Counter
import math
from itertools import combinations
from functools import reduce
from vigenere import *
from helpers import *


def count_ngrams(text, n, top_k):
    ngrams = [text[i : i + n] for i in range(len(text) - n + 1)]
    counter = Counter(ngrams)
    return counter.most_common(top_k)


def find_positions(ngrams, text):
    positions = {}
    for ng in ngrams:
        pos_list = [
            i + 1 for i in range(len(text) - len(ng) + 1) if text[i : i + len(ng)] == ng
        ]
        positions[ng] = pos_list
    return positions


def prime_factors(n):
    factors = []
    # handle 2 separately to allow incrementing by 2 later
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # check odd numbers from 3 onwards
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors


def gcd_of_differences_with_primes(position_dict):
    result = {}
    for ngram, positions in position_dict.items():
        if len(positions) < 2:
            result[ngram] = {"gcd": None, "differences": []}
            continue

        differences_info = []
        differences = []

        for a, b in combinations(positions, 2):
            diff = abs(a - b)
            differences.append(diff)
            differences_info.append(
                {
                    "start": a,
                    "end": b,
                    "difference": diff,
                    "prime_factors": prime_factors(diff),
                }
            )

        gcd_value = reduce(math.gcd, differences)
        result[ngram] = {"gcd": gcd_value, "differences": differences_info}

    return result


def test_slides():
    # produces the numbers shown in the Kasiski slides
    text_klar = "MEINKLEINERREIMSCHEINTKEINERZUSEIN"
    schluessel = "CODE"
    text = vigenere(text_klar, schluessel)

    ngrams = ["HMP", "IKB"]
    result_pos = find_positions(ngrams, text)
    print(result_pos)

    result = gcd_of_differences(result_pos)
    print(result)


def test_arbeitsblatt():
    # code for Kasiski Arbeitsblatt
    text = "UEUIOOCEUDIWIOOWRRCLWVUQURRCLWVNDTHXETHERRCFKRTWVSFYOQRNJJTGRSVUAVIOOCEQEIHRUIYOHITQLNJZNJVSEVRJRUILNGUEUIOOCEUDIWIOOWHRVRWVAXWZXIOOCEQIOOWAWDEWVAXWUQUWRCLWVDLVNDVCKJTHETDXEYFMUFLOVRQZCKKSPVHUYOHIEQ"

    # get 5 most common 3-grams
    result = count_ngrams(text, 3, 5)
    print(result)

    # chose top two 3-grams
    ngrams = ["IOO", "OCE"]

    # find positions of 3-grams in text
    result_pos = find_positions(ngrams, text)
    print(result_pos)

    # get GCD of all pairwise differences
    result = gcd_of_differences_with_primes(result_pos)
    for key, val in result.items():
        print("{}:".format(key))
        for subkey, subval in val.items():
            print("{}:{}".format(subkey, subval))


def insert_subscripts_latex_wrapped(
    text: str, n: int, line_length: int = 80, highlight_ngrams=None
) -> str:
    if highlight_ngrams is None:
        highlight_ngrams = []

    # Step 1: Erzeuge "sichtbare" Tokens mit Formatierung
    tokens = []
    for i, char in enumerate(text, start=1):
        if i % n == 0:
            formatted = rf"\(\underset{{\makebox[\widthof{{\texttt{{X}}}}][c]{{\footnotesize\texttt{{\red{{{i}}}}}}}}}{{\texttt{{\red{{{char}}}}}}}\)"
        else:
            formatted = rf"{char}"
        tokens.append((char, formatted))  # tuple: (plain, latex)

    # Step 2: Markiere n-Gramme (im originalen Zeichenstrom)
    if highlight_ngrams:
        i = 0
        while i < len(tokens):
            matched = False
            for ngram in highlight_ngrams:
                length = len(ngram)
                segment = "".join(
                    tokens[j][0] for j in range(i, min(i + length, len(tokens)))
                )
                if segment == ngram:
                    # Markiere alle betroffenen Tokens
                    for j in range(length):
                        char, latex = tokens[i + j]
                        tokens[i + j] = (char, rf"\underline{{{latex}}}")
                    matched = True
                    break
            i += length if matched else 1

    # Step 3: Baue Zeilen mit jeweils genau line_length sichtbaren Zeichen
    lines = []
    for i in range(0, len(tokens), line_length):
        line = "".join(latex for _, latex in tokens[i : i + line_length])
        lines.append(line)

    # Step 4: Zusammensetzen mit Zeilenabstand
    latex_body = "\\\\[1cm]\\rule{\\linewidth}{1pt}\n".join(lines)

    return r"\begin{alltt}" + "\n" + latex_body + "\n" + r"\end{alltt}"


# long_text="UEUIOOCEUDIWIOOWRRCLWVUQURRCLWVNDTHXETHERRCFKRTWVSFYOQRNJJTGRSVUAVIOOCEQEIHRUIYOHITQLNJZNJVSEVRJRUILNGUEUIOOCEUDIWIOOWHRVRWVAXWZXIOOCEQIOOWAWDEWVAXWUQUWRCLWVDLVNDVCKJTHETDXEYFMUFLOVRQZCKKSPVHUYOHIEQ"
# print(insert_subscripts_latex_wrapped(long_text,10,60, ["IOO", "OCE"]))
# #test_arbeitsblatt()


if __name__ == "__main__":
    # exercise 1
    long_text = "UEUIOOCEUDIWIOOWRRCLWVUQURRCLWVNDTHXETHERRCFKRTWVSFYOQRNJJTGRSVUAVIOOCEQEIHRUIYOHITQLNJZNJVSEVRJRUILNGUEUIOOCEUDIWIOOWHRVRWVAXWZXIOOCEQIOOWAWDEWVAXWUQUWRCLWVDLVNDVCKJTHETDXEYFMUFLOVRQZCKKSPVHUYOHIEQ"
    print(insert_subscripts_latex_wrapped(long_text, 10, 60, ["IOO"]))

    # exercise 2
    long_text = "UEUIOOCEUDIWIOOWRRCLWVUQURRCLWVNDTHXETHERRCFKRTWVSFYOQRNJJTGRSVUAVIOOCEQEIHRUIYOHITQLNJZNJVSEVRJRUILNGUEUIOOCEUDIWIOOWHRVRWVAXWZXIOOCEQIOOWAWDEWVAXWUQUWRCLWVDLVNDVCKJTHETDXEYFMUFLOVRQZCKKSPVHUYOHIEQ"
    print(insert_subscripts_latex_wrapped(long_text, 10, 60, ["IOO"]))
    # test_arbeitsblatt()
