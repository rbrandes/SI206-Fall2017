import re

f = open('mbox-short.txt','r')
f = f.readlines()

for line in f:
	if re.search("From", line):
		print (line)
		numbers= re.findall("[0-9]+",line)
		print (numbers)
		names= re.findall("(\S+)@", line)[0]
		print (names)