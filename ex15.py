print "Input your file name."

filename = raw_input(">")

txt = open(filename)

print "Here is your file %r" % filename

print txt.read()

