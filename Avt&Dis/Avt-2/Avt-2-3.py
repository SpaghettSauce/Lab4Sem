class Automaton:
    def __init__(self):
        self.states = set()
        self.start_state = None
        self.accept_states = set()
        self.transitions = {}

    def add_state(self, state, is_start=False, is_accept=False):
        self.states.add(state)
        if is_start:
            self.start_state = state
        if is_accept:
            self.accept_states.add(state)

    def add_transition(self, from_state, symbol, to_state):
        if from_state not in self.transitions:
            self.transitions[from_state] = {}
        if symbol not in self.transitions[from_state]:
            self.transitions[from_state][symbol] = set()
        self.transitions[from_state][symbol].add(to_state)

    def is_accepted(self, string):
        current_states = {self.start_state}
        for symbol in string:
            next_states = set()
            for state in current_states:
                if state in self.transitions and symbol in self.transitions[state]:
                    next_states |= self.transitions[state][symbol]
            current_states = next_states
        return any(state in self.accept_states for state in current_states)


automaton = Automaton()


automaton.add_state('q0', is_start=True)
automaton.add_state('q1')
automaton.add_state('q2')
automaton.add_state('q3', is_accept=True)
automaton.add_state('q4')
automaton.add_state('q5')
automaton.add_state('q6')

automaton.add_transition('q0', 'a', 'q1')
automaton.add_transition('q1', 'b', 'q4')
automaton.add_transition('q4', 'c', 'q3')
automaton.add_transition('q1', 'c', 'q2')
automaton.add_transition('q2', 'a', 'q5')
automaton.add_transition('q5', 'b', 'q6')
automaton.add_transition('q6', 'a', 'q5')

# Test the automaton with some strings
strings_to_test = ["abbc", "abababbc", "ba", "ab", "abcc","abb", ]

for string in strings_to_test:
    if automaton.is_accepted(string):
        print(f"'{string}' is accepted")
    else:
        print(f"'{string}' is not accepted")