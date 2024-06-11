"""
BOJ#21317
징검다리 건너기
"""

import sys

def main():
    
    n = int(sys.stdin.readline().rstrip())
    
    
    energy = []
    for _ in range(n-1):
        temp = list(map(int, sys.stdin.readline().split()))
        energy.append(temp)
    
    k = int(sys.stdin.readline().rstrip())

    dp = [0 for _ in range(n)]
    k_dp = [0 for _ in range(n)]

    if n <= 1:
        print(0)
        return

    dp[1] = energy[0][0]
    
    for i in range(2, n):
        small = dp[i-1] + energy[i-1][0]
        big = dp[i-2] + energy[i-2][1]

        dp[i] = small if small < big else big

    answers = [dp[n-1]]
    for i in range(3, n):
        k_dp[i] = dp[i-3]+k

    if n == 2:
        print(dp[n-1])
        return
    
    all = [dp for _ in range(n-3)]
    for i in range(n-3):
        a = all[i]
        a[i+3] = k_dp[i+3] 
        for j in range(i+4, n):
            small = a[j-1] + energy[j-1][0]
            big = a[j-2] + energy[j-2][1]
            a[j] = small if small < big else big
        
        answers.append(a[n-1])


    print(min(answers))	# 결과 출력


if __name__ == "__main__":
    main()