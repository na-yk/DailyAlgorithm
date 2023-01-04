"""
BOJ#10250 ACM호텔
기본 수학 1
"""

import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    h,w,n = map(int, sys.stdin.readline().split())
    if (n%h == 0):
        print(h*100+n//h)
    else:
        print((n%h)*100+n//h+1)