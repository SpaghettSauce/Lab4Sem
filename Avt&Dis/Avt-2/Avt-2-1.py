class DFA:
    def __init__(self):
        self.states = {'S', 'A', 'B', 'C'}
        self.alphabet = {'a', 'b', 'c'}
        self.transitions = {
            'S': {'a': 'A', 'b': 'S'},
            'A': {'a': 'B', 'b': 'C'},
            'B': {'b': 'B', 'c': 'A'},
            'C': {'b': 'A', 'a': 'C'}
        }
        self.start_state = 'S'
        self.final_states = {'S', 'C'}

    def is_valid_input(self, input_str):
        return all(char in self.alphabet for char in input_str)

    def run(self, input_str):
        if not self.is_valid_input(input_str):
            return False
        current_state = self.start_state
        for char in input_str:
            current_state = self.transitions[current_state].get(char)
            if current_state is None:
                return False
        return current_state in self.final_states


dfa = DFA()
test_strings = ["ab", "bbca", "bca", "bac", "bcb", "abbbc"]
for test_string in test_strings:
    if dfa.run(test_string):
        print(f"'{test_string}' is accepted")
    else:
        print(f"'{test_string}' is rejected")

