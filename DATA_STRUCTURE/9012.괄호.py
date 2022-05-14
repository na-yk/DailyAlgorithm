import sys

class Stack():
    def __init__(self):
        self.items = []
    def push(self,val):
        self.items.append(val)
    def pop(self):
        try:
            self.items.pop()
        except IndexError:
            return 0
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            return 0
    def __len__(self):
        return len(self.items)
    def is_empty(self):
        return self.__len__() == 0


input = sys.stdin.readlines()

for i in range(1,len(input)):
    input[i] = input[i].rstrip()
    if ("(" not in input[i]) or (")" not in input[i]):
        print("NO")
    else:
        sign = 1
        stack = Stack()
        for j in range(len(input[i])):
            if input[i][j] == '(':
                stack.push("(")
            elif input[i][j] == ')':
                if stack.is_empty() == 1:
                    print("NO")
                    sign = 0
                    break
                else:
                    stack.pop()
        if sign == 1:     
            if stack.is_empty() == 1:
                print("YES")
            else:
                print("NO")



                