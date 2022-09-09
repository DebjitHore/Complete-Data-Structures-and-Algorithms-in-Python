#Creating a Stack with Limited Size

class Stack:
	def __init__(self, maxSize):
		self.maxSize=maxSize
		self.list= []

	def __str__(self):
		values= self.list.reverse()
		values= [str(x) for x in self.list]
		return '\n'.join(values)

	#isEmpty

	def isEmpty(self):
		if self.list== []:
			return True
		else:
			return False

	#isFull checks if the stack has reached its maximum capacity
	def isFull(self):
		if len(self.list) == self.maxSize:
			return True
		else: 
			return False

	def push(self, value):
		if self.isFull():
			return "The stac is full"
		else:
			self.list.append(value)
			return "Element has been successfully inserted"

	def pop(self):
		if self.isEmpty():
			return "No element is stack"
		else:
			return self.list.pop()


	def peek(self):
		if self.isEmpty():
			return "No element is stack"
		else:
			return self.list[-1]

	def deleteStack(self):
		self.list = None


