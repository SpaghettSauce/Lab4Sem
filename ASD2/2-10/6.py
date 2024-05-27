'''
Шаги в алгоритме Крускала:
1. Создаем список, состоящий из всех ребер, сортированный по возрастанию их веса.
2. Создаем пустое дерево и множество, содержащее все вершины графа.
3. Берем ребро из отсортированного списка ребер с наименьшим весом и проверяем, не создает ли оно цикл в дереве.
Если ребро не создает цикла, добавляем его в дерево, а вершины, соединяемые этим ребром, объединяем в одно множество.
4. Повторяем шаг 3 для каждого ребра в отсортированном списке до тех пор, пока не будут рассмотрены все ребра или пока 
дерево не станет остовным.
Грубо говоря мы строим новое дерево, в котором нету циклов
'''

def read_matrix(file_path): #считываем матрицу 
    with open(file_path, 'r') as file:
        lines = file.readlines() #считываем каждую строку из файла
        matrix = [[int(val) for val in line.split()] for line in lines] #преобразуем каждую строку в int, заполняем ими вложенный список, наш граф
    return matrix

def write_results(mst, output_file):
    with open(output_file, 'w') as file:
        file.write("Путь \tВес\n")
        for u, v, weight in mst:
            file.write(f"{u+1} - {v+1}\t{weight}\n")

def find(parent, i): #находим корень сета в котором есть элемент i
    if parent[i] == i: #если нашли корень
        return i #верни его
    return find(parent, parent[i]) #в ином случае рекурсивно далее ищем

def union(parent, rank, x, y): #фунция соединяет два поддерева в одном из которых x в другом y
    xroot = find(parent, x)#находим их корни (чтобы их соединить)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]: #все эти ифы нужны чтобы поддерево с меньшим ранком соединить под большим 
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot #если они одиннаковы то выбираем какой сами хотим
        rank[xroot] += 1

def kruskal(adjacency_matrix):
    num_vertices = len(adjacency_matrix) #здесь будем хранить кол-во вершин в графе
    result = []
    i = 0
    e = 0

    edges = [] #а здесь сами вершины 
    for u in range(num_vertices): #проходимся по всем вершинам
        for v in range(u + 1, num_vertices):
            if adjacency_matrix[u][v] != 0: #еслм между вершинами есть путь
                edges.append([u, v, adjacency_matrix[u][v]]) #добавим в массив
    edges.sort(key=lambda x: x[2]) #отсортируем

    parent = [i for i in range(num_vertices)]
    rank = [0] * num_vertices

    while e < num_vertices - 1: #рассмотрим все вершины
        u, v, weight = edges[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y: #берем ребро из отсортированного списка ребер с наименьшим весом и проверяем, не создает ли оно цикл в дереве
            e += 1
            result.append([u, v, weight])
            union(parent, rank, x, y)

    return result



input_file_path = "input.txt"  
output_file_path = "output_6.txt"

adjacency_matrix = read_matrix(input_file_path)
mst = kruskal(adjacency_matrix)
write_results(mst, output_file_path)