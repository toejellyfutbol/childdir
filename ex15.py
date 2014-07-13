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
close(txt.read)

# print request for input
print "Type the filename again:"
# y = z
file_again = raw_input("> ")

# x = opening(y = z)
txt_again = open(file_again)

#print the context of the file x.  
print txt_again.read()
close(txt_again.read)