"""
BOJ#2839 설탕 배달
기본 수학 1
"""

import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n//5,-1,-1): # 5*x+3*y=n의 x에 넣을 수 있는 가장 큰 수(n//5)부터 0까지 대입해보면서 y를 구함
    x = i
    if (n-5*x)%3 > 0:
        continue
    else:
        print(x+(n-5*x)//3)
        sys.exit()

print(-1) # x에 0까지 대입했는데 적절한 y값을 찾을 수 없으므로 -1 출력