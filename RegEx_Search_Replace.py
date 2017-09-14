#!/usr/bin/python

# Replace everything inside all the square brackets with _
import re
line = "asdfaf[asdfad]asdfadf[23123]asdfa23424[645235$55]asdfaf"	
print line
line = re.sub(r'\[\w+\]','_', line) # => asdfaf_asdfadf_asdfa23424[645235$55]asdfaf
print line

line = "asdfaf[asdfad]asdfadf[23123]asdfa23424[645235$55]asdfaf"	
print line
line = re.sub(r'\[\S+?\]','_', line) # => asdfaf_asdfadf_asdfa23424_asdfaf (Note: Adding ? makes it non-greedy)
print line

# Output
# asdfaf[asdfad]asdfadf[23123]asdfa23424[645235$55]asdfaf
# asdfaf_asdfadf_asdfa23424_asdfaf
