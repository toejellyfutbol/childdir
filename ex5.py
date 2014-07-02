name = 'Zed A. Shaw'
age = 35 # not a lie
height = round(74 * 0.3048)# inches times multiplier for meters
weight = round(180 * 2.205)# lbs times multiplier for kilos
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %r meters tall." % height
print "He's %r kilos heavy." % weight
print "Actually that's not too heavy."  
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)