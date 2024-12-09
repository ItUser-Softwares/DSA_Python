queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue")
print(queue)
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)

class Node:
    
    def __init__(self):
        self.data = None
        self.next = None
    
class Queue:
    #!Queue has max size
    max = 20
    
    def __init__(self):
        self.size = 0
        self.peek_val = None
    
    def isEmpty(self):
        return self.size == 0
    
    def top(self):
        return self.peek_val
    
    def enqueue(self, data):
        if self.isEmpty():
            self.peek_val = data
        
        if self.size < 10:
            self.size += 1
            self.new = data
            self.rear_val = data
        else:
            print("Queue is full")
    
    def dequeue(args):
        pass
    
if __name__ == "__main__":
    queue1 = Queue()
    
    for i in range(1, 10):
        queue1.enqueue(i)
        print(queue1.new)
        
    print(queue1.isEmpty())
    print(queue1.top())
    print(queue1.rear_val)
    