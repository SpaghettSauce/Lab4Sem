from collections import defaultdict
from math import ceil, log2


class Node:
    def __init__(self, label, weight=0):
        self.label = label
        self.weight = weight
        self.left = None
        self.right = None
        self.code = ""

    def __repr__(self):
        return f"{self.label}: {self.weight}"


def codewords_making(node, code=""):
    if node.left is not None:
        node.left.code = code + "0"
        codewords_making(node.left, code + "0")
    if node.right is not None:
        node.right.code = code + "1"
        codewords_making(node.right, code + "1")


def encoding(text, codes):
    encoded_text = ""
    for ch in text:
        encoded_text += codes[ch]
    return encoded_text


def Shannon_formula(frequencies, text_length):
    shannon = 0
    for char, prob in frequencies.items():
        shannon += (prob / text_length) * log2(prob / text_length)
    return round(-1 * shannon, 6)


# алгоритм Хаффмана
freqs1 = defaultdict(int)
freqs2 = defaultdict(int)
text = ""
with open("input.txt", "r") as file:
    text = file.read()
for ch in text:
    freqs1[ch] += 1
for i in range(0, len(text) - 1):
    freqs2[text[i] + text[i + 1]] += 1
# построение кодов Хаффмана
nodes = []
for k, v in freqs1.items():
    nodes.append(Node(k, v))
nodes.sort(key=lambda x: x.weight)
end_nodes = nodes.copy()
while len(nodes) != 1:
    left = nodes.pop(0)
    right = nodes.pop(0)
    node = Node(left.label + right.label, left.weight + right.weight)
    node.left = left
    node.right = right
    nodes.insert(0, node)
    nodes.sort(key=lambda x: x.weight)
codewords_making(nodes[0])
codes = dict()
for node in end_nodes:
    codes[node.label] = node.code
encoded = encoding(text, codes)
freqs1_list = []
freqs2_list = []
for i in freqs1.keys():
    freqs1_list.append([i, freqs1[i]])
for i in freqs2.keys():
    freqs2_list.append([i, freqs2[i]])
print("Количество символов в исходном тексте: ", len(text))
print("Количество уникальных символов: ", len(freqs1_list))
with open('output1.txt', 'w') as file:
    file.write("Символы и их частоты: " + str(sorted(freqs1_list, key=lambda frequency: frequency[1])))
    file.write("\n\n")
    file.write("Пары символов и их частоты: " + str(sorted(freqs2_list, key=lambda frequency: frequency[1])))
    file.close()
with open('output2.txt', 'w') as file:
    file.write("Символы и их коды Хаффмана: " + str(codes))
    file.write("\n\n")
    file.write("Закодированная строка: " + encoded)
    file.close()
print("Длина закодированного текста (метод Хаффмана):", len(encoded))
print("Длина при равномерном (шестибитовом) кодировании:", 6 * len(text))
print("Степень сжатия по сравнению с равномерным (шестибитовым) кодированием:",
      round(100 - (len(encoded) / (6 * len(text))) * 100, 6), "%")
print("Формула Шеннона (метод Хаффмана):", Shannon_formula(freqs1, len(text)), "бит")

# алгоритм LZW
LZW_dict = dict()
i = 0
for char in codes:
    LZW_dict[char] = i
    i += 1
dictionary_size = len(LZW_dict)
init_bits = ceil(log2(dictionary_size))
string = ""
LZW_encoded = []
for char in text:
    new_string = string + char
    if new_string in LZW_dict:
        string = new_string
    else:
        LZW_encoded.append(LZW_dict[string])
        LZW_dict[new_string] = dictionary_size
        dictionary_size += 1
        string = char
if string in LZW_dict:
    LZW_encoded.append(LZW_dict[string])
LZW_encoded_res = ""
for seq in LZW_encoded:
    bits = 0
    if seq == 0:
        bits = init_bits
    elif ceil(log2(seq)) < init_bits:
        bits = init_bits
    else:
        bits = ceil(log2(seq))
    LZW_encoded_res += format(seq, f'0{bits}b')
with open('output3.txt', 'w') as file:
    file.write("Словарь: " + str(LZW_dict))
    file.write("\n\n")
    file.write("Закодированная строка (битовая): " + LZW_encoded_res)
    file.write("\n\n")
    file.write("Закодированная строка (кодовая): " + str(LZW_encoded))
    file.close()
print()
print("Длина закодированного текста (метод LZW): ", len(LZW_encoded_res))
print("Степень сжатия по сравнению с равномерным (шестибитовым) кодированием:",
      round(100 - (len(LZW_encoded_res) / (6 * len(text))) * 100, 6), "%")
print("Степень сжатия по сравнению с кодами Хаффмана:",
      round(100 - (len(LZW_encoded_res) / len(encoded)) * 100, 6), "%")
