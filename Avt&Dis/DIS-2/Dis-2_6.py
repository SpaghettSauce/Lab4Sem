size_ver = 15
size_hor = 14
matrix = [[0 for x in range(size_hor)] for y in range(size_ver)]
matrix[0][0] = 1

for count in range(1, size_ver):
    i = count   
    j = 0
    while i >= 0 and j < size_hor:
        if i != 0:
            matrix[i][j] = matrix[i -1][j]        
        if j != 0:
            matrix[i][j] += matrix[i][j - 1]       
        i -= 1
        j += 1        
        if i== 0 and j == 1:
            matrix[i][j] = 1
for count in range(1, size_hor):
    i = size_ver - 1     
    j = count
    while j < size_hor and i >= 1:         
        if i != 0:
            matrix[i][j] = matrix[i - 1][j]         
        if j != 0:
            matrix[i][j] += matrix[i][j - 1]       
        i -= 1
        j += 1
#
for count in range(1, size_ver):
    i = count    
    j = 0
    while i >= 0 and j < size_hor:        
        if i != 0:
            matrix[i][j] = matrix[i -1][j]        
        if j != 0 and i != 0:
            matrix[i][j] += matrix[i - 1][j - 1]        
        i -= 1
        j += 1        
        if i== 0 and j == 1:
            matrix[i][j] = 1
for count in range(1, size_hor):    
    i = size_ver - 1
    j = count    
    while j < size_hor and i >= 1:
        if i != 0:            
            matrix[i][j] = matrix[i - 1][j]
        if j != 0 and i != 0:           
            matrix[i][j] += matrix[i - 1][j - 1]
        i -= 1        
        j += 1
print(str(matrix[size_ver - 1][size_hor - 1]))

'''
# Создание массива размером 16x16 и заполнение его нулями
grid = [[0 for _ in range(15)] for _ in range(15)]

grid[0][1] = 1
grid[1][0] = 1
# Заполнение первой строки и первого столбца значениями 1

# Вычисление количества путей для каждой ячейки массива
for i in range(1, 15):
    for j in range(1, 15):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

# Вывод количества путей из левого нижнего угла в правый верхний угол
print(grid[14][14])
'''
