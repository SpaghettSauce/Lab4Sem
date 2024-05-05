def bad_character_table(pattern):
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table

def good_suffix_table(pattern):
    table = [0] * (len(pattern) + 1)
    i = len(pattern)
    j = len(pattern) + 1
    table[i] = j
    while i > 0:
        while j <= len(pattern) and pattern[i-1] != pattern[j-1]:
            if table[j] == 0:
                table[j] = j - i
            j = table[j]
        i -= 1
        j -= 1
        table[i] = j
    return table

def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    bad_char = bad_character_table(pattern)
    good_suffix = good_suffix_table(pattern)
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            return i
        else:
            bad_char_shift = j - bad_char.get(text[i + j], -1)
            good_suffix_shift = good_suffix[j + 1]
            i += max(bad_char_shift, good_suffix_shift)
    return -1

input_file = 'input.txt'
with open(input_file) as f:
    text = f.readline().strip()
print(f' {text}')
pattern = input()

index = boyer_moore(text, pattern)
if index != -1:
    print(f"Нашел в {index}")
else:
    print("Не нашел")