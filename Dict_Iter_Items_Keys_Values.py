#!/usr/bin/python
mydict = {'abc': ['abc', 'cab'], 'art': ['tar', 'rat'], 'ads': ['asd'], 'ajr': ['jar', 'raj'], 'adf': ['adf', 'afd'], 'pqr': ['pqr'], '123': ['123', '321', '231', '213'], 'aadffss': ['asdfasf'], 'rst': ['str'], 'def': ['def']}

print "======== Items ========"
for items in mydict.iteritems():
	print items

print "======== Keys ========"
for keys in mydict.iterkeys():
	print keys

print "======== Values ========"
for vals in mydict.itervalues():
	print vals
