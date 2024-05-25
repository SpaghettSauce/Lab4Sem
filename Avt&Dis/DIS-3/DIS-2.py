from tabulate import tabulate

m = [" ", 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л']
n = ['00000000', '00000111', '00011001', '11000001', '01010101', '10110010', '10100100', '11111111']

table = [m]


for i in range(len(n)):
    line = [m[i + 1]]
    for l in range(i):
        line.append(" ")
    line.append(0)
    for j in range(i + 1, len(n)):
        num = sum(1 for k in range(len(n[i])) if n[i][k] != n[j][k])
        line.append(num)
    table.append(line)

for i in range(1, len(n) + 1):
    for j in range(i):
        table[i][j + 1] = table[j + 1][i]

print(tabulate(table, tablefmt="grid", numalign='center'))
