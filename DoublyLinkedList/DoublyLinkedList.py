class Node:
 	def __init__(self, value=None):
 		self.value= value
 		self.next= None 
 		self.prev= None

class DoublyLinkedList:
 	def __init__(self):
 		self.head=None
 		self.tail=None

 	# Default method to print the Linked List
 	def __iter__ (self):
 		node= self.head
 		while node:
 			yield node
 			node= node.next

 	# Creation of Double Linked List

 	def createDLL(self, nodeValue):
 		node= Node(nodeValue)
 		node.prev= None
 		node.next= None 
 		self.head = node
 		self.tail= node

 	#Insertion of node in a Double Linked List
 	def insertNode(self, value, location):
 		if self.head is None:
 			print ("Linked list does not exist")
 		else:
 			newNode= Node(value)
 			if location==0:
 				newNode.prev= None
 				newNode.next= self.head
 				self.head.prev= newNode
 				self.head = newNode
 			elif location ==-1:
 				newNode.next= None 
 				newNode.prev= self.tail
 				self.tail.next= newNode
 				self.tail= newNode
 			else:
 				tempNode= self.head
 				index=0
 				while index<location-1:
 					tempNode=tempNode.next
 					index+=1
 				nextNode= tempNode.next
 				newNode.next= nextNode
 				newNode.prev= tempNode
 				nextNode.prev =newNode
 				tempNode.next=newNode
 	def traverseDLL(self):
 		if self.head is None:
 			print('Linked List does not exist')
 		else:
 			tempNode= self.head
 			while tempNode is not None:
 				print(tempNode.value)
 				tempNode=tempNode.next

 	def reverseTraversal(self):
 		if self.head is None:
 			print("Linked List does not exist")
 		else:
 			tempNode=self.tail
 			while tempNode is not None:
 				print(tempNode.value)
 				tempNode=tempNode.prev
 	def searchLinkedList(self, nodeValue):  #search is O(n) time complexity and O(1) space complexity
 		if self.head is None:
 			print('Linked List does not exist')
 		else:
 			tempNode= self.head
 			index=0
 			counter=0
 			while tempNode is not None:
 				if tempNode.value == nodeValue:
 					print ('Value exists at location', index)
 					counter+=1
 				index+=1
 				tempNode=tempNode.next
 			if counter==0:
 				print("Value does not exist")

 	#Delete a node from a Double Linked List

 	def deleteNodeDLL(self, location):
 		if self.head is None:
 			print("Doubly Linked List does not exist")
 		else:
 			if location == 0: #delete the first node, has two cases, i.e. if there is just one or multiple nodes in the Doubly Linked List
 				if self.head == self.tail:
 					self.head = None 
 					self.tail = None 
 				else:
 					self.head= self.head.next 
 					self.head.prev= None
 			elif location==-1:
 				if self.head == self.tail:
 					self.head = None 
 					self.tail = None
 				else:
 					self.tail= self.tail.prev
 					self.tail.next= None
 			else:
 				tempNode= self.head
 				index=0
 				while index<location-1:
 					tempNode= tempNode.next
 					index+=1
 				nextNode = tempNode.next
 				tempNode.next = nextNode.next
 				nextNode.next.prev = tempNode
 	def deleteEntireDLL(self):
 		'''
 		Setting the head and tail to None does not work for a Doubly Linked List does not work 
 		because the nodes are referenced back and forth, so we need to set all nodes 
 		references to null explicitly.

 		'''
 		if self.head == None:
 			print("The double linked list does not exist")
 		else:
 			tempNode = self.head
 			while tempNode:
 				tempNode.prev= None
 				tempNode= tempNode.next 
 			self.head= None 
 			self.tail = None 
 			print("The DLL has been successfully deleted, printing it.")
 			print([node.value for node in doubleLinkedList])
 			

#Testing creation
doubleLinkedList= DoublyLinkedList()
doubleLinkedList.createDLL(5)

print([node.value for node in doubleLinkedList])

#Testing insertion
doubleLinkedList.insertNode(0,0)
doubleLinkedList.insertNode(2,1)
doubleLinkedList.insertNode(6,2)
doubleLinkedList.insertNode(13,3)

print([node.value for node in doubleLinkedList])

print("Traversing elements of the Linked list")
doubleLinkedList.traverseDLL()

print("Reverse traversing elements of the Linked list")
doubleLinkedList.reverseTraversal()       

doubleLinkedList.searchLinkedList(5)
doubleLinkedList.searchLinkedList(12)

#testing out deletion 

doubleLinkedList.deleteNodeDLL(-1)

print([node.value for node in doubleLinkedList])

doubleLinkedList.deleteEntireDLL()
