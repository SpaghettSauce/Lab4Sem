"""На вход подаётся математическое выражение.
    Элементы - числа. Операции - "+ - * /". Также есть скобочки.
    Окончанием выражения служит "=".Программа должна вывести результат выражения"""


OPERATORS = {'+': (1, lambda x, y: x + y),
             '-': (2, lambda x, y: x - y),
             '/': (3, lambda x, y: x / y),
             '*': (4, lambda x, y: x * y)}


def eval_(formula):
    def parse(formula_string):
        number = ''
        for s in formula_string:
            if s in '1234567890.':
                number += s
            elif number:
                yield float(number)
                number = ''
            if s in OPERATORS or s in "()":
                yield s
        if number:
            yield float(number)

    def shunting_yard(parsed_formula):
        stack = []
        for token in parsed_formula:
            if token in OPERATORS:
                while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                stack.append(token)
            else:
                yield token
        while stack:
            yield stack.pop()

    def calc(polish):
        stack = []
        for token in polish:
            if token in OPERATORS:
                y, x = stack.pop(), stack.pop()
                stack.append(OPERATORS[token][1](x, y))
            else:
                stack.append(token)
        return stack[0]

    r = list(shunting_yard(parse(formula)))
    print("Арифметическое выражение в обратной польской записи: ")
    print(' '.join(map(str, r)))
    print()
    print("Результат вычисления: ")
    return calc(shunting_yard(parse(formula)))


print("Введите арифметическое выражение: ")
arithmetic_expression = input()
print("Арифметическое выражение: " + str(arithmetic_expression))
try:
    eval(arithmetic_expression)
    print(eval_(arithmetic_expression))
except SyntaxError:
    print("Ошибка! Обнаружена синтаксическая ошибка")
except ZeroDivisionError:
    print("Ошибка! Деление на ноль")
