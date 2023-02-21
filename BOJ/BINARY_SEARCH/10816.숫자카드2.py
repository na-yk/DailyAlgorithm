"""
BOJ#10816 숫자 카드 2
이분 탐색
"""

import sys

# def binary_search(data, start, end, target, count):
#     if start > end:
#         return count
#     mid = (start + end) // 2
#
#     if target == data[mid]:
#         count += 1
#         del data[mid]
#         end = len(data)-1
#         return binary_search(data, start, end, target, count)
#     elif target < data[mid]:
#         return binary_search(data, start, mid-1, target, count)
#     elif target > data[mid]:
#         return binary_search(data, mid+1, end, target, count)

def bs_first(data, target):
    start = 0
    end = len(data) - 1

    while(start <= end):
        mid = (start + end) // 2
        if target > data[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return start


def bs_last(data, target):
    start = 0
    end = len(data) - 1

    while(start <= end):
        mid = (start + end) // 2
        if target < data[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return end

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().rstrip().split()))
results = {}

data.sort()

for i in range(m):
    target = targets[i]
    if target in results:
        continue

    first = bs_first(data, target)
    last = bs_last(data, target)

    if (first < 0) or (first > len(data)-1):
        result = 0
    elif (last < 0) or (last > len(data)-1):
        result = 0
    elif data[first] != target or data[last] != target:
        result = 0
    elif first == last:
        result = 1
    else:
        result = last - first + 1

    results[target] = result

for target in targets:
    if target in results:
        print(results[target], end=" ")