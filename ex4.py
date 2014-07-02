cars = 100 #number of cars avail
space_in_a_car = 4.0 # max number of people in each car
drivers = 30 # number of drivers available for the day
passengers = 90 # number of passengers available
cars_not_driven = cars - drivers # cars not driven
cars_driven = drivers # number of cars driven can only be the number of drivers
carpool_capacity = cars_driven * space_in_a_car # carpool capacity
average_passengers_per_car = passengers / cars_driven # how many people we need to put in each car today


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."