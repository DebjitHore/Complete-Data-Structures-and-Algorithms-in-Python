class Node:
	def __init__(self, value=None):
		self.value= value
		self.prev= None
		self.next= None
class CircularDoublyLL:
	def __init__(self):
		self.head= None
		self.tail= None 


	def __iter__(self):
		node=self.head
		while node:
			yield node
			node= node.next
			if node==self.tail.next:
				break


	#Creation of a circular double linked list
	def createLinkedList(self, nodeValue):
		newnode= Node(nodeValue)
		self.head= newnode
		self.tail= newnode
		newnode.prev= newnode
		newnode.next = newnode
		return "The CDLL is created successfully"

	def insertNewNode(self, value, location):
		if self.head is None:
			print("The linked list does not exist")
		else:
			newnode= Node(value)
			if location == 0:
				newnode.prev= self.tail
				newnode.next= self.head
				self.head.prev= newnode
				self.head= newnode
				self.tail.next=newnode
			if location==-1:
				newnode.prev=self.tail
				newnode.next= self.head
				self.tail.next= newnode
				self.head.prev= newnode
				self.tail=newnode
			else:
				tempnode= self.head
				index=0
				while index<location-1:
					tempnode= tempnode.next
					index+=1
				nextnode= tempnode.next
				tempnode.next= newnode
				newnode.prev= tempnode
				newnode.next= nextnode
				nextnode.prev= newnode




#Testing creation of the Linked List
circularDoubleLinkedList= CircularDoublyLL()
print(circularDoubleLinkedList.createLinkedList(12))

print([node.value for node in circularDoubleLinkedList])

# Testing Insertion

circularDoubleLinkedList.insertNewNode(0,0)
circularDoubleLinkedList.insertNewNode(1, 1)
circularDoubleLinkedList.insertNewNode(2,2)
circularDoubleLinkedList.insertNewNode(23, -1)
print([node.value for node in circularDoubleLinkedList])