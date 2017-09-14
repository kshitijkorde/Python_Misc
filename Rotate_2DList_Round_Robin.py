#!/usr/bin/python
mylist1 = [[1,2,3,4,5],[7,8,9,10,11],['a','b','c','d','e']]

for element in mylist1:
	print element
while 1:
	print " "
	print "Row:"
	row = int(raw_input())
	print "Rotate by:"
	pos = int(raw_input())
	mylist1[row] = mylist1[row][-pos:] + mylist1[row][:-pos] 
	for element in mylist1:
		print element

