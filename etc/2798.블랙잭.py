import sys

first_line = sys.stdin.readline()
n,m = map(int, first_line.split()) 

arr = sys.stdin.readline()
arr = list(map(int,arr.split()))

cur = m
result = 0

for i in range(n-1, 2,-1):
    for j in range(i-1, 1,-1):
        for k in range(j-1,0,-1):
            if (arr[i]+arr[j]+arr[k] > m):
                continue
            else:
                result = max(result,arr[i]+arr[j]+arr[k])

print(result)

sys.exit()