"""
BOJ#10872 팩토리얼
재귀
"""

def factorial(n, result):
    if (n==0):  # 이유는 모르겠으나 문제 출력 조건 맞추기
        print(1)
    elif (n==1):
        print(result)
    elif n > 1:
        factorial(n-1,result*(n-1))


n = int(input())    # 정수 입력
factorial(n,n)
