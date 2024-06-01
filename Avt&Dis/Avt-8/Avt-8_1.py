class LL1Parser:
    def __init__(self):
        self.grammar_rules = {
            1: ('S', ['a', 'A', 'b', 'B']),
            2: ('A', ['0', 'A', '1']),
            3: ('A', ['0', '1']),
            4: ('B', ['0', 'B', '1', '1']),
            5: ('B', ['0', '1', '1'])
        }
        self.parse_table = {
            'S': {'a': 1},
            'A': {'0': 2},
            'B': {'0': 4}
        }
        self.non_terminals = set(['S', 'A', 'B'])
    
    def parse(self, input_string):
        input_string += '$'
        stack = ['$', 'S']
        index = 0
        output = []

        while len(stack) > 0:
            top = stack.pop()
            current_input = input_string[index]

            if top in self.non_terminals:
                if current_input in self.parse_table[top]:
                    rule_number = self.parse_table[top][current_input]
                    lhs, rhs = self.grammar_rules[rule_number]
                    output.append(rule_number)
                    stack.extend(reversed(rhs))
                else:
                    raise SyntaxError(f"Не тот символ: {current_input} в позиции {index}")
            elif top == current_input:
                index += 1
            else:
                raise SyntaxError(f"Не тот символ: {current_input} в позиции {index}")

        if index == len(input_string) - 1:
            return output
        else:
            raise SyntaxError("Упси")

# Example usage
parser = LL1Parser()
input_string = "a0b011"
try:
    result = parser.parse(input_string)
  
    print( result)
except SyntaxError as e:
    print(e)
