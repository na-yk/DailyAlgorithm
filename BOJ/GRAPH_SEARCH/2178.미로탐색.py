"""
BOJ#2178 미로 탐색
그래프 탐색
"""

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

visited = [[False] * (m+2) for _ in range(n+2)]     # 방문 여부 저장

# 미로 저장
maze = []
maze.append([0]*(m+2))
for i in range(n):
    temp = [0]
    cur = list(sys.stdin.readline().rstrip())
    cur = list(map(int,cur))
    temp += cur
    temp.append(0)
    maze.append(temp)
maze.append([0]*(m+2))

# 시작점 위치
vx = 1
vy = 1

# 기준점의 상하좌우 판별을 위한 리스트
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# BFS
queue = deque()
queue.append((vx, vy))
visited[vy][vx] = True  # 시작점 (1,1) 방문 처리

while (queue):
    vx, vy = queue.popleft()
    
    # 기준점 상하좌우(인접노드) 판별
    for i in range(4):
        ax = vx+dx[i]
        ay = vy+dy[i]
        if maze[ay][ax] == 1 and not visited[ay][ax]:
            queue.append((ax, ay))
            maze[ay][ax] = maze[vy][vx] + 1     # 시작점에서 해당 노드까지의 거리로 미로의 값을 업데이트
            visited[ay][ax] = True

print(maze[n][m])