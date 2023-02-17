"""
BOJ#1260 DFS와 BFS
그래프 탐색
"""

import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for adj in graph[v]:
        if not visited[adj]:
            dfs(graph, adj, visited)

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while(queue):
        n = queue.popleft()
        print(n, end=' ')
        for adj in graph[n]:
            if not visited[adj]:
                queue.append(adj)
                visited[adj] = True


n, m, v = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for vertex in graph:
    vertex.sort()

dfs(graph, v, visited)
print("")
visited = [False] * (n+1)
bfs(graph, v, visited)