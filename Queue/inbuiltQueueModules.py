# Collection modules
#collections.deque class
from collections import deque

#deque
customQueue = deque(maxlen=3)
print(customQueue)


#append
customQueue.append(1)
customQueue.append(11)
customQueue.append(111)
print(customQueue)

customQueue.append(43)
print(customQueue)
#popleft
print("Popping the first element")
print(customQueue.popleft())
print(customQueue)

#clear
customQueue.clear()
print(customQueue)


#Queue modules

import queue as q
customQueue = q.Queue(maxsize=3)

#qsize
print(customQueue.qsize())
print(customQueue.empty())

#put
customQueue.put(1)
customQueue.put(11)
customQueue.put(111)
print(customQueue.qsize())


#empty
print(customQueue.empty())

#full

print(customQueue.full())

#get/dequeue
print(customQueue.get())
print("New size after deleting first element")
print(customQueue.qsize())
#task_done

#multiprocessing queue

from multiprocessing import Queue

customQueue = Queue(maxsize=3)

#put
customQueue.put(1)
customQueue.put(11)
customQueue.put(111)
print("Getting the first element")
print(customQueue.get())

