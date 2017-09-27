import re

f = open('mbox-short.txt','r')
f = f.readlines()

for line in f:
	if re.search("From", line):
		print (line)
