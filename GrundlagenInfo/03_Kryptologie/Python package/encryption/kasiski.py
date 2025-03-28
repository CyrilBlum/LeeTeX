from collections import Counter
import math
from itertools import combinations
from functools import reduce
from vigenere import *
from helpers import *

def count_ngrams(text, n, top_k):
    ngrams = [text[i:i+n] for i in range(len(text)-n+1)]
    counter = Counter(ngrams)
    return counter.most_common(top_k)

def find_positions(ngrams, text):
    positions = {}
    for ng in ngrams:
        pos_list = [i+1 for i in range(len(text) - len(ng) + 1) if text[i:i+len(ng)] == ng]
        positions[ng] = pos_list
    return positions

def gcd_of_differences(position_dict):
    gcds = {}
    for ngram, positions in position_dict.items():
        if len(positions) < 2:
            gcds[ngram] = None  # not enough positions to calculate differences
            continue
        differences = [abs(a - b) for a, b in combinations(positions, 2)]
        gcds[ngram] = reduce(math.gcd, differences)
    return gcds




text_klar = "WEINSCHEINTMIRFEINZUSEIN"
schluessel = "CODE"
text = vigenere(text_klar, schluessel)
print(text)

#text= "UEUIOOCEUDIWIOOWRRCLWVUQURRCLWVNDTHXETHERRCFKRTWVSFYOQRNJJTGRSVUAVIOOCEQEIHRUIYOHITQLNJZNJVSEVRJRUILNGUEUIOOCEUDIWIOOWHRVRWVAXWZXIOOCEQIOOWAWDEWVAXWUQUWRCLWVDLVNDVCKJTHETDXEYFMUFLOVRQZCKKSPVHUYOHIEQ"
result = count_ngrams(text, 3, 5)
print(result)

ngrams = ["SLR", "IKB"]
result_pos = find_positions(ngrams, text)
print(result_pos)

#result = gcd_of_differences(result_pos)
#print(result)
# {'ABC': [0, 4, 8, 15], 'BCD': [1, 5, 9]}
