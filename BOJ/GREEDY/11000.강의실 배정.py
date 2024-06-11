"""
BOJ#11000
강의실 배정
"""

import sys
import heapq

def main():
    
    answer = 1
    n = int(sys.stdin.readline().rstrip())
    times = []
    lasts = []
    heapq.heapify(lasts)
    for _ in range(n):
        times.append(list(map(int, sys.stdin.readline().split())))
    
    times.sort(key=lambda x: (x[0], x[1]))

    heapq.heappush(lasts, times[0][1])
    for i in range(1, n):
        start, end = times[i]
        if start < lasts[0]:
            answer+=1
            heapq.heappush(lasts, end)
        else:
            heapq.heappushpop(lasts, end)

    
    
    print(answer)	# 결과 출력


if __name__ == "__main__":
    main()