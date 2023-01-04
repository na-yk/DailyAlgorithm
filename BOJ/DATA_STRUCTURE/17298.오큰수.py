"""
BOJ #17298 오큰수
자료구조 - 스택
"""

import sys

class Stack():
    def __init__(self):
        self.items = []
    def push(self, val):
        self.items.append(val)
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty.")
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty.")
    def __len__(self):
        return len(self.items)
    def is_empty(self):
        return self.__len__()==0

    
n = int(sys.stdin.readline().rstrip())
input = sys.stdin.readline().rstrip()
input = input.split(" ")

input.reverse()

seq = Stack()
nge = Stack()

for i in range(n):
    input[i] = int(input[i])
    while(not seq.is_empty()):
        if seq.top() <= input[i]:
            seq.pop()
        else: break
    if seq.is_empty():
        nge.push(-1)
    else:
        nge.push(seq.top())
    seq.push(input[i])

while(not nge.is_empty()):
    print(nge.pop(),end=" ")