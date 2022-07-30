class Node:
	def __init__(self, value=None):
		self.value=value
		self.next=None
class CircularSinglyLinkedList:
	def __init__(self):
		self.head= None
		self.tail= None
	def __iter__(self):
		node= self.head
		while node:
			yield node
			if node.next==self.head:
				break
			node=node.next

#Function to create a Circular Single Linked List

	def CreateCSLL(self, nodeValue):
		node=Node(nodeValue)
		node.next=node
		self.head= node 
		self.tail= node 
		return "The CSLL has been created"
# Insertion of a new node in a circular single linked list
	def insertCSLL(self, value, location):
		if self.head is None:
			return "The head reference is null"
		else:
			newNode= Node(value)
			if location == 0: #insertion at beginning of single linked list
				newNode.next= self.head
				self.head= newNode
				self.tail.next= newNode
			elif location == -1:
				newNode.next= self.head
				self.tail.next= newNode
				self.tail= newNode
			else:
				tempNode= self.head
				index= 0

				while index<location-1:
					tempNode= tempNode.next
					index+=1
				nextNode=tempNode.next
				tempNode.next= newNode
				newNode.next =  nextNode
			return "Node has been successfully inserted"
# Traverse Circular Single Linked List
#traversal is O(n) time complexity and O(1) space complexity
	def traverseSLL(self): 
		if self.head is None:
			print('Linked List does not exist')
		else:
			tempNode= self.head
			while True:
				print(tempNode.value)
				tempNode= tempNode.next
				if tempNode == self.head:
					break

#search is O(n) time complexity and O(1) space complexity
	  	
	def searchLinkedList(self, nodeValue):
	  if self.head is None:
	  	print('Linked List does not exist')
	  else:
	  	tempNode= self.head
	  	index=0
	  	counter=0
	  	while tempNode:
	  		if tempNode.value == nodeValue:
	  			print ('Value exists at location', index)
	  			counter+=1
	  		index+=1
	  		tempNode=tempNode.next
	  		if tempNode == self.tail.next and counter==0:
	  			print("The particular node value does not exist")
	  			break



circularSLL= CircularSinglyLinkedList()
circularSLL.CreateCSLL(nodeValue=55)



circularSLL.insertCSLL(0,0) #insert at beginning

circularSLL.insertCSLL(2,1) #insert at random location

circularSLL.insertCSLL(3,1) #insert at random location

circularSLL.insertCSLL(2,2) #insert at middle



print([node.value for node in circularSLL])

circularSLL.traverseSLL()
circularSLL.searchLinkedList(55)
circularSLL.searchLinkedList(11)