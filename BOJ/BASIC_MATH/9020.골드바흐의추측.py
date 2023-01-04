"""
BOJ#9020 골드바흐의 추측
기본 수학 2
"""

import sys
from math import sqrt

def is_prime(n):
    if n==1:
        return False
    elif n!=2 and n%2==0:
        return False
    else:
        for i in range(2,int(sqrt(n))+1):
            if n%i == 0:
                return False
            else:
                continue
        
    return True


# main
t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    a = n//2
    b = n//2

    while (not is_prime(a) or not is_prime(b)):
        a-=1
        b+=1
    
    print(a,b)