"""
BOJ#10773 제로
자료구조-스택
"""

import sys

class Stack():
    def __init__(self):
        self.items = []
    def push(self,val):
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
        return self.__len__() == 0  #스택 길이가 0이면 1을 반환, 아니면 0을 반환


line_num = int(sys.stdin.readline().rstrip())

stack = Stack()
result = 0

for i in range(line_num):
    input = int(sys.stdin.readline().rstrip())

    if input == 0:
        result-=stack.pop()
    else:
        stack.push(input)
        result+=input
        
print(result)
