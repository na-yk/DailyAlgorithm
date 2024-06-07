"""
BOJ#11055
가장 큰 증가하는 부분 수열
"""

import sys

def main():
    
    n = int(sys.stdin.readline().rstrip())
    seq = list(map(int, sys.stdin.readline().split()))
    
    dp = [seq[i] for i in range(n)]

    for i in range(1, n):
        for j in range(i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[j]+seq[i], dp[i]) 
    
    print(max(dp))	# 결과 출력



if __name__ == "__main__":
    main()