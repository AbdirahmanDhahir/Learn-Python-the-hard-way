from sys import argv

script, filename = argv

print "We're going to erase %r." % filename # the filename thats going to be erased i mentioned at the start when we about to run the code . e.g. python ex16.py test.txt.
print "If you don't want that, hit CTRL-C (^C)." # asking question to user
print "If you do want that, hit RETURN." # options are avavibale 

raw_input("?") # we input a qestion to the user

print "Opening the file..." # telling user we reading file
target = open(filename, 'w') # the user whant to open so we target.

print "Truncating the file. Goodbye!" # trucating means erasing the file.
target.truncate() # erase the conent on the file

print "Now i'm going to ask you for three lines." # we going to write a new conent on the file

line1 = raw_input("line 1: ") # lines are inputed they will apear as such
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1) # target is waiting for the user to ender data on the program 
target.write("\n") # this name means put space between the lines, new line.
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it." # finally we tell user you want to close. 
target.close() # target(parameter) then the function close. 
