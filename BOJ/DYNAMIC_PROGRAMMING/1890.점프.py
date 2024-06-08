"""
BOJ#1890
점프
"""

import sys

def main():
    
    n = int(sys.stdin.readline().rstrip())
    board = []
    for i in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        board.append(temp)

    dp = [[0 for _ in range(n)] for _ in range(n)]

    dp[0][0] = 1

    
    for i in range(n):
        for j in range(n):
            if i == n-1 and j == n-1:
                break
            if dp[i][j] > 0:
                right = go(j, n, board[i][j])
                down = go(i, n, board[i][j])
                # print("right = ", right, "down = ", down)
                if right > -1:
                    dp[i][right]+=dp[i][j]
                if down > -1:
                    dp[down][j]+=dp[i][j] 
        
    print(dp[n-1][n-1])	# 결과 출력

def go(l, n, v):
    if l+v >= n:
        return -1
    else:
        return l+v
    
if __name__ == "__main__":
    main()