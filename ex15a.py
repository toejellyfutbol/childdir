# import the argument variables
from sys import argv

# designates variables to be unpacked
script, filename = argv

#designates txt as the content of the filename
txt = open(filename)

#print presentation of file's name 
print "Here's your file %r:" % filename
#print content of file
print txt.read()