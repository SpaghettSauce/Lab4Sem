class CYK:
    def __init__(self, N=140):
        self.N = N
        self.M = [[set() for _ in range(N)] for _ in range(N)]
        self.l = 0

    def __str__(self, S):
        return ''.join(S)

    def cyk(self, s):
        for i in range(self.N):
            for j in range(self.N):
                self.M[i][j] = set()

        self.l = len(s)
        for i in range(self.l):
            if s[i] == '+':
                self.M[i][i].add('A')
            elif s[i] == '0':
                self.M[i][i].add('B')
            elif s[i] == '1':
                self.M[i][i].add('C')
            else:
                print("Unknown terminal symbol!")
                exit(1)

        for j in range(1, self.l):
            for i in range(self.l - j):
                for k in range(i, i + j):
                    if 'A' in self.M[i][k] and 'S' in self.M[k + 1][i + j]:
                        self.M[i][i + j].add('S')

                    if 'D' in self.M[i][k] and 'E' in self.M[k + 1][i + j]:
                        self.M[i][i + j].add('S')

                    if 'M' in self.M[i][k] and 'C' in self.M[k + 1][i + j]:
                        self.M[i][i + j].add('S')

                    if 'B' in self.M[i][k] and 'F' in self.M[k + 1][i + j]:
                        self.M[i][i + j].add('D')

                    if 'C' in self.M[i][k] and 'C' in self.M[k + 1][i + j]:
                        self.M[i][i + j].add('E')

                    if 'B' in self.M[i][k] and 'S' in self.M[k + 1][i + j]:
                        self.M[i][i + j].add('M')

                    if 'B' in self.M[i][k] and 'C' in self.M[k + 1][i + j]:
                        self.M[i][i + j].add('F')

        print(f"L={self.l}")
        S = self.l - 1

        for i in range(self.l):
            for j in range(S - i, self.l):
                print(self.__str__(self.M[j - (S - i)][j]), end='\t')
            print()

        return self.l == 0 or 'S' in self.M[0][self.l - 1]


cyk_parser = CYK()
s = input()
if cyk_parser.cyk(s):
    print("Is in grammar")
else:
    print("Isn't in grammar")

with open("Output.txt", "w") as file:
    file.write(f"input: {s}\noutput:\n")
    for i in range(cyk_parser.l + 1):
        for j in range(i):
            file.write(cyk_parser.__str__(cyk_parser.M[j][cyk_parser.l - i + j]) + '\t')
        file.write('\n')

'''
+000000000000000000000000000000000111111111111111111111111111111111111111111111111111111111111111111
'''
