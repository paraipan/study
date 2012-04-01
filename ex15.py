
# Import argv module from sys
from sys import argv

# Define what the arguments should be
script, filename = argv

# Open the specified filename
txt = open(filename)

# Print the filename
print "Here's your file %r:" % filename
# Print the file
print txt.read()
print txt.close()

# Ask for the filename again with prompt
print "Type the filename again:"
file_again = raw_input("> ")

# Open the file again
txt_again = open(file_again)

# Print the file
print txt_again.read()
print txt_again.close()