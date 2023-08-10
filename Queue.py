from collections import deque

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, x):
        self.buffer.appendleft(x)

    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(4)
    q.enqueue(3)
    print('q size: ', q.size())
    print(q.dequeue())
    print(q.dequeue())
    print('q size: ', q.size())
    print(q.dequeue())
    print('q is empty: ', q.is_empty())
