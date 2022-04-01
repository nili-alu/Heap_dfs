# import of all libralies we want to use
import sys
from heapq import heapify, heappush, heappop


def question3a(diagram, source, destination):
    # initialising maximum value as infinity
    INF = sys.maxsize
    node_data = {"A": {"DIST": INF, "Pth": []},
                 "B": {"DIST": INF, "Pth": []},
                 "C": {"DIST": INF, "Pth": []},
                 "D": {"DIST": INF, "Pth": []},
                 "E": {"DIST": INF, "Pth": []},
                 "F": {"DIST": INF, "Pth": []}
                 }

    node_data[source]["DIST"] = 0
    visited = []
    temp = source

    for i in range(5):
        if temp is not visited:
            visited.append(temp)
            MinHeap = []
            for j in diagram[temp]:
                if j is not visited:
                    DIST = node_data[temp]["DIST"] + diagram[temp][j]
                    if DIST < node_data[j]["DIST"]:
                        node_data[j]["DIST"] = DIST
                        node_data[j]["Pth"] = node_data[temp]["Pth"] + list(temp)
                    heappush(MinHeap, (node_data[j]["DIST"], j))
        heapify(MinHeap)
        temp = MinHeap[0][1]
    print("shortest path: " + str(node_data[destination]["Pth"] + list(destination)))
    print("shortest distance of the above path is " + str(node_data[destination]["DIST"]))


if __name__ == "__main__":
    diagram = {
        "A": {"B": 13, "D": 10},
        "B": {"A": 13, "D": 17, "C": 5, "E": 20, "F": 18},
        "C": {"B": 5, "E": 22, "F": 30},
        "D": {"B": 17, "A": 10},
        "E": {"C": 22, "B": 20},
        "F": {"C": 30, "B": 18}
    }
    source = "C"

    for vertix in diagram.keys():
        destination = ""
        question3a(diagram, source, vertix)


