def recursdfs(graph,s,path=[]):
    if s not in path:
        path.append(s)
        if s not in graph:
            return path
        for neighbour in graph[s]:
            path = recursdfs(graph,neighbour,path)
            return path

graph = {"A":["B","C","D"],
           "B":["E"],
           "C":["G","F"],
           "D":["H"],
           "E":["I"],
           "F":["J"],
           "G":["K"]}

dfs=recursdfs(graph,"A")
print("Depth Frist searck Traversal")
print("_____________________________")
print(dfs)
