# defining the graph
graph = {
    "C":["B", "E", "F"],
    "B":["A", "D", "E", "F"],
    "A":["D","B"],
    "D":["A", "B"],
    "E":["B","C"],
    "F":["C","B"] }
vertices_visited =set()

print("order of visiting vertices using depth-first traversal is:")

# define a function with three methods such as vertices, graph and source
def dfs(v, g, src):

    # if source not visited return it then add source into visited list
    if src not in v:
        print(src)
        v.add(src)

        for x in g[src]:
            dfs(v, g, x)

#function calling
dfs(vertices_visited, graph, "C")



