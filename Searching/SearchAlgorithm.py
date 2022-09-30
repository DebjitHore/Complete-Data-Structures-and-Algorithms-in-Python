#implementing linear, binary search

#LinearSearch
import math
def linearSearch(arrayA, value):
	for i in range(len(arrayA)):
		if arrayA[i]== value:
			return i
	return -1


#implementing binary search
#needs a sorted array
def binarySearch(sortedArray, value):
	leftPointer= 0
	rightPointer= len(sortedArray)-1
	middlePointer= math.floor((leftPointer+rightPointer)/2)
	while not(sortedArray[middlePointer]==value) and leftPointer<=rightPointer:
		if sortedArray[middlePointer]>value:
			rightPointer = middlePointer-1
		if sortedArray[middlePointer]<value:
			leftPointer= middlePointer+1
		middlePointer= math.floor((leftPointer+rightPointer)/2)
	if sortedArray[middlePointer]==value:
		return middlePointer
	else:
		return -1













#print(linearSearch([10, 30, 50, 20, 70, 55, 72], 90))

print(binarySearch([1, 3, 6, 9, 12, 15, 32, 77, 93, 95, 99], 94))