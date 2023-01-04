"""
BOJ#1018 체스판 다시 칠하기
브루트 포스
"""
import sys

def make_board(start):
    chess_board = []
    if start == "W":
        for i in range(8):
            if i%2==0:
                chess_board.append(list("WBWBWBWB"))
            else:
                chess_board.append(list("BWBWBWBW"))
    elif start == "B":
        for i in range(8):
            if i%2==0:
                chess_board.append(list("BWBWBWBW"))
            else:
                chess_board.append(list("WBWBWBWB"))

    return chess_board

def count(cur):
    white_sample = make_board('W')
    black_sample = make_board('B')

    white_cnt = 0
    black_cnt = 0
    for i in range(8):
        for j in range(8):
            if cur[i][j] != white_sample[i][j]:
                white_cnt+=1
            if cur[i][j] != black_sample[i][j]:
                black_cnt+=1
    
    return min(white_cnt,black_cnt)



m,n = map(int,sys.stdin.readline().split())

original = []
for i in range(m):
    row = list(sys.stdin.readline().rstrip())
    original.append(row)

count_all = []
for i in range(m-7):
    for j in range(n-7):
        cur = []
        for k in range(8):
            cur.append(original[i+k][j:j+8])
        count_all.append(count(cur))

print(min(count_all))