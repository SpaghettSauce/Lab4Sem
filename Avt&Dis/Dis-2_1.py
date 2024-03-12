from itertools import permutations

'''1'''
word = "комбинаторика"
letters = list(word)
unique_letters = set(letters)
permutations = permutations(unique_letters, 4)
unique_words = set([''.join(p) for p in permutations])

print("Number of different 5-letter words:", len(unique_words))

