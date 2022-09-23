#Implementing Bubble sort


def bubbleSort(customList):
	for i in range(len(customList)-1):
		for j in range(len(customList)-i-1):
			 if customList[j]>customList[j+1]:
			 	customList[j], customList[j+1]= customList[j+1], customList[j]
	print(customList)



customList=[2, 1, 7, 3, 5, 5, 6, 0]
bubbleSort(customList)

def bubbleSortTwo(customList):
	for i in range(len(customList)-1):
		for j in range(i+1, len(customList)):
			 if customList[i]>customList[j]:
			 	customList[i], customList[j]= customList[j], customList[i]
	print(customList)


#bubbleSortTwo(customList)