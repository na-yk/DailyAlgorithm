"""
BOJ#1712 손익분기점
기본 수학 1
"""

# a+b*result < c*result
# a<(c-b)*result

import sys

a,b,c = map(int, sys.stdin.readline().split())


if ((c-b) <= 0):
    print(-1)
    sys.exit()
else:
    result = a//(c-b)+1

print(result)