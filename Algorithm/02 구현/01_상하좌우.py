import sys

n = int(sys.stdin.readline().rstrip())
plan = sys.stdin.readline().split() #이동 계획

x = 1
y = 1

for i in range(len(plan)):
    if plan[i] == "R" and x < n:
        x+=1
    elif plan[i] == "L" and x > 1:
        x-=1
    elif plan[i] == "U" and y > 1:
        y-=1
    elif plan[i] == "D" and y < n:
        y+=1


print(y, x)
