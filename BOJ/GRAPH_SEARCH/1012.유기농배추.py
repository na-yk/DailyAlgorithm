"""
BOJ#1012 유기농 배추
그래프 탐색
"""

import sys
from collections import deque

def bfs(graph, sx, sy, visited):
    if graph[sy][sx] == 0 or visited[sy][sx] == True:
        return False

    queue = deque()
    queue.append((sx,sy))
    visited[sy][sx] = True

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    while(queue):
        vx, vy = map(int, queue.popleft())
        for i in range(4):
            ax = vx + dx[i]
            ay = vy + dy[i]
            if graph[ay][ax] == 1 and visited[ay][ax] == False:
                queue.append((ax, ay))
                visited[ay][ax] = True

    return True


t = int(sys.stdin.readline())

for i in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0 for _ in range(m+2)] for _ in range(n+2)]
    visited = [[0 for _ in range(m+2)] for _ in range(n+2)]

    result = 0

    for j in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[y+1][x+1] = 1

    for y in range(1, n+1):
        for x in range(1, m+1):
            cabbage = bfs(graph, x, y, visited)
            if cabbage:
                result += 1

    print(result, end=' ')

