import sys

n, m = map(int, sys.stdin.readline().split())
a, b, way = map(int, sys.stdin.readline().split())

game_map = []
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    game_map.append(row)

ways = [0, 1, 2, 3]  # 북,동,남,서
steps = [(-1,0), (0,1), (1,0), (0,-1)]
result = 0

game_map[a][b] = 2

while True:
    scan=0
    for i in range(4):
        scan+=1
        way = ways[ways.index(way)-1]
        print(way)
        to_y, to_x = a+steps[way][0], b+steps[way][1]
        if to_x < 0 or to_x > m-1 or to_y < 0 or to_y > n-1:
            continue
        elif game_map[to_y][to_x] == 1 or game_map[to_y][to_x] == 2:
            continue
        elif game_map[to_y][to_x] == 0:
            a = to_y
            b = to_x
            print(a,b)
            game_map[to_y][to_x] = 2
            break
    if scan == 4:
        to_y = a-steps[way][0]
        to_x = b-steps[way][1]
        if to_x < 0 or to_x > m - 1 or to_y < 0 or to_y > n - 1:
            break
        elif game_map[to_y][to_x] == 1:
            break
        elif game_map[to_y][to_x] == 2:
            a, b = to_y, to_x
        else:
            a, b = to_y, to_x
    else:
        continue

for row in game_map:
    for i in row:
        if i == 2:
            result+=1
    print(row)

print(result)