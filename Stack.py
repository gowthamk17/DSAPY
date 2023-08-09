from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, x):
        self.container.append(x)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)

if __name__ == "__main__":
    stk = Stack()
    stk.push(10)
    stk.push(22)
    stk.push(23)
    print(stk.peek())
    stk.pop()
    print(stk.peek())
    print(stk.size())