"""
BOJ#1931
회의실 배정
"""

import sys

def main():
    
    answer = 1

    n = int(sys.stdin.readline().rstrip())
    times = []
    for _ in range(n):
        times.append(list(map(int, sys.stdin.readline().split())))
    
    times.sort(key=lambda x: (x[1], x[0]))  # 회의 종료 시간 기준으로 정렬

    last = times[0][1]
    for i in range(1, n):
        start, end = times[i]
        if start < last:
            pass
        else:
            answer+=1
            last = end
    
    print(answer)	# 결과 출력


if __name__ == "__main__":
    main()