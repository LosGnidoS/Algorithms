#!/usr/bin/python3
#Created by KIRILL SHVEDOV

'''RECURSION ALGORITHM
(USING SAME FUNCTION 
IN FUNCTION ITSELF)'''



def sum_rec(arr):
	if sum(arr) == 0:
		return 0
	else: 
		return arr.pop(0) + sum_rec(arr) 




list_array = [2,5,6,7,8,4,3,3]
print(sum_rec(list_array))


