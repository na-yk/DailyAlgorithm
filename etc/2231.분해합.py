# BOJ 2231 분해합
# 브루트포스

import sys

input = sys.stdin.readline().rstrip() # 입력받기
n = int(input)

result = 1

while(result<n):
    temp = 0
    cur = str(result)
    for i in range(len(cur)):
        temp += int(cur[i])
    if (temp+result == n):
        break
    else:
        result+=1

if (result == n):
    print(0)
else:
    print(result)
