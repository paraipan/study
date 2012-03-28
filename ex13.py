
from sys import argv

script, x, y, z = argv

print "The script is called:", script
print "Your first variable is:", x
print "Your second variable is:", y
print "Your third variable is:", z

print x,y,z

stuff = raw_input("do you like %s, %s or %s the most ?" %(x,y,z))