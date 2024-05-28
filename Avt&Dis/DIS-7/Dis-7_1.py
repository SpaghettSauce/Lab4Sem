import random
import sys

def shortest_dist(count_of_nodes, dist, shortest_way):
    min_dist = sys.maxsize
    min_index = 0
    for i in range(count_of_nodes):
        if not shortest_way[i] and dist[i] <= min_dist:
            min_dist = dist[i]
            min_index = i
    return min_index

def print_way(parent, v):
    if parent[v] == -1:
        return
    print_way(parent, parent[v])
    print(v, end=" ")

def print_res(current_node, distance, count_of_nodes, parent):
    print("Node\tDistance\tWay")
    for i in range(count_of_nodes):
        if i != current_node:
            print(f"{current_node} -> {i}\t\t{distance[i]}\t\t", end="")
            print_way(parent, i)
            print()

def dijkstra_algorithm(count_nodes, matrix, this_node):
    dist = [sys.maxsize] * count_nodes
    shortest_way = [False] * count_nodes
    parent = [-1] * count_nodes

    dist[this_node] = 0

    for _ in range(count_nodes):
        a = shortest_dist(count_nodes, dist, shortest_way)
        shortest_way[a] = True

        for j in range(count_nodes):
            if not shortest_way[j] and matrix[a][j] and dist[a] + matrix[a][j] < dist[j]:
                parent[j] = a
                dist[j] = dist[a] + matrix[a][j]

    print_res(this_node, dist, count_nodes, parent)

def input_matrix(count_nodes):
    mat = []
    for i in range(count_nodes):
        row = []
        for j in range(count_nodes):
            data = random.randint(1, 9)
            row.append(data)
            print(data, end=" ")
        mat.append(row)
        print()
    return mat

def main():
    random.seed()
    count_nodes = int(input("Enter count of nodes: "))
    
    print("Matrix: ")
    mat = input_matrix(count_nodes)

    this_node = int(input("Enter node: "))
    print()

    print(f"Shortest way from {this_node}")
    dijkstra_algorithm(count_nodes, mat, this_node)

if __name__ == "__main__":
    main()
