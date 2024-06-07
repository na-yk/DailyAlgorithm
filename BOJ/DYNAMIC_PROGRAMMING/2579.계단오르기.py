"""
BOJ#2579 계단 오르기
다이나믹 프로그래밍
"""

import sys

n = int(sys.stdin.readline())

stair = [0 for _ in range(301)]
dp = [0 for _ in range(301)]

for i in range(1, n+1):
    stair[i] = int(sys.stdin.readline())

dp[1] = stair[1]
dp[2] = stair[1] + stair[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

print(dp[n])
