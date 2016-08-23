def minimum_distance_vertex_pair(graph):
    n = len(graph)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[j][k] > graph[j][i]+graph[i][k]:
                    graph[j][k] = graph[j][i]+graph[i][k]

    return graph

n, m = map(int, raw_input().split(" "))
INF = float('Inf')
graph = []
for i in range(n):
    graph.append([])
    for j in range(n):
        if i == j:
            graph[i].append(0)
        else:
            graph[i].append(INF)
for i in range(m):
    a, b, c = map(int, raw_input().split(" "))
    graph[a - 1][b - 1] = c
graph = minimum_distance_vertex_pair(graph)
q = int(raw_input())
while q:
    q -= 1
    a, b = map(int, raw_input().split(" "))
    print graph[a-1][b-1] if graph[a-1][b-1] != INF else -1

