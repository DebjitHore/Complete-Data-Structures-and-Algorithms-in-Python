# Queue with fixed capacity
 

class CircularQueue:
    def __init__(self, maxSize):
        self.items= maxSize*[None]
        self.maxSize= maxSize        
        self.start= -1
        self.top=-1

    def __str__ (self):
        values= [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.top +1 == self.start:
            return True
        elif self.start == 0 and self.top+1 == self.maxSize:
            return True
        else:
             return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    

    def enqueue(self, value):
        if self.isFull():
            return "Queue is full"
        else: #insert elements
            if self.top+1== self.maxSize:
                self.top=0
            else:
                self.top+=1
                if self.start==-1:
                    self.start=0
                self.items[self.top]= value
                return "Element is inserted at the end of the Circular Queue"
    def dequeue(self):
        if self.isEmpty():
            return "Queue empty, nothing to delete"
        else:
            firstElement= self.items[self.start]
            start= self.start
            if self.start == self.top: # there is just one element in the queue, both point to same element
                self.start=-1
                self.top = -1
            elif self.start+1 == self.maxSize: #when start has moved to last position so reset the counter
                self.start=0
            else:
                self.start+=1    #when start pointer is in intermediate position
            self.items[start]= None
            return 
    def peek(self):
        if self.isEmpty():
            return "Queue empty, nothing to peek at"
        else:
            return self.items[self.start]

    def delete(self):
        self.items= self.maxSize * [None]
        self.top=-1
        self.start=-1





customCirQueue = CircularQueue(3)

print(customCirQueue.isEmpty())
print("---------")
print(customCirQueue.isFull())
print("---------")
customCirQueue.enqueue(1)
customCirQueue.enqueue(11)
customCirQueue.enqueue(111)
print(customCirQueue)
print("---------")
print(customCirQueue.isFull())
print("---------")
print(customCirQueue.dequeue())
print("---------- ")
print(customCirQueue)
print("---------")
print("Peeking")
print(customCirQueue.peek())
print("Deleting Queue")
customCirQueue.delete()
print(customCirQueue)