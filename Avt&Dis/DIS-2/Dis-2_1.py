word =['к','о','м','б','и','н','а','т','о','р','и','к','а',]
endW = set()

for i in range(len(word)):
    for j in range(len(word)):
        for q in range(len(word)):
            for c in range(len(word)):
                endW.add( word[i] + word[j] + word[q] + word[c])
                
print (len(endW))