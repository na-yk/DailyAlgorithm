"""
BOJ#9465
DP
"""

import sys

def main():
    T = int(sys.stdin.readline().rstrip())
    answers = []
    for test_case in range(T):
        n = int(sys.stdin.readline().rstrip())

        sticker = []
        for i in range(2):
            row = list(map(int, sys.stdin.readline().split()))
            sticker.append(row)
        answers.append(getMax(n, sticker))

    for answer in answers:
        print(answer)

        
    

def getMax(n, sticker):
    for col in range(n):
        if col == 0:
            continue
        elif col == 1:
            sticker[0][col] += sticker[1][col-1]
            sticker[1][col] += sticker[0][col-1]
        else:
            memo_up = sticker[1][col-1] if sticker[1][col-1] > sticker[1][col-2] else sticker[1][col-2]
            memo_down = sticker[0][col-1] if sticker[0][col-1] > sticker[0][col-2] else sticker[0][col-2]

            sticker[0][col]+=memo_up
            sticker[1][col]+=memo_down

    result = 0
    for row in sticker:
        if (result < max(row)):
            result = max(row)
    
    return result

if __name__ == "__main__":
    main()