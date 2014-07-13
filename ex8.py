
#denotes variable formatter as %r %r %r %r
formatter = "%r %r %r %r"
#print 1234 in format
print formatter % (1, 2, 3, 4)
#print 'one' 'two 'three' 'four' in format
print formatter % ("one", "two", "three", "four")
#print in format
print formatter % (True, False, False, True)
#print the variable formatter in format 4 times
print formatter % (formatter, formatter, formatter, formatter)
# print in format
print formatter % (
	"I had this thing.", 
	"That you could type up right.", 
	"But it didn't sing.",
	"So I said goodnight."
	)