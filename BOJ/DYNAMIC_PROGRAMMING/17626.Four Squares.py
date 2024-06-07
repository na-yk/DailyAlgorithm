"""
BOJ#17626
Four Squares
"""

import sys
import math


def main():
    n = int(sys.stdin.readline().rstrip())
    # n = 26
    memo = [0 for _ in range(n+1)]
    
    memo[1] = 1
    for i in range(2, n+1):
        # print(i, "=---========")
        sqr = int(math.sqrt(i))
        if i == sqr**2:
            memo[i] = 1
            continue
        
        temp = 4
        for s in range(1, sqr+1):
            # print(s)
            temp = min(temp, memo[i-(s*s)])
            
        memo[i] = temp + 1

    # print(memo)
    print(memo[n])


if __name__ == "__main__":
    main()
