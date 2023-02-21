"""
BOJ#1920 수 찾기
이분 탐색
"""

import sys

def binary_search(data, start, end, target):
    if start > end:
        return 0

    mid = (start + end) // 2
    if data[mid] == target:
        return 1
    elif data[mid] > target:
        start = start
        end = mid - 1
        return binary_search(data, start, end, target)
    elif data[mid] < target:
        start = mid + 1
        end = end
        return binary_search(data, start, end, target)




n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort()

for i in range(m):
    start = 0
    end = len(data) - 1
    target = targets[i]
    result = binary_search(data, start, end, target)
    print(result)
