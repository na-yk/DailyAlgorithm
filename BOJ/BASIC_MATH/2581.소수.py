"""
BOJ#2581 소수
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

m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

results = []

for i in range(m,n+1):
    if prime_num(i) == True:
        results.append(i)
    else:
        continue

if len(results) == 0:
    print(-1)
else:
    print(sum(results))
    print(min(results))