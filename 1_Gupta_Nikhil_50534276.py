from collections import deque

def bfs(graph, startVertex):
    visited = set()
    queue = deque()
    queue.append(startVertex)
    visited.add(startVertex)
    d={}
    d[startVertex] = 0
    bfsOrder = []

    while queue:
        vertex = queue.popleft()
        bfsOrder.append(vertex)

        for vertexes in graph[vertex]:
            if vertexes not in visited:
                d[vertexes] = 1 if d[vertex]==0 else 0
                visited.add(vertexes)
                queue.append(vertexes)

    return bfsOrder, d

n,m = list(map(int, input().split()))
graph = {i+1: [] for i in range(n)}
while m!=0:
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)
    m-=1

def ifBipartite(bfsTraversal, dColor):
    for vertex in bfsTraversal:
        for vertexes in graph[vertex]:
            if dColor[vertex]==dColor[vertexes]:
                return "no"
    return "yes"

bfsTraversal , dColor = bfs(graph, 1)
print(ifBipartite(bfsTraversal, dColor))