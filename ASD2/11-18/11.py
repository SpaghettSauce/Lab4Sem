
def automat(pattern):
    alphabet = set(pattern)
    automaton = [{ch: 0 for ch in alphabet} for _ in range(len(pattern) + 1)]
    for state in range(len(pattern) + 1):  
        for ch in alphabet:
            next_state = min(len(pattern), state + 1)
            while next_state > 0 and pattern[:next_state] != pattern[state-next_state+1:state+1]:
                next_state -= 1
            automaton[state][ch] = next_state
    return automaton


def find_pattern(text, pattern):
    automaton = automat(pattern)
    state = 0  
    for i, ch in enumerate(text):  
        if ch in automaton[state]:
            state = automaton[state][ch]
        else:  
            state = 0
        if state == len(pattern):
            return i - len(pattern) + 1
    return -1 


input_file = 'input.txt'
with open(input_file) as f:
    text = f.readline().strip()
print(f' {text}')

pattern = input()
index = find_pattern(text, pattern)

if index != -1:
    print(f'\nОбразец "{pattern}" найден в {index} \n')
else:
    print(f'\nОбразец "{pattern}" не найден \n')