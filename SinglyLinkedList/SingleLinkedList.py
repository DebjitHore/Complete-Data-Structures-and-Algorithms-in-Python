class Node:
  def __init__(self, value=None):
    self.value = value  #value of node.
    self.next= None     #Reference of next node.
class SingleLinkedList:
  def __init__(self):
    self.head= None  #Head
    self.tail=None   #Tail 
  def __iter__(self): # function to print the linked list to compare original and updated node values
    node= self.head
    while node:
      yield node
      node= node.next
  def insertSLL(self, value, location):
    newNode=  Node(value)
    if self.head is None: # if the SLL is empty we're referencing both the head and tail to newly created node
      self.head= newNode
      self.tail = newNode
    else:
      if location == 0: #inserting element at beginning of SLL
        newNode.next= self.head
        self.head= newNode
      elif location == -1 : # insert element at end of SLL
        newNode.next= None
        self.tail.next= newNode
        self.tail= newNode
      else:
        tempNode= self.head
        index=0
        while index< location-1:
          tempNode= tempNode.next
          index+=1
        nextNode= tempNode.next
        tempNode.next= newNode
        newNode.next= nextNode
        if tempNode == self.tail:
          self.tail = newNode


# Traverse Single Linked List
  def traverseSLL(self): #traversal is O(n) time complexity and O(1) space complexity
    if self.head is None:
      print('Linked List does not exist')
    else:
      tempNode= self.head
      while tempNode is not None:
        print(tempNode.value)
        tempNode= tempNode.next
  # Search for a value in a Single Linked List
  def searchLinkedList(self, nodeValue):  #search is O(n) time complexity and O(1) space complexity
    if self.head is None:
      print('Linked List does not exist')
    else:
      tempNode= self.head
      index=0
      while tempNode is not None:
        if tempNode.value == nodeValue:
          print ('Value exists at location', index)
        index+=1
        tempNode=tempNode.next
      print("Value does not exist")
  def deleteNode(self, location): #time complexity is O(n) and space complexity is O(1)
    if self.head is None:
      print('Single Linked List does not exist')
    else:
      if location == 0 or location ==-1: # deleting either the first or last element of a linked list, checking if the linked list has one or more than one components and implemnating accordingly
        if self.head == self.tail:
          self.head= None
          self.tail = None 
        elif location==0 and self.head != self.tail:
          self.head= self.head.next
        elif location ==-1 and self.head != self.tail:
          tempNode = self.head
          while tempNode is not None:
            if tempNode.next == self.tail:
              break
            tempNode = tempNode.next
          tempNode.next = None 
          self.tail = tempNode
      else: # deleting a node from in between
        tempNode= self.head
        index=0
        while index<location-1:
          tempNode= tempNode.next
          index+=1
        nextNode= tempNode.next
        tempNode.next = nextNode.next


  def deleteEntireLinkedList(self): #Time and Space complexity is O(1)
    if self.head is None:
      print('Linked List does not exist')
    else:
      self.head= None
      self.tail = None


singlylinkedlist= SingleLinkedList()
singlylinkedlist.insertSLL (0,0)
singlylinkedlist.insertSLL (1,1)
singlylinkedlist.insertSLL (2,1)
singlylinkedlist.insertSLL (3,1)

singlylinkedlist.insertSLL(56, 2)
print([node.value for node in singlylinkedlist])

singlylinkedlist.traverseSLL()
#singlylinkedlist.searchLinkedList(56)
singlylinkedlist.searchLinkedList(66)

singlylinkedlist.deleteNode(-1)
#singlylinkedlist.deleteNode(2)
print([node.value for node in singlylinkedlist])

singlylinkedlist.deleteEntireLinkedList()
print([node.value for node in singlylinkedlist])



