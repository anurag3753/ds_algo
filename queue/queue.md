# Queue (FIFO)
-   Operations:
    - enqueue(x)
    - dequeue()
    - getFront()
    - getRear()
    - isEmpty()
    - size()

## Applications:
    - single resource and multiple consumers
    - synchronization b/w slow and fast devices
    - in OS(semaphores, FCFS Scheduling, Spooling, Buffers for devices like Keyboard)
    - in computer networks(routers/switches and mail queues)
    - Variations:
        - Deque
        - Priority Queue
        - Doubly Ended Priority Queue

## Queue in Python
    - Using List
    - Using Collections.deque
    - Using queue.Queue (used in multithread examples)
    - Our own implementation

### List Implementation for Queue
We do not use list implementation of Queue, since it is not efficient:
- append() :- O(1) `ammortized`
- pop(0)   :- O(n)
```python
q = []
q.append(10) # enqueue
q.append(20)
q.append(30)
print(q)   # [10, 20, 30]
print(q.pop(0)) # [20, 30]
q.append(40)
print(q.pop(0)) # [30, 40]
print(len(q))
print(q[0])
print(q[-1])
```
### Using Deque implement Queue
We need to use this implementation only
- enqueue - O(1)
- dequeue - O(1)
Since deque is based on DLL, and in DLL all 4 operations are O(1)
```python
from collections import Queue
q = deque()     # deque([])
q.append(10)    # deque([10])
q.append(20)    # deque([10, 20])
q.append(30)    # deque([10, 20, 30])
print(q)
print(q.popleft())  #deque([20, 30])
q.append(40)        #deque([20, 30, 40])
print(q.popleft())
print(len(q))       # size()
print(q[0])         # getFront()
print(q[-1])        # getRear()
``` 

## Implement own Queue using Linked List
```python
class Node:
    def __init(self, data):
        self.data = data
        self.next = None

class MyQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.sz = 0
    
    def size(self):
        return self.sz

    def isEmpty(self):
        return self.sz == 0
    
    def getFront(self):
        if self.front is not None:
            return self.front.data
        return None

    def getRear(self):
        if self.rear is not None:
            return self.rear.data
        return None 
    
    def enqueue(self,x):
        temp = Node(x)
        if self.rear is None:
            self.front = temp
        else:
            self.rear.next = temp
        self.rear = temp
        self.sz += 1

    def dequeue(self):
        if self.front is None:
            return None
        else:
            res = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            self.sz -= 1
            return res

# Driver Code
q = MyQueue()
q.enqueue(10)
q.enqueue(20)
q.dequeue()
```

## Queue Implementation using Circular List
```python
class MyQueue:
    def __init__(self, c):
        self.capacity = c
        self.queue = [None]*c
        self.front = self.rear = -1

    def isEmpty(self):
        return self.front == -1 and self.rear == -1

    def enqueue(self, data):
        if (self.rear + 1) % self.capacity == self.front:
            print("\nQueue Full")
        elif (self.front == -1):
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear+1)%self.capacity
            self.queue[self.rear] = data
        
    def dequeue(self):
        if (self.front == -1):
            print("Queue is Empty\n")
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            return temp
```
