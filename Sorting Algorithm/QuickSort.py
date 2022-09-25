# implementing quick sort
def quickSort(customList, left, right):
	if left<right: #subarray atleast has two elements
		partition_pos= partition(customList, left, right)
		quickSort(customList, left, partition_pos-1)
		quickSort(customList, partition_pos+1, right)
	return customList



def partition(customList, left, right):
	leftPointer= left
	rightPointer= right-1
	pivot= customList[right]

	while leftPointer<rightPointer:
		while leftPointer<right and customList[leftPointer]<pivot:
			leftPointer+=1
		while rightPointer > left and customList[rightPointer]>pivot:
			rightPointer-=1

		if leftPointer<rightPointer: #swap
			customList[leftPointer], customList[rightPointer]= customList[rightPointer], customList[leftPointer]

	if customList[leftPointer]>pivot:
		customList[leftPointer], customList[right]= customList[right], customList[leftPointer]
	return leftPointer


customList=[2, 1, 7, 3, -5, 7,  6]
print(quickSort(customList, 0, len(customList)-1))
