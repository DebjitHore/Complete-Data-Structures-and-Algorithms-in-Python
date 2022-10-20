
# LinkedList implementation
from collections import deque
#Creation 
#O(1) space and time complexity 
 
class treeNode:
	def __init__(self, data):
		self.data= data
		self.leftChild= None
		self.rightChild= None

#Traversal
#Preorder (rootNode--> leftSubtree--> rightSubtree)
# O(n) time complexity and space complexity is O(n)
def preTrav(rootNode):
	if not rootNode:
		return
	print(rootNode.data)
	preTrav(rootNode.leftChild)
	preTrav(rootNode.rightChild)

#Inorder (leftSubtree-->rootNode-->rightSubtree)
#O(n) time complexity and O(n) space complexity; because stack memory

def inOrderTraversal(rootNode):
	if not rootNode:
		return
	inOrderTraversal(rootNode.leftChild)
	print(rootNode.data)
	inOrderTraversal(rootNode.rightChild)

#Postorder (leftsubtree-->rightsubtree-->rootNode)

def postOrderTraversal(rootNode):
	if not rootNode:
		return
	postOrderTraversal(rootNode.leftChild)
	postOrderTraversal(rootNode.rightChild)
	print(rootNode.data)

def levelOrderTraversal(rootNode):
  if not rootNode:
    return
  else:
  	customQueue= deque()
  	customQueue.append(rootNode)
  	while len(customQueue)>0:
  		root= customQueue.popleft()
  		print(root.data)
  		if root.leftChild is not None:
  			customQueue.append(root.leftChild)
  		if root.rightChild is not None:
  			customQueue.append(root.rightChild)

def searchNodeBT(rootNode, nodeValue):
	#we will use levelOrderTraversal
	if not rootNode:
		return "Binary Tree does not exist"
	else:
		customQueue= deque()
		customQueue.append(rootNode)
		while len(customQueue)>0:
			 node= customQueue.popleft()
			 if node.data == nodeValue:
			 	 return "Node exists in Binary Tree"
			 if node.leftChild is not None:
			 	customQueue.append(node.leftChild)
			 if node.rightChild is not None:
			 	customQueue.append(node.rightChild)
		return "Node does not exist in Binary Tree "

def insertNode(rootNode, newNode):
	 if not rootNode:
	 	rootNode= newNode
	 else:
	 	customQueue= deque()
	 	customQueue.append(rootNode)
	 	while len(customQueue)>0:
	 		root= customQueue.popleft()
	 		if root.leftChild is not None:
	 			customQueue.append(root.leftChild)
	 		else:
	 			root.leftChild = newNode
	 			return "Successfully inserted"
	 		if root.rightChild is not None:
	 			customQueue.append(root.rightChild)
	 		else:
	 			root.rightChild= newNode
	 			return "Successfully inserted"



def getDeepestNode(rootNode):
	if not rootNode:
		return
	else:
		customQueue= deque()
		customQueue.append(rootNode)
		while len(customQueue)>0:
			root = customQueue.popleft()
			if root.leftChild is not None:
				customQueue.append(root.leftChild)
			if root.rightChild is not None:
				customQueue.append(root.rightChild)
		deepestNode= root
		return deepestNode

def deleteDeepestNode(rootNode, deepestNode):
	if not rootNode:
		return 
	else:
		customQueue= deque()
		customQueue.append(rootNode)
		while len(customQueue)>0:
			root= customQueue.popleft()
			if root.data== deepestNode:
				root.data= None
				return
			if root.rightChild is not None:
				if root.rightChild == deepestNode:
					root.rightChild = None 
					return
				else:
					customQueue.append(rightChild)
			if root.leftChild is not None:
				if root.leftChild is deepestNode:
					root.leftChild = None
					return 
				else:
					customQueue.append(root.leftChild)
def deleteNodeBT(rootNode, node):
	if not rootNode:
		return "Binary Tree does not exist"
	else:
		customQueue = deque()
		customQueue.append(rootNode)
		while len(customQueue)>0:
			root= customQueue.popleft()
			if root.data == node:
				dNode= getDeepestNode(rootNode)
				root.data = dNode.data
				deleteDeepestNode(rootNode, dNode)
				return "Node has been successfully deleted"
			if root.rightChild is not None:
				customQueue.append(root.rightChild)
			if root.leftChild is not None:
				customQueue.append(root.leftChild)
		return "Failed to delete node from given Binary Tree "

def deleteEntireBinaryTree(rootNode):
	if not rootNode:
		return "BT does not exist"
	else:
		rootNode.rightChild=None
		rootNode.leftChild = None 
		rootNode.data=None
		return "BT successfully deleted"




newBT= treeNode("Drinks")
leftChild= treeNode("Hot")
rightChild = treeNode("Cold")
tea=treeNode("Tea")
coffee= treeNode("Coffee")
leftChild.leftChild=tea
leftChild.rightChild=coffee
sprite=treeNode("Sprite")
fanta=treeNode("Faaaaaanta")
rightChild.leftChild=sprite
rightChild.rightChild=fanta
newBT.leftChild = leftChild
newBT.rightChild = rightChild






preTrav(newBT)
print('\n')
inOrderTraversal(newBT)
print('\n')
postOrderTraversal(newBT)
print('\n')
levelOrderTraversal(newBT) 
print('\n')
print(searchNodeBT(newBT, "Tea"))
print('\n')
print(searchNodeBT(newBT, "Cola"))
print('\n')
newNode= treeNode("DarjeelingTea")
print(insertNode(newBT, newNode))
print('\n')
levelOrderTraversal(newBT)
print('\n')
print(getDeepestNode(newBT))
print('\n')
#deepestNode= getDeepestNode(newBT)
#deleteDeepestNode(newBT, deepestNode)
deleteNodeBT(newBT, 'Tea')
levelOrderTraversal(newBT)
print('\n')
deleteEntireBinaryTree(newBT)
levelOrderTraversal(newBT)

 