import random

def findElem(arr,target):
	for i in range(len(arr)):
		if arr[i] == target:
			return i
	return None


def findMinimal(arr):
	smallest = arr[0]
	for i in range(len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
	return smallest


def findMaximum(arr):
	biggest = arr[0]
	for i in range(0,len(arr)-1):
		if arr[i] > biggest:
			biggest = arr[i]
	return biggest



def findMedian(arr):
	for i in range(len(arr)):
		num_smaller = 0
		num_bigger = 0
		for j in range(len(arr)):
			if arr[j] < arr[i]:
				num_smaller += 1
			if arr[j] > arr[i]:
				num_bigger += 1
		if num_smaller == num_bigger:
			return arr[i]

array = [random.randint(1,10) for i in range((10))]
