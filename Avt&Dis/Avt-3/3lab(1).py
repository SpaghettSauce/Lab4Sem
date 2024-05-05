import nltk
grammar = nltk.CFG.fromstring("""
S -> A "+" "b" | "b" "+" A 
A -> "a" "+" "b" | "a" "+" A "+" "b" | "b" "+" A "+" "a"
""") #Обычная форма грамматики
try:
    string = ''
    sent = list("a+b") #Cтрока
    rd_parser = nltk.RecursiveDescentParser(grammar) #Определяем метод рекурсивного спуска для данной грамматики
    for p in rd_parser.parse(sent): #Строим дерево и сразу по этому дереву собираем нашу строку заново
        print(p)
        string = string.join(p.leaves())
        print(string)
    if string != '':
        print("Строка принята!))")
    else:
        print("Строка не принята!((")
except:
    print("Строка не принята!((")