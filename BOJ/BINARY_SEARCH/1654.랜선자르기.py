"""
BOJ#1654 랜선 자르기
이분 탐색
"""

import sys

def parametric_search(data, start, end,target):
    result = 0
    for i in data:
        result+=(start//i)

k, n = map(int, sys.stdin.readline())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))
results = {}

data.sort()