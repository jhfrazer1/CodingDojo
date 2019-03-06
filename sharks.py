tanks = 20
space_in_main_tank = 500.0
divers = 5
sharks = 15
tanks_not_filled = tanks - divers
tanks_filled = divers
shark_tank_capacity = sharks_in_main_tank * space_in_main_tank
average_sharks__per_tank = sharks / tanks_filled


print "There are", tanks, "tanks available."
print "There are only", divers, "divers available."
print "There will be", tanks_not_filled, "empty tanks today."
print "We can fill" , shark_tank_capacity, "sharks today."
print "We have", sharks, "to fill today."
print We need to put about", average_sharks_per_tank, "in each tank."