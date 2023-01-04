"""
BOJ#1978 소수 찾기
기본 수학 2
"""

import sys
import math

def prime_num(num):
    if num <= 1:
        return False
    else:
        for i in range(2,int(math.sqrt(num)+1)):
            if num%i == 0:
                return False
            else:
                continue
    return True


n = int(sys.stdin.readline().rstrip())
nums = list(map(int,sys.stdin.readline().split()))

cnt = 0

for i in range(n):
    if prime_num(nums[i]) == True:
        cnt += 1
    else:
        continue

print(cnt)