"""
BOJ#1912
연속합
"""

import sys

n = int(sys.stdin.readline().rstrip())
seq = list(map(int, sys.stdin.readline().split()))

dp = [seq[i] for i in range(n)]
total = 0

for i in range(1, n):
    if dp[i-1] < 0:
        continue
    else:
        dp[i] += dp[i-1]

print(max(dp))


