#!/usr/bin/python 
mydict = {'abc':100, 'q':10000, '1wqe': 20000, 'trt': 30, 'aaa':20000}
print mydict
max_key = max(mydict.iterkeys(), key=(lambda key: mydict[key]))
print max_key

for keys in mydict.itervalues():
	print keys
