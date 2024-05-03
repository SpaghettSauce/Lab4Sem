

def build_automaton(pattern):
    
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
    # построим конечный автомат по строке-образцу
    automaton = build_automaton(pattern)
    state = 0  # начинаем обработку из начального состояния автомата
    for i, ch in enumerate(text):  # обрабатываем каждый символ из строки-текста
        # проверяем, есть ли переход из текущего состояния по текущему символу
        if ch in automaton[state]:
            # переходим по автомату в следующее состояние
            state = automaton[state][ch]
        else:  # если перехода нет, возвращаемся на начальное состояние и продолжаем обработку с нового символа
            state = 0
        # если достигнуто терминальное состояние автомата, значит строка-образец найдена
        if state == len(pattern):
            # возвращаем индекс первого символа найденного образца в строке-тексте
            return i - len(pattern) + 1
    return -1  # если образец не найден, возвращаем -1


# считываем строку из файла
input_file = 'input.txt'
with open(input_file) as f:
    text = f.readline().strip()
print(f'\nИсходная строка: {text}')

# ищем образец в строке
pattern = input('\nВведите строку-образец: ')
index = find_pattern(text, pattern)

if index != -1:
    print(f'\nОбразец "{pattern}" найден в позиции {index} в строке-тексте: "{text}"\n')
else:
    print(f'\nОбразец "{pattern}" не найден в строке-тексте: "{text}"\n')