#!/usr/bin/python
mylist = [1,2,3,4,5,6,7,8,9]

# Logic
# mylist[-pos:] will print elements from pos (counting from the end) upto end
# Ex: mylist[-2:] will print [8,9]
# mylist[:-pos] will print elements from pos (counting from the end) upto beg

print mylist
while 1:
	print "Rotate by:"
	pos = int(raw_input())
	mylist = mylist[-pos:] + mylist[:-pos] 
	print mylist


