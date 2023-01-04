"""
BOJ#2869 달팽이는 올라가고 싶다
기본 수학 1
"""

import sys

a,b,v = map(int,sys.stdin.readline().split())

temp = v-b  # 마지막 날 밤이 되기 전에 정상에 도착할 수도 있으므로 v-(a-(a-b)) = v-b
result = temp//(a-b)

if temp%(a-b) > 0:  # 마지막 날 낮에 정상에 도착하지 못하는 경우
    print(result+1)
else:   
    print(result)