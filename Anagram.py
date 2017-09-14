#!/usr/bin/python
anagram = {}
with open('abc.txt') as fobj:
	for word in fobj:
		word = word.strip()
		hashkey = "".join(sorted(word))
		if hashkey not in anagram:
			anagram[hashkey] = []
		anagram[hashkey].append(word)

# print anagram
fobj.closed
for val in anagram.itervalues():
	if(len(val) > 1):
		print val

# Contents of abc.txt
# adf
# afd
# asdfasf 
# asd
# abc
# def
# pqr
# str
# cab
# 123
# 321
# 231
# 213
# jar
# tar
# rat
# raj

# Output
# ['abc', 'cab']
# ['tar', 'rat']
# ['jar', 'raj']
# ['adf', 'afd']
# ['123', '321', '231', '213']

