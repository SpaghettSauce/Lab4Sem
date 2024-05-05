import nltk
grammar = nltk.CFG.fromstring("""
S -> "a" Z1 Z1 | "a" Z0 A Z1 Z1| "b" Z0 A 
A -> "a" Z1 | "a" Z0 A Z1 | "b" Z0 A Z3 
Z0 -> "+" 
Z1 -> "+" Z2
Z2 -> "b"
Z3 -> "+" Z4
Z4 -> "a"
""") #Форма Грейбах
sent = list("a+a+b+b")
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