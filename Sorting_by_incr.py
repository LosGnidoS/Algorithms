#!/usr/bin/python3
#Created by KIRILL SHVEDOV

'''
SIMPLE ALGORITHM:
SORTING BY INCREASING
1.FIND THE SMALLEST ELEMENT
2.SORT THE ARRAY BY INCREASING
'''


def findSmallest(arr):
	smallest_index = 0
	smallest  = arr[0]

	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index



def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

list_arr = [4,7,6,9,10,15,1,8]
print(selectionSort(list_arr))

