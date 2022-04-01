# import of all libralies we want to use
import sys
from heapq import heapify,heappush,heappop


def dijkstra(diagram,source,destination):
    # initialising maximum value as infinity
    INF = sys.maxsize
    node_data={"A": {"cost": INF,"pred":[]},
               "B": {"cost": INF, "pred": []},
               "C": {"cost": INF, "pred": []},
               "D": {"cost": INF, "pred": []},
               "E": {"cost": INF, "pred": []},
               "F": {"cost": INF, "pred": []}
               }

    node_data[source]["cost"] = 0
    visited = []
    temp = source

    for  i in range(5):
        if temp is not visited:
            visited.append(temp)
            MinHeap=[]
            for j in diagram[temp]:
                if j is not visited:
                    cost=node_data[temp]["cost"] +diagram[temp][j]
                    if cost<node_data[j]["cost"]:
                        node_data[j]["cost"]=cost
                        node_data[j]["pred"]=node_data[temp]["pred"]+list(temp)
                    heappush(MinHeap,(node_data[j]["cost"],j))
        heapify(MinHeap)
        temp=MinHeap[0][1]
    print("shortest path: " + str(node_data[destination]["pred"] + list(destination)))
    print("shortest distance of the above path is " + str(node_data[destination]["cost"]))



if __name__=="__main__":
    diagram={
        "A": {"B":13,"D":10},
        "B": {"A":13,"D":17,"C":5,"E":20,"F":18},
        "C": {"B":5,"E":22,"F":30},
        "D": {"B":17,"A":10},
        "E": {"C":22,"B":20},
        "F": {"C":30,"B":18}
    }
    source = "C"

    for vertix in diagram.keys():
        destination = ""
        dijkstra(diagram, source, vertix)
