class FiniteAutomaton:
    def __init__(self):
        self.transitions = {
            (0, 'a'): None,
            (0, 'b'): 0,
            (1, 'a'): 1,
            (1, 'b'): None,
            (2, 'a'): 1,
            (2, 'b'): None,
            (3, 'a'): 3,
            (3, 'b'): 3
        }
        self.accepting_states = {1}

    def run(self, input_string):
        current_state = 0
        for symbol in input_string:
            if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)]
            else:
                return False
        return current_state in self.accepting_states



automaton = FiniteAutomaton()
input_string = input()
if automaton.run(input_string):
    print("Принята")
else:
    print("Не принята")