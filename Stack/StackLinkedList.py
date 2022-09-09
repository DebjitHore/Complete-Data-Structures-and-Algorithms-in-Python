class Node:
	def __init__(self, value= None):
		self.value= value
		self.next=  next


class LinkedList:
	def __init__(self):
		self.head= None


	def __iter__(self):
		curNode= self.head
		while curNode:
			yield curNode
			curNode= curNode.next


class Stack:
	def __init__(self):
		self.LinkedList= LinkedList()

	def __str__(self):
		values= [str(x.value) for x in self.LinkedList]
		return '\n'.join(values)

	def isEmpty(self):
		if self.LinkedList.head == None:
			return True
		else:
			return False


	def push(self, value):
		node= Node(value)
		node.next= self.LinkedList.head
		self.LinkedList.head= node

	def pop(self):
		if self.isEmpty():
			return "Stack empty"
		else:
			nodeValue= self.LinkedList.head.value
			self.LinkedList.head= self.LinkedList.head.next #head points to the next node
			return nodeValue

	def peek(self):
		if self.isEmpty():
			return "Stack empty"
		else:
			nodeValue= self.LinkedList.head.value
			return nodeValue

	def deleteStack(self):
		self.LinkedList.head.value= None
		return "Stack has been deleted"





customStack= Stack()
print(customStack.isEmpty())

customStack.push(12)
customStack.push(121)
customStack.push(1212)

print(customStack)

print('Testing Pop Method')

customStack.pop()
print(customStack)
print('-------')
print(customStack.peek())

print(customStack.deleteStack())

