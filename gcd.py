#!usr/bin/python3
#Created by Kirill Shvedov
#GITHUB---->LosGnidoS\

'''THE HIGHEST COMMON FACTOR (HCF)
 , ALSO CALLED GCD, CAN BE COMPUTED
  IN PYTHON USING A SINGLE FUNCTION
   OFFERED BY MATH MODULE AND HENCE
 CAN MAKE TASKS EASIER IN MANY SITUATIONS'''


def gcd(a,b):
	if b == 0:
		return a
	else:
		print(a%b)
		return gcd(b, a%b)


#print(gcd(4851,3003))


def gcd2(a,b):
	while b != 0:
		remainder = a%b
		a = b
		b = remainder
	return a

#print(gcd2(4851,3003))
