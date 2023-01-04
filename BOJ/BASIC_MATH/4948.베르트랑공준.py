"""
BOJ#4948 베르트랑 공준
기본 수학 2
"""

import sys
from math import sqrt

def prime_num(num):
    if num == 1:
        return False
    elif num!=2 and num%2==0:
        return False
    else:
        for i in range(2,int(sqrt(num)+1)):
            if num%i == 0:
                return False
            else:
                continue
    return True

def eratos(n):  # 에라토스테네스의 체
    end = 2*n
    nums=[]
    for i in range(2,end+1): # 2~2n까지의 수로 이루어진 리스트 생성한다
        nums.append(i)
    for i in range(len(nums)):
        if nums[i]==0:  # 소수의 배수라서 제거한(0으로 바꾼) 수에 대해서는 판단하지 않는다
            continue
        elif prime_num(nums[i]):  # 이 수가 소수라면,
            multiples = end//nums[i]    # multiples: 전체 수 중 이 수의 배수의 개수
            if multiples<=1:    
                continue
            else:
                for j in range(1,multiples):    # 이 수를 제외하고, 이 수의 배수를 모두 제거한다(0으로 바꾼다)
                    index = i+j*nums[i]
                    nums[index]=0
        
    return nums

def count_prime(array):    # 해당 리스트에서 소수의 개수를 세는 함수
    cnt=0
    for i in range(len(array)):
        if array[i] != 0:
            cnt+=1
        else:
            continue
    
    return cnt


sample = eratos(123456) # n의 최대 범위 = 123456

while (True):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    elif n == 1:
        print(1)
    else:   
        temp = sample[n-1:2*n-1]    # n ~ 2*n 범위를 슬라이싱
        print(count_prime(temp))