"""
BOJ#1459
걷기
"""

import sys
import math
def main():
    
    x, y, w, s = map(int, sys.stdin.readline().split())
    answer = 0
    if s > 2*w:
        answer = (x+y) *w
    
    else:
        if x < y:
            answer+=x*s
        else:
            answer+=y*s
        
        diff = abs(x-y)
        if s < w:
            answer+= (diff//2)*2*s+(diff%2)*w
        else:
            answer+=diff*w


    print(answer)	# 결과 출력


if __name__ == "__main__":
    main()