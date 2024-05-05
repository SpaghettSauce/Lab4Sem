import nltk
grammar = nltk.CFG.fromstring("""
S -> A C1 | C4 A
A -> C5 C1 | C8 C1 | C9 C10
C1 -> C2 C3
C2 -> "+"
C3 -> "b"
C4 -> C3 C2
C5 -> "a"
C7 -> C5 C2
C8 -> C7 A
C9 -> C4 A
C10 -> C2 C5 
""") #Форма Хомского
sent = list("b+a+b")
string = ''
rd_parser = nltk.RecursiveDescentParser(grammar)
for p in rd_parser.parse(sent):
    print(p)
    string = string.join(p.leaves())
    print(string)
if string != '':
    print("Строка принята!))")
else:
    print("Строка не принята!((")
