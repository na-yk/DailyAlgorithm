import sys

n, k = map(int, sys.stdin.readline().split())

count = 0

# while (n > 1):
#     if n%k == 0:
#         n = n/k
#         count+=1
#     else:
#         n-=1
#         count+=1

while (n > 1):
    target = (n//k)*k
    count += (n-target)

    n = target//k
    count += 1

print(count)