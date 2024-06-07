"""
BOJ#21317
징검다리 건너기
"""

import sys

def main():
    
    N = int(sys.stdin.readline().rstrip())

    memo = [[0, 0] for _ in range(N)]

    stones = []
    for i in range(N-1):
        temp = list(map(int, sys.stdin.readline().split()))
        stones.append(temp)
    
    k = int(sys.stdin.readline().rstrip())

    routes = []
    for i in range(N):
        if i == 0:
            memo[i][0] = 0
            memo[i][1] = 0
        elif i == 1:
            memo[i][0] = stones[0][0]
            memo[i][1] = 0
        elif i >= 2:
            small = memo[i-1][0] + stones[i-1][0]
            big = memo[i-2][0] + stones[i-2][1]
            memo[i][0] = small if small < big else big
            prev = i-1 if small < big else i-2
            routes.append(prev)
            if(i >= 3):
                bigger = memo[i-3][0] + k
                memo[i][1] = bigger
    
    routes.append(N-1)
    print(routes)
    print(stones)        
    print(memo)

    gap = 0
    k_used = -1
    for route in routes:
        cur_gap = memo[route][0] - memo[route][1]
        if cur_gap > gap:
            gap = cur_gap
            k_used = route
    
    answer = 0
    if k_used == -1:
        answer = memo[-1][0]
    elif k_used > 0:
        answer = memo[-1][0] - memo[k_used][0] + memo[k_used][1]

    print(answer)


if __name__ == "__main__":

    main()
