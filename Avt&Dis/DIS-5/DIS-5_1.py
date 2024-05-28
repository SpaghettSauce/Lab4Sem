import sys
import numpy as np
import itertools
from tabulate import tabulate

np.set_printoptions(threshold=sys.maxsize)

def hammingDist(str1, str2, fillchar='-'):
    return sum([ch1 != ch2 for (ch1, ch2) in itertools.zip_longest(str1, str2, fillvalue=fillchar)])

g = [int(i) for i in "10100110111"] # порождающий многочлен
n = 31 # общее число элементов
m = 11 # число информационных элементов
length = len(g)

for i in range(n - length):
    g.append(0)

G0 = [] # временная матрица
for i in range(m):
    G0.append(np.roll(g, i))
G = np.array(G0) # порождающая матрица

codewords_table_headers = ["Информационное слово", "Кодовое слово"]
codewords_table = []
length = pow(2, m)

for i in range(0, length):
    d = np.array([int(i) for i in np.binary_repr(i, m)])
    codewords_table.append([''.join(map(str, d.tolist())), ''.join(map(str, np.mod(d.dot(G), 2)))])

with open('output1.txt', 'w') as file:
    file.write("Разрешённые кодовые комбинации: ")
    file.write("\n")
    file.write(tabulate(codewords_table, codewords_table_headers, tablefmt="grid", numalign='center'))
    file.close()

codewords_table = np.array("00000000000")
length = pow(2, m)

for i in range(1, length):
    d = np.array([int(i) for i in np.binary_repr(i, m)])
    codewords_table = np.append(codewords_table, ''.join(map(str, np.mod(d.dot(G), 2))))

length = len(codewords_table)
hamming_distances_table = np.zeros((length, length), dtype=int)

with open('output2.txt', 'w') as file:
    file.write("Таблица кодовых расстояний:\n")
    file.write("\n")

    for i in range(0, length):
        for j in range(i + 1, length):
            hamming_distances_table[i][j] = hammingDist(codewords_table[i], codewords_table[j])
            hamming_distances_table[j][i] = hamming_distances_table[i][j]
        file.write(str(hamming_distances_table[i]))
        file.write("\n")

    file.write("\n")
    file.write("Минимальное кодовое расстояние:\n")
    file.write(str(np.amin(np.where(hamming_distances_table == 0, 100, hamming_distances_table))))
    file.close()