"""
BOJ#2775 부녀회장이 될 테야
기본 수학 1
"""

import sys



t = int(sys.stdin.readline().rstrip())

num =[[0 for col in range(14)] for row in range(15)]
for i in range(15):
    for j in range(14):
        if i == 0:     # 0층 j호에는 j명이 산다
            num[i][j] = j+1
        elif i > 0:    # i층 j호에는 i-1층의 1~j호에 사는 사람의 합만큼 산다
            num[i][j] = sum(num[i-1][:j+1])

for i in range(t):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    print(num[k][n-1])
    