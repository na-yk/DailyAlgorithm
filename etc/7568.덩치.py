"""
BOJ#7568 덩치
브루트포스
"""

import sys

first_line = sys.stdin.readline().rstrip() # 사람 수 입력
n = int(first_line)


arr =[]
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    arr.append([x,y])

rank = [0 for i in range(n)]


for i in range(n):
    for j in range(n):
        if (arr[i][0]<arr[j][0]) and (arr[i][1]<arr[j][1]):
                rank[i]+=1
        

for k in rank:
    print(k+1,end=" ")

 

