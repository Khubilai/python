#!/usr/bin/env python
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
mylist = []
for i in range(1,10):
	x = i % 3
	if x == 0:
		mylist.append(i)
	y = i % 5
	if y == 0:
		mylist.append(i)
z = sum(mylist)
print(z)

# Find the sum of all the multiples of 3 or 5 below 1000
