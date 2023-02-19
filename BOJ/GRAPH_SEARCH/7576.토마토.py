"""
BOJ#7576 토마토
그래프 탐색
"""

import sys
from collections import deque

def bfs(graph, starts, visited):
    queue = deque()
    # 시작점을 큐에 연속으로 넣어서
    for start in starts:
        queue.append(start)
        visited[start[1]][start[0]] = True

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # 각 시작점에서 번갈아가면서 bfs를 하도록 만듦
    while(queue):
        vx, vy = map(int, queue.popleft())
        if graph[vy][vx] >= 1:
            for i in range(4):
                ax = vx + dx[i]
                ay = vy + dy[i]
                if graph[ay][ax] == 0 and not visited[ay][ax]:
                    queue.append((ax, ay))
                    graph[ay][ax] = graph[vy][vx] + 1
                    visited[ay][ax] = True


m, n = map(int, sys.stdin.readline().rstrip().split())

# 토마토 박스 그래플 저장하기
graph = [[-1 for _ in range(m+2)] for _ in range(n+2)]
visited = [[False for _ in range(m+2)] for _ in range(n+2)]

for i in range(1, n+1):
    line = list(sys.stdin.readline().rstrip().split())
    temp = list(map(int, line))
    for j in range(1,m+1):
        graph[i][j] = temp[j-1]

# 익은 토마토의 위치(bfs 시작점) 리스트로 만들기
starts = []
for y in range(1, n+1):
    for x in range(1, m+1):
        if graph[y][x] == 1:
            starts.append((x,y))

bfs(graph, starts, visited)


maximum = 0
for row in graph:
    # 안 익은 토마토(0)가 남아있는 경우
    if 0 in row:
        print(-1)
        exit()
    # 모든 토마토가 다 익은 경우, 그 중 가장 오래 걸리는 시간이 전부 익는 데 걸리는 시간임
    elif maximum < max(row):
            maximum = max(row)

print(maximum - 1)
