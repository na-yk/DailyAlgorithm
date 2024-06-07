import sys

n = int(sys.stdin.readline())

memo = {}

for i in range(1, n+1):
    memo[i] = 0
    if(i == 1) {
        memo[i] = 1
    }

    divide_two = i//2
    remain_two = i%2

    memo[i] += divide_two
    memo[i] += divide_two * memo[1]

    divide_three = i//3
    
    remain_three = i%3
    