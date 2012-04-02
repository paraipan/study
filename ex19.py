
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"

def bottles_and_glasses(bottles_count, glasses_count):
    print "Then we need %d bottles." % bottles_count
    print "And 4 times more than %d glasses." %glasses_count
    print "Then we can really party !"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)
bottles_and_glasses(4, 5)

print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
amount_of_bottles = 5
amount_of_glasses = 10

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
bottles_and_glasses(amount_of_bottles, amount_of_glasses)


print "We can even math inside too:"
cheese_and_crackers(10+20, 5+6)
bottles_and_glasses(2+5, 3+7)

print "We can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
bottles_and_glasses(amount_of_bottles + 2, amount_of_glasses + 7)
