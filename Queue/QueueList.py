# Queue without list

class Queue:
	def __init__(self):
		self.items=[]

	def __str__(self):
		values= [str(x) for x in self.items]
		return ' '.join(values)

	def isEmpty(self):
		if self.items==[]:
			return True
		else:
			return False

	def enqueue(self, value):
		self.items.append(value)
		return "Element is inserted to the end of the queue"

	def dequeue(self):
		if self.isEmpty():
			return "Nothing to remove from the Queue"
		else:
			return self.items.pop(0)

	def peek(self):
		if self.isEmpty():
			return "Nothing to remove from the Queue"
		else:
			return self.items[0]

	def deleteQueue(self):
		self.items= None
		return "Queue has been deleted"



customQueue= Queue()
print(customQueue.isEmpty())

customQueue.enqueue(1)
customQueue.enqueue(11)
customQueue.enqueue(111)
customQueue.enqueue(1111)

print(customQueue)
print('---------')

customQueue.dequeue()

print(customQueue)
print('---------')


print(customQueue.peek())