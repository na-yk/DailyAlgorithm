"""
BOJ#9655
돌 게임
"""

import sys

SK = True
CY = False

n = int(sys.stdin.readline().rstrip())

dp = [False for _ in range(n+1)]

dp[1] = SK
if n >= 2:
    dp[2] = CY

if n >= 3:
    dp[3] = SK

if n >= 4:  
    for i in range(4, n+1):
        dp[i] = not dp[i-1]

if (dp[n] == True):
    print("SK")
else:
    print("CY")