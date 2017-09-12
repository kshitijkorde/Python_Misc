#!/usr/bin/python
import re
pattern = '\d+-\d+-(\S+)'
prog = re.compile(pattern)
mylist = ['123-12-abc', '1-2-werewr', '002-asdf-aadsf', '123a-1244a-asdf', '12-12-1234avc']
for element in mylist:
	result = prog.match(element)
	if result:
		print "Matched pattern: " + result.group(0)
		print "Name :" + result.group(1)
		
# Output
# Matched pattern: 123-12-abc
# Name :abc
# Matched pattern: 1-2-werewr
# Name :werewr
# Matched pattern: 12-12-1234avc
# Name :1234avc

