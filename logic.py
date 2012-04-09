
# Define a function for the while loop and if statement. The while loop holds you at the question until you get it right (answer == correct) and the if statement just tels you've got it right.
def flash_card(question, correct):
    answer = raw_input(question)
    while answer != correct:
        print "Incorrect. Try again"
        answer = raw_input(question)
    if answer == correct:
        print "Correct :)\n"

print "\nQuit anytime pressing CTRL-Z (^Z)"
print "\n\n\tAnswer True or False\n"

# Now the sequence of all the questions. Perhaps it's possible to random rotate it, but I don't know how.

print "NOT\n" # Remove or add '#' in front of all these 'print' commands if you random rotate the sequence.
flash_card(" not False: ", "True")
flash_card(" not True: ", "False")

print "OR\n"
flash_card(" True or False: ", "True")
flash_card(" True or True: ", "True")
flash_card(" False or True: ", "True")
flash_card(" False or False: ", "False")

print "AND\n"
flash_card(" True and False: ", "False")
flash_card(" True and True: ", "True")
flash_card(" False and True: ", "False")
flash_card(" False and False: ", "False")

print "NOT OR\n"
flash_card(" not(True or False): ", "False")
flash_card(" not(True or True): ", "False")
flash_card(" not(False or True): ", "False")
flash_card(" not(False or False): ", "True")

print "NOT AND\n"
flash_card(" not(True and False): ", "True")
flash_card(" not(True and True): ", "False")
flash_card(" not(False and True): ", "True")
flash_card(" not(False and False): ", "True")

print "!=\n"
flash_card(" 1 != 0: ", "True")
flash_card(" 1 != 1: ", "False")
flash_card(" 0 != 1: ", "True")
flash_card(" 0 != 0: ", "False")

print "==\n"
flash_card(" 1 == 0: ", "False")
flash_card(" 1 == 1: ", "True")
flash_card(" 0 == 1: ", "False")
flash_card(" 0 == 0: ", "True")

print "All finished. Congrats."