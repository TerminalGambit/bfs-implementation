class Queue:
    # Implementation of a FIFO (first in first out)
    def __init__(self):
        self.queue = []
    
    # to create an empty queue
    def emptyQueue(self):
        self.queue = []
        return self
    
    # to add an element to the queue
    def addtoQueue(self, x):
        self.queue.append(x)
        return self
    
    # returns the first element of the queue
    def front(self):
        if len(self.queue) == 0:
            raise ValueError("queue is empty")
        return self.queue[0]
    
    # to remove an element from the queue
    def removefromQueue(self):
        if self.queue == []:
            raise ValueError("queue is empty")
        return self.queue.pop(0)