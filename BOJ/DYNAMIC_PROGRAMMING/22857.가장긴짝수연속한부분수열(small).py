"""
BOJ#22857
가장 긴 짝수 연속한 부분 수열(small)
"""

import sys

def main():
    
    n, k = map(int, sys.stdin.readline().split())
    s = list(map(int, sys.stdin.readline().split()))

    dp = [[0 for _ in range(n)] for _ in range(k+1)]

    for i in range(n):
        dp[i][0] = 0 if s[i]%2 == 1 else 1
        for j in range(1, k+1):
            if i < j:
                dp[i][j] = 0 if s[i]%2 == 1 else 1
            else:
                dp[i][j] = dp[i-1][j] if s[i]%2 else dp[i-1][j]+1

                

    
    print(result)	# 결과 출력


if __name__ == "__main__":
    main()