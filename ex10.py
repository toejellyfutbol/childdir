#denotes variable that is tabbed when printed
tabby_cat = "\tI'm tabbed in."
#denotes variable and starts a new line character in the middle of being printed.  
persian_cat = "I'm split\non a line."
#denotes variable with backslashes displayed in the printed string.  
backslash_cat = "I'm \\ a \\ cat."

#Triple quoted tabbed list with 4 lines.  
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

#print variables line by line
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,