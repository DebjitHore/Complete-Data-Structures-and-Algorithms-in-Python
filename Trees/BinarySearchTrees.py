#implementing binary search tree
from collections import deque
class BSTNode:
	def __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild= None


def insertNodeBST(rootNode, nodeValue):
	if rootNode.data is None:
		rootNode.data= nodeValue
	elif nodeValue<= rootNode.data:
		if rootNode.leftChild is None:
			rootNode.leftChild = BSTNode(nodeValue)
		else:
			insertNodeBST(rootNode.leftChild, nodeValue)
	else:
		if rootNode.rightChild is None:
			rootNode.rightChild =BSTNode(nodeValue)
		else:
			insertNodeBST(rootNode.rightChild, nodeValue)
	return "Node has been successfully inserted"

def preOrderTraversal(rootNode):
	if not rootNode:
		return
	print(rootNode.data)
	preOrderTraversal(rootNode.leftChild)
	preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
	if not rootNode:
		return
	inOrderTraversal(rootNode.leftChild)
	print(rootNode.data)
	inOrderTraversal(rootNode.rightChild)
def postOrderTraversal(rootNode):
	if not rootNode:
		return
	postOrderTraversal(rootNode.leftChild)
	inOrderTraversal(rootNode.rightChild)
	print(rootNode.data)

def levelOrderTraversal(rootNode):
	if not rootNode:
		return
	customQueue= deque()
	customQueue.append(rootNode)
	while len(customQueue)>0:
		root= customQueue.popleft()
		print(root.data)
		if root.leftChild is not None:
			customQueue.append(root.leftChild)
		if root.rightChild is not None:
			customQueue.append(root.rightChild)

def searchBinaryTree(rootNode, nodeValue):
	if rootNode.data is None and rootNode.leftChild.data is None and rootNode.rightChild.data is None:
		return "Not found"
	if rootNode.data == nodeValue:
		print("Value has been found")
	elif nodeValue< rootNode.data:
		if rootNode.leftChild.data==nodeValue:
			print("Value has been found")
		else:
			searchBinaryTree(rootNode.leftChild, nodeValue)
	else:
		if rootNode.rightChild.data == nodeValue:
			print("Value has been found")
		else:
			searchBinaryTree(rootNode.rightChild, nodeValue)

def minValueNode(bstNode):
	currentNode= bstNode
	while currentNode.leftChild is not None:
		currentNode = currentNode.leftChild
	return currentNode 


def deleteNodeBST(rootNode, nodeValue):
	if rootNode is None:
		return rootNode
	if nodeValue< rootNode.data:
		rootNode.leftChild = deleteNodeBST(rootNode.leftChild, nodeValue)
	elif nodeValue>rootNode.data:
		rootNode.rightChild = deleteNodeBST(rootNode.rightChild, nodeValue)
	else:
		if rootNode.leftChild is None:
			tempNode = rootNode.rightChild
			rootNode=None
			return tempNode
			

		if rootNode.rightChild is None:
			tempNode = rootNode.leftChild
			rootNode= None
			return tempNode
		tempNode= minValueNode(rootNode.rightChild)
		rootNode.data = tempNode.data
		rootNode.rightChild = deleteNodeBST(rootNode.rightChild, tempNode.data)
	return rootNode

def deleteBST(rootNode):
	if not rootNode:
		return None
	else:
		rootNode.data= None
		rootNode.rightChild= None
		rootNode.leftChild = None
	return "The BST has been successfully deleted"

newBST = BSTNode(None)
print(insertNodeBST(newBST, 70))
print(insertNodeBST(newBST, 50))




print(newBST.data)
print(newBST.leftChild.data)

print(insertNodeBST(newBST, 90))
print(insertNodeBST(newBST, 30))
print(insertNodeBST(newBST, 60))
print(insertNodeBST(newBST, 80))
print(insertNodeBST(newBST, 100))
print(insertNodeBST(newBST, 20))
print(insertNodeBST(newBST, 40))
print(insertNodeBST(newBST, 10))
print('\n')
print("PreOrder Traversal")
preOrderTraversal(newBST)

print('\n')
print("InOrder Traversal")
inOrderTraversal(newBST)

print('\n')
print("PostOrder Traversal")
postOrderTraversal(newBST)

print('\n')
print("LevelOrder Traversal")
levelOrderTraversal(newBST)
print('\n')
print('Searching for nodes')
searchBinaryTree(newBST, 20)
print('\n')
print('Deleting node valued 20')
deleteNodeBST(newBST, 20)
levelOrderTraversal(newBST)

