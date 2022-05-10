"""
BOJ#11729 하노이 탑 이동 순서
재귀
"""

import sys

def hanoi_tower(n,frm,tmp,to,result):
    if (n == 1):
        result.append(frm)
        result.append(to)        
    else:
        hanoi_tower(n-1,frm,to,tmp,result)
        result.append(frm)
        result.append(to)
        hanoi_tower(n-1,tmp,frm,to,result)


n = sys.stdin.readline().rstrip()
n = int(n)
result = []
hanoi_tower(n,1,2,3,result)

print(len(result)//2)
for i in range(len(result)):
    if i%2 == 0:
        print(result[i],end=" ")
    else:
        print(result[i])