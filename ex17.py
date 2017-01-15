from sys import argv
from os.path import exists
script, from_file, to_file = argv
print("Copying from %s to %s...") % (from_file, to_file)
in_file = open(from_file)
indata = in_file.read()
print("The input file is %s bytes long.") % len(indata)
print("Does the output file exist?\n%s") % exists(to_file)
print("Ready, hit return to continue.")
raw_input("Hit return to continue")
out_file = open(to_file, 'w')
out_file.write(indata)
print("Done!")
out_file.close()
in_file.close()

print("Here is the new txt.")
txt = open(to_file)
print txt.read()
txt.close()