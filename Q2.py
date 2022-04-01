# Floyd Warshall Algorithm
# Author: Lievin
import sys

# The number of nodes/vertices of graph
Nbr_node = 6

INF = sys.maxsize

# Algorithm implementation
def shortest_Path(Diagram):
    length_btn_Nodes = list(map(lambda i: list(map(lambda j: j, i)), Diagram))

    # Adding nodes(vertices) using matrix
    for k in range(Nbr_node):
        for i in range(Nbr_node):
            for j in range(Nbr_node):
                length_btn_Nodes[i][j] = min(length_btn_Nodes[i][j], length_btn_Nodes[i][k] + length_btn_Nodes[k][j])
    print_solution(length_btn_Nodes)


# Printing the solution
print("the shortest path from each vertix : ")
def print_solution(length_btn_Nodes):
    for i in range(Nbr_node):
        for j in range(Nbr_node):
            if(length_btn_Nodes[i][j] == INF):
                print("INF", end=" ")

            else:
                print(length_btn_Nodes[i][j], end="  ")
        print(" ")


Diagram = [[0, 2, 5, 1, INF, INF],
           [2, 0, 3, 2, INF, INF],
           [5, 3, 0, 3, 1, 5],
           [1, 2, 3, 0, 1, INF],
           [INF, INF, 1, 1, 0, 1],
           [INF, INF, 5, INF, 1, 0]
          ]
shortest_Path(Diagram)