#Python list implementation of Binary Trees


class BinaryTrees:
	def __init__(self, size):
		self.customList= size*[None]
		self.lastUsedIndex= 0
		self.maxSize= size

	def insertNode(self, value):
		if self.lastUsedIndex +1 == self.maxSize:
			return "Binary Tree is full"
		self.customList[self.lastUsedIndex+1]= value
		self.lastUsedIndex+=1
		return "Value has been successfully inserted"
	def searchNode(self, nodeValue):
		for i in range(len(self.customList)):
			if self.customList[i]==nodeValue:
				return "Successfully found in Binary Trees"
			return "Not Found"

	def preOrderTraversal(self, index):
		if index > self.lastUsedIndex:
			return
		print(self.customList[index])
		self.preOrderTraversal(index*2)
		self.preOrderTraversal(index*2+1)


	def inOrderTraversal(self, index):
		 if index > self.lastUsedIndex:
		 	return
		 self.inOrderTraversal(index*2)
		 print(self.customList[index])
		 self.inOrderTraversal(index*2+1)

	def postOrderTraversal(self, index):
		if index>self.lastUsedIndex:
			return
		self.postOrderTraversal(index*2)
		self.postOrderTraversal(index*2+1)
		print(self.customList[index])

	def levelOrderTraversal(self, index):
		if index>self.lastUsedIndex:
			return
		for i in range(index, self.lastUsedIndex+1):
			print(self.customList[i])
	def deleteNode(self, value):
		if self.lastUsedIndex ==0:
			return
		for i in range(1, self.lastUsedIndex+1):
			if self.customList[i]== value:
				self.customList[i]= self.customList[self.lastUsedIndex]
				self.customList[self.lastUsedIndex]= None
				self.lastUsedIndex-=1 
				return "Node has been successfully deleted"
	def deleteEntireBT(self):
		self.customList= None
		return "Binary Tree successfully deleted"







newBT= BinaryTrees(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
newBT.insertNode("Sprite")
newBT.insertNode("Fanta")

print(newBT.searchNode("DarjeelingTea"))

print('\n')
newBT.preOrderTraversal(1)

print('\n')
newBT.inOrderTraversal(1)

print('\n')
newBT.postOrderTraversal(1)

print('\n')
newBT.levelOrderTraversal(1)


print('\n')
print(newBT.deleteNode('Tea'))
newBT.levelOrderTraversal(1)

print('\n')
print(newBT.deleteEntireBT())

