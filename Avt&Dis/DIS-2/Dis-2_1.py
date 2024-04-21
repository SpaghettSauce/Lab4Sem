from itertools import permutations

word = "Комбинатoрuкa"
unique_letters = ''.join(set(word)) 
Wlist = permutations(unique_letters, 4) 
arr = []

for perm in Wlist: 
    arr.append(''.join(perm))

print("Total valid words:", len(arr))
print(arr)