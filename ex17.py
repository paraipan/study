
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# how to do it on one line ?
input = open(from_file)
indata = input.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists ? %r" %exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Allright, all done."

output.close()
input.close()

