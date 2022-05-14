"""
#4949 균형잡힌 세상
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
        return self.__len__() == 0


input = " "

while(1):
    input = sys.stdin.readline().rstrip()
    if input == ".":
        sys.exit()
    else:
        stack = Stack()
        sign = 1
        for i in range(len(input)):
            if input[i] == "(" or input[i] == "{" or input[i] == "[":
                stack.push(input[i])
            elif input[i] == ")" or input[i] == "}" or input[i] == "]":
                if stack.is_empty() == 1:
                    sign = 0
                    print("no")
                    break
                elif input[i] == ")":
                    if stack.pop() == "(":
                        continue
                    else:
                        sign = 0
                        print("no")
                        break
                elif input[i] == "}":
                    if stack.pop() == "{":
                        continue
                    else:
                        sign = 0
                        print("no")
                        break
                elif input[i] == "]":
                    if stack.pop() == "[":
                        continue
                    else:
                        sign = 0
                        print("no")
                        break
        if sign == 1:
            if stack.is_empty() == 1:
                print("yes")
            else:
                print("no")