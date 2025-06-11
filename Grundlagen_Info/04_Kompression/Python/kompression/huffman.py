from fractions import Fraction

# Huffman Coding in python

# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


def calculate_huffman_codes(frequencies):
    # Sort frequencies
    freq = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    nodes = freq

    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))

        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    huffmanCode = huffman_code_tree(nodes[0][0])

    print(' Char | Frequency       | Huffman code ')
    print('---------------------------------------')
    len_chars = 0
    len_text = 100
    total_frequency = sum(frequencies.values())
    sorted_huffman = sorted(huffmanCode.items())  # Sort by letter (alphabetic)
    for char, code in sorted_huffman:
        frequency = frequencies[char]
        frequency_fraction = Fraction(frequency, total_frequency)
        len_chars += frequency / total_frequency * len_text * len(code)
        print(' %-4r | %15s | %12s' % (char, frequency_fraction, code))

    print('---------------------------------------')
    print('Total encoded length: %.2f' % len_chars)
    return huffmanCode


# Example usage with a string
string = 'AAAABBBBBCCCDDDE'
def calculate_frequencies(input_string):
    frequencies = {}
    for c in input_string:
        if c in frequencies:
            frequencies[c] += 1
        else:
            frequencies[c] = 1
    return frequencies

frequencies = calculate_frequencies(string)

print("Using string:")
calculate_huffman_codes(frequencies)

# Example usage with predefined frequencies
predefined_frequencies = {'A': 3, 'B': 15, 'C': 59, 'D': 10, 'E': 4, 'F': 9}
print("\nUsing predefined frequencies:")
calculate_huffman_codes(predefined_frequencies)