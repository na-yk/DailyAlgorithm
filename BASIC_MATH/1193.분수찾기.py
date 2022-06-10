"""
BOJ#1193 분수 찾기
기본 수학 1
"""

import math
import sys

def func(a,b,c):
    return (-b+math.sqrt(b**2-4*a*c))/2*a


x = int(sys.stdin.readline().rstrip())

n = int(func(1,-1,2-2*x))
k = x-((n-1)*n/2)


if (n%2 == 0):
    print("%d/%d"%(k,n-k+1))
else:
    print("%d/%d"%(n-k+1,k)) 
    