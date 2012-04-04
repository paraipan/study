print "Small recap..."

print "Hello World!"

# print "If I add %d, %d, and %d I get %d." % (
# my_age, my_height, my_weight, my_age + my_height + my_weight)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious

months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print months

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print fat_cat

print "How old are you?",
age = raw_input()
print "You have %s years" % age



from sys import argv

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

input = open(from_file)
indata = input.read()


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

age = add(30, 5)

print "You have", age, "years"