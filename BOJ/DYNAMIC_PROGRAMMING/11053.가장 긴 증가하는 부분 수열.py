"""
BOJ#11053
가장 긴 증가하는 부분수열
"""

import sys

n = int(sys.stdin.readline().rstrip()) # 수열의 크기
seq = list(map(int, sys.stdin.readline().split())) # 수열

dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(0, i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(dp) 