from sys import argv

script, filename = argv

print "We're going to erase %r. " % filename
print "If you do not want that, hit CTRL-C. "
print "If you want that, hit return. "

raw_input("?")

print "Opening the file..."
target = open(filename,"w")

print "Truncating the file. Goodbye!" 
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1 is:")
line2 = raw_input("Line 2 is:")
line3 = raw_input("Line 3 is:")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

print "Here is the new txt."
target = open(filename)
print target.read()
