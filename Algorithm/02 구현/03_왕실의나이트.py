import sys

loc = sys.stdin.readline().rstrip()

x, y = ord(loc[:1])-ord('a')+1, int(loc[1:])

dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]

x_cases = []
y_cases = []
for i in range(8):
    x_cases.append(x+dx[i])
    y_cases.append(y+dy[i])

result = 0
for j in range(8):
    if x_cases[j] in range(1, 9):
        if y_cases[j] in range(1, 9):
            result+=1

print(result)