
# LinkedList implementation

#Creation 
#O(1) space and time complexity 
import QueueLinkedList as queue
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
	customQueue= queue.Queue()
	customQueue.enqueue(rootNode)
	while not(customQueue.isEmpty()):
		root= customQueue.dequeue()
		print(root.value.data)
		if root.value.leftChild is not None:
			customQueue.enqueue(root.value.leftChild)
		if root.value.rightChild is not None:
			customQueue.enqueue(root.value.rightChild)




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

 