"""
BOJ#10870 피보나치 수 5
재귀
"""
import sys
sys.setrecursionlimit(10**6)

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)   



n = sys.stdin.readline().rstrip()
n = int(n)
print(fibonacci(n))