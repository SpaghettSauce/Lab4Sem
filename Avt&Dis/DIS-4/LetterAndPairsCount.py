from collections import Counter
import re

def count_letters(text):
    clean_text = re.sub(r'[^a-zA-Z]', '', text.lower())
    letter_counts = Counter(clean_text)
    total_letters = sum(letter_counts.values())
    letter_freq = {letter: count / total_letters for letter, count in letter_counts.items()}
    return letter_freq

def count_letter_pairs(text):
    clean_text = re.sub(r'[^a-zA-Z]', '', text.lower())
    letter_pairs = [clean_text[i:i+2] for i in range(len(clean_text) - 1)]
    pair_counts = Counter(letter_pairs)
    total_pairs = sum(pair_counts.values())
    pair_freq = {pair: count / total_pairs for pair, count in pair_counts.items()}
    return pair_freq

def analyze_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    letter_freq = count_letters(text)
    pair_freq = count_letter_pairs(text)
    return letter_freq, pair_freq


file_path = 'input.txt'  
letter_freq, pair_freq = analyze_file(file_path)
print("Letter frequencies:")
print(letter_freq)
print("\nLetter pair frequencies:")
print(pair_freq)