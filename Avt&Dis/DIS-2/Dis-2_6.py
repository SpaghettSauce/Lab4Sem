def count_paths(rows, cols):
    paths = [[0] * (cols + 1) for _ in range(rows + 1)]
    paths[0][0] = 1

    for i in range(rows + 1):
        for j in range(cols + 1):
            # Если мы не в начале
            if i != 0 or j != 0:
                # если мы слева сверху, то путь 1
                if i == 0 and j == 0:
                    paths[i][j] = 1
                else:
                    # проверяем если предыдущий ход был вертикальным 
                    if j >= 2:
                        paths[i][j] += paths[i][j - 2]
                    # проверяем если предыдущий ход был вертикальным
                    if i >= 1:
                        paths[i][j] += paths[i - 1][j]

    return paths[rows][cols]

rectangle_rows = 15
rectangle_cols = 14
print("Кол-во разных путе:", count_paths(rectangle_rows, rectangle_cols))

def count_paths(rows, cols):
    paths = [[0] * (cols + 1) for _ in range(rows + 1)]
    paths[0][0] = 1

    for i in range(rows + 1):
        for j in range(cols + 1):
            if i != 0 or j != 0:
                # Summing paths from top and left cells
                paths[i][j] = 0
                if j >= 2:
                    paths[i][j] += paths[i][j - 2]
                paths[i][j] += paths[i - 1][j]

    return paths[rows][cols]

rectangle_rows = 15
rectangle_cols = 14
print("Number of different paths:", count_paths(rectangle_rows, rectangle_cols))