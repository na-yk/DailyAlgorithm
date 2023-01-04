"""
BOJ#10828 스택
자료구조
"""

import sys

class Stack():
    def __init__(self):
        self.items=[]
        self.top = -1
    def is_empty(self):
        if self.top == -1:
            print(1)
        else:
            print(0)
    def print_size(self):
        print(len(self.items))
    def push(self,item):
        self.items.append(item)
        self.top+=1
    def pop(self):
        try:
            print(self.items.pop())
            self.top-=1
        except IndexError:
            print(-1)
    def print_top(self):
        try:
            print(self.items[self.top])
        except IndexError:
            print(-1)


n = int(sys.stdin.readline().rstrip())
stack = Stack()

for i in range(n):
    command = sys.stdin.readline().rstrip()
    if "push" in command:
        item = command.split(' ')
        item = int(item[1])
        stack.push(item)
    elif "pop" in command:
        stack.pop()
    elif "size" in command:
        stack.print_size()
    elif "empty" in command:
        stack.is_empty()
    elif "top" in command:
        stack.print_top()

sys.exit(0)
