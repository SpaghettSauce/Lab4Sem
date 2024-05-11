from random import randint
def get_distance(N):
    Start = 0
    Graf = [[0 for i in range(N)] for i in range(N)]
    for i in range(N):
        Graf[i][i]=0
        for j in range(i + 1, N): 
            Graf[i][j] = randint(0, 100)
            Graf[j][i] = Graf[i][j]
    
    x = 0
    Dist = [10000 for i in range(N)]
    Used = [False for i in range(N)]
    minindex = 0
    min_value = 0
    
    Dist[Start] = 0
    while minindex < 10000:
        minindex = 10000
        min_value = 10000
        for i in range(N):
            if not Used[i] and Dist[i] < min_value:
                min_value = Dist[i]
                minindex = i
        if minindex != 10000:
            for i in range(N):
                if Graf[minindex][i] > 0:
                    x = min_value + Graf[minindex][i]
                    if x < Dist[i]:
                        Dist[i] = x
            Used[minindex] = True
            
    for endI in range(N):
        if Start == endI:
            print(str(Start + 1) + " - " + str(endI + 1) + " = " + str(Dist[endI]))
        else:
            end = endI
            Ver = [end + 1]
            weight = Dist[end]
            while end != Start:
                for i in range(N):
                    if Graf[end][i] != 0:
                        temp = weight - Graf[end][i]
                        if temp == Dist[i]:  
                            weight = temp 
                            end = i
                            Ver.append( i + 1)
                    
            print(str(Start + 1) + " - " + str(endI + 1) + " = " + str(Dist[endI]) + ":")
            for i in reversed(Ver):
                print(i, end = ' ')
            print()

get_distance(500)