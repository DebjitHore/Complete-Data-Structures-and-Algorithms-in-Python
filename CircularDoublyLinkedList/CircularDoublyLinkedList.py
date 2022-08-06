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


	def traverseCDLL(self):
		if self.head is None:
			print("Linked list does not exist baka")
		else:
			tempnode= self.head
			while tempnode:
				print(tempnode.value)
				tempnode=tempnode.next
				if tempnode == self.head:
					break 	
	def reverseTraversal(self):
 		if self.head is None:
 			print("Linked List does not exist")
 		else:
 			tempNode=self.tail
 			while tempNode:
 				print(tempNode.value)
 				tempNode=tempNode.prev
 				if tempNode == self.tail:
 					break
	def searchCDLL(self, nodeValue):
 		if self.head is None:
 			print("Linked list does not exist baka")
 		else:
 			tempnode= self.head
 			index=0
 			counter=0
 			while tempnode:
 				if tempnode.value == nodeValue:
 					print('The value exists at location', index)
 					counter+=1
 				index+=1
 				tempnode=tempnode.next
 				if tempnode == self.head:
 					break
 			if counter==0:
 				print("Value does not exist")

	def deleteNode(self, location):
 		if self.head is None:
 			print("Linked list does not exist baka")
 		else: 
 			if location ==0:
 				if self.head == self.tail:
 					self.head = None 
 					self.head= None
 					self.head.next= None
 					self.tail.prev = None
 				else:
 					self.head= self.head.next
 					self.head.prev= self.tail
 					self.tail.next = self.head
 			elif location==-1:
 				if self.head == self.tail:
 					self.head = None 
 					self.head= None
 					self.head.next= None
 					self.tail.prev = None
 				else:
 					self.tail = self.tail.prev
 					self.tail.next=self.head
 					self.head.prev=self.tail
 			else:
 				tempnode= self.head
 				index=0
 				while index<location-1:
 					tempnode=tempnode.next
 					index+=1
 				nextnode= tempnode.next
 				tempnode.next= nextnode.next
 				nextnode.next.prev= tempnode
	def deleteEntireLinkedList(self):
 		self.tail.next= None
 		tempnode=self.head
 		while tempnode:
 			tempnode.prev = None
 			tempnode = tempnode.next
 		self.head= None
 		self.tail= None
 		print("Successfully deleted")
 		print([node.value for node in self])



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

#Testing traversal

circularDoubleLinkedList.traverseCDLL()

#Testing reverse-traversal

circularDoubleLinkedList.reverseTraversal()

#Searching for a value in the Linked List

circularDoubleLinkedList.searchCDLL(55)
circularDoubleLinkedList.searchCDLL(12)

#Testing deletion 

circularDoubleLinkedList.deleteNode(2)
#circularDoubleLinkedList.deleteNode(0)
print([node.value for node in circularDoubleLinkedList])

#Testing delete

circularDoubleLinkedList.deleteEntireLinkedList() 
