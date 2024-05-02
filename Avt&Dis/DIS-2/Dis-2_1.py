word = "Комбинатoрuкa"
endW = set()

for i in range(len(word)):
    for j in range(len(word)):
        for q in range(len(word)):
            for c in range(len(word)):
                four = word[i] + word[j] + word[q] + word[c]
                
