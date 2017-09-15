#!/usr/bin/python
import commands

cmdLongList = "/bin/ls -l"
outlist = commands.getoutput(cmdLongList).split('\n')
for element in outlist:
	print element.strip()

cmdId = "/usr/bin/id"
outId = commands.getstatusoutput(cmdId)
print "Status:"+str(outId[0])
print "Output:"+outId[1]
