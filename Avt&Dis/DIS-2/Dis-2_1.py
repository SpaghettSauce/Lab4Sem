from itertools import permutations

word = "комбинр"      
unique_letters = ''.join(set(word)) #делим слово на индивидуальные символы
Wlist = permutations(unique_letters, 4) #создаем через пермутацию лист со всеми возможными комбинациями
arr = [] #создаем пустой массив, куда запишем лист

for perm in Wlist: 
    arr.append(''.join(perm))

print("Клво слов:", len(arr))
print(arr)