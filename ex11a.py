print "What is your name?",
name = raw_input()
print "What do you want to be when you grow up?",  
career = raw_input()
print "Why do you want to be %s?" % career,
because = raw_input()

print "So your name is %r and you want to be %r because %r?" % (
name, career, because)
