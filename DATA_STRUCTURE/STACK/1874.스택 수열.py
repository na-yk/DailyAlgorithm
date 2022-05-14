"""
#1874 스택 수열
자료구조 - 스택
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
            print("stack is empty.")
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            return 0
    def __len__(self):
        return len(self.items)
    def is_empty(self):
        return self.__len__() == 0


num = int(sys.stdin.readline().rstrip())
seq = []
for i in range(num):
    input = int(sys.stdin.readline().rstrip())
    seq.append(input)

result = [] 
stack = Stack()

flag = 1
j = 1

for i in range(num):
    while(j <= seq[i]):
        stack.push(j)
        result.append('+')
        j+=1
    if stack.top() == seq[i]:
        stack.pop()
        result.append('-')
    else:
        flag = 0
        print("NO")
        break

if flag == 1:
    if stack.is_empty() == 1:
        for i in range (len(result)):
            print(result[i])