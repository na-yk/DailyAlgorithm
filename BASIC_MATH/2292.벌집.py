"""
BOJ#2292 벌집
기본 수학
"""

import math
import sys

def func(a,b,c):   # 근의 공식, 양수인 해 반환
    return (-b+math.sqrt(b**2-4*a*c))/2*a
    

n = int(sys.stdin.readline().rstrip())

if n == 1:
    result = 1
else:
    result = int(func(1,-3,(8-n)/3))    # 3*x^2-9*x+8-n <= n <= 3*x^2-3*x+1-n

print(result)