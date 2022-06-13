"""
BOJ#1929 소수 구하기
기본 수학 2
"""
import sys
import math

def prime_num(num):
    if num <= 1:
        return False
    else:
        for i in range(2,int(math.sqrt(num)+1)):
            if num%i == 0:
                return False
            else:
                continue
    return True

m,n = map(int,sys.stdin.readline().split())

for i in range(m,n+1):
    if prime_num(i) == True:
        print(i)
    else:
        continue