"""
BOJ#1707 이분 그래프
그래프와 순회
"""

import sys

sys.setrecursionlimit(100000) # Recursion Error 방지

# DFS 함수
def dfs(graph, v, visited):
    global result

    for a in graph[v]:
        if colors[a] == 0:
            if colors[v] == 1:
                colors[a] = -1
            elif colors[v] == -1:
                colors[a] = 1
            dfs(graph, a, visited)
        elif colors[v] == colors[a]:
            result = False
            return



k = int(sys.stdin.readline())

results = []
for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(v+1)]
    colors = [0 for _ in range(v+1)]
    edges = []
    result = True
    for j in range(e):
        a, b = map(int, sys.stdin.readline().split())
        edges.append((a,b))
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v+1):
        if colors[i] == 0:
            colors[i] = 1
            dfs(graph, i, colors)

            if not result:
                results.append("NO")
                break

    if result:
        results.append("YES")


for answer in results:
    print(answer)