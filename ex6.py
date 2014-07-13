#establishing variable x as having 10 types of people
x = "There are %d types of people." %10
# est. binary as binary
binary = "binary"
# est. do_not as don't
do_not = "don't"
# est y as those who know binary and don't.  
y = "Those who know %s and those who %s." % (binary, do_not)

#print there are 10 types of people
print x
#print those who know binary and those who don't
print y

# I said variable x 
print "I said: %r." % x
# I also said y
print "I also said: '%s'." % y

#est hilarious as False
hilarious = False
#est joke_evaluation as Isn't that joke funny?! 
joke_evaluation = "Isn't that joke funny?! %r"

#print variable % variable
print joke_evaluation % hilarious

# est w as...
w = "This is the left side of..."
# est e as...
e = "a string with a right side."

#print w + e
print w + e