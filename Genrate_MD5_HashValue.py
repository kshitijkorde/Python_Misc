#!/usr/bin/python 
import hashlib

md5strhex = hashlib.md5("python").hexdigest()
print md5strhex
md5str = hashlib.md5("python").digest()
print md5str
