#!/usr/bin/env python

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


a, b, c = 0, 1, 0
while a < 4000000:
	if a % 2 == 0:
		c = a + c
	a, b = b, a+b
print(c)
