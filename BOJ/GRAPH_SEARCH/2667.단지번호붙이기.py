"""
BOJ#2667 단지 번호 붙이기
그래프 탐색
"""

import sys
from collections import deque

def bfs(graph, sx, sy, visited):
    # 시작점이 집이 아닌 위치(0)이거나 이미 방문한 위치인 경우 0 반환
    if graph[sy][sx] == 0 or visited[sy][sx] == True:
        return 0
    
    # 시작점이 집의 위치(1)이고 아직 방문하지 않은 위치인 경우 bfs 시작
    queue = deque()
    queue.append((sx, sy))
    visited[sy][sx] = True
    count = 1   # 가구 수를 저장하는 변수

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    while(queue):
        vx, vy = map(int, queue.popleft())
        # 인접 위치에 대해 탐색
        for i in range(4):
            ax = vx + dx[i]
            ay = vy + dy[i]
            if graph[ay][ax] == 1 and visited[ay][ax] == False:
                queue.append((ax, ay))
                count += 1
                visited[ay][ax] = True

    return count


n = int(sys.stdin.readline())
graph = [[0 for _ in range(n+2)] for _ in range(n+2)]
visited = [[0 for _ in range(n+2)] for _ in range(n+2)]

for i in range(1, n+1):
    line = list(sys.stdin.readline().rstrip())
    for j in range(1, n+1):
        graph[i][j] = int(line[j-1])

result = []
for i in range(1, n+1):
    for j in range(1, n+1):
        count = bfs(graph, i, j, visited)
        if count > 0:
            result.append(count)


print(len(result))  # 단지 수 출력

# 각 단지 별 가구 수 오름차순 출력
result.sort()
for num in result:
    print(num)