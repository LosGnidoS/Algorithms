#!/usr/bin/python3
# MADE by LosGnidoS

'''QUICKSORT FUNCTION
1.DEFINE THE BASE CASE
2.IMPLEMENT THE QUICK SORTING ALGORITHN
3.PRINT THE FUNCTION'''


def quickSort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		
		less = [i for i in array[1:]
			if i <= pivot]
		
		greater = [i for i in array[1:]
			   if i > pivot]
		
		return quickSort(less) + [pivot]\
	+ quickSort(greater)

arr = [56,4,5,7,8,4,6,82,56,4,63,7,56]

print(quickSort(arr))

