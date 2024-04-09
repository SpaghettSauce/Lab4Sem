array = ['к','о','м','б','и','н','а','т','о','р','и','к','а']  
n = len(array)
words = set()

for i in range(0,n):
    for j in range(0,n):
        for q in range(0,n):
            for k in range(0,n):
                for o in range(0,n):
                    if (array[i] != array[i+1]):
                        words.add(array[i]+array[j]+array[q]+array[k])

print(len(words))