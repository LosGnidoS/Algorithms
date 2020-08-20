#!usr/bin/python3
#created by Kirill Shvedov

'''TASK THAT MAY BE GIVEN
 DURING YOUR JOB INTERVIEW:
 FIND THE NUMBER IN THE ARRAY
  WHICH WAS DELETED
'''

import random


array = []
new_arr = []
def first_array(arr):
	while len(arr)==0:
		for i in range(10):
			x = random.randint(1, 100)
			arr.append(x)
		return arr
	return None


print(first_array(array))

def new_array(arr):
	new_arr = arr.copy()
	num_to_delete = arr.pop(2)
	x = sum(new_arr);y = sum(arr)
	num_deleted = x - y
	return num_deleted

print(new_array(array))








