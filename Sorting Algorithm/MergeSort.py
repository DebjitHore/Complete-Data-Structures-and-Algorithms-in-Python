# Merge sort


def merge_sort(customList):
	if len(customList)>1:
		left_arr= customList[:len(customList)//2]
		right_arr = customList[len(customList)//2:]

		#recursion
		merge_sort(left_arr)
		merge_sort(right_arr)

		#merge 
		i=j=k=0
		# i is left arr idx, j is right arr idx and k is merged arr idx
		while i<len(left_arr) and j<len(right_arr):
			if left_arr[i]<right_arr[j]:
				customList[k]=left_arr[i]
				i+=1

			else:
				customList[k]=right_arr[j]
				j+=1
			k+=1

		 # if all elements from right array are inserted but left_arr has leftover elements
		while i< len(left_arr):
		 	customList[k]= left_arr[i]
		 	i+=1
		 	k+=1
		 #similar but reverse case

		while j< len(right_arr):
			customList[k]= right_arr[j]
			j+=1
			k+=1
	return customList

customList=[2, 1, 7, 3, 5, 5,  6]
print(merge_sort(customList))


