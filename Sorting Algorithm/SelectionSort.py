# Implementing Selection Sort

def selectionSort(customList):
	for i in range(len(customList)):
		min_index= i
		for j in range(i+1, len(customList)):
			if customList[min_index]> customList[j]:
				min_index = j
				customList[min_index], customList[i]= customList[i], customList[min_index]  
	print(customList)




customList=[2, 1, 7, 3, 5, 5, 6, 0]
selectionSort(customList)