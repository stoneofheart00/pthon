I=9999999
vertices=5
graph=[[0,9,75,0,0],
[9,0,95,19,42],
[75,95,0,51,66],
[0,19,51,0,31],
[0,42,66,31,0]]
selected=[0,0,0,0,0]
no_edge=0
selected[0]=True
print("Edge : weight \n")
while(no_edge < vertices-1):
    minimum=I
    x=0
    y=0
    for i in range(vertices):
        if selected[i]:
            for j in range(vertices):
                if((not selected[j]) and graph[i][j]):
                    if minimum > graph[i][j]:
                        minimum = graph[i][j]
                        x=i 
                        y=j 
    print(str(x) + "-" +str(y)+":"+str(graph[x][y]))
    selected[y]=True
    no_edge+=1