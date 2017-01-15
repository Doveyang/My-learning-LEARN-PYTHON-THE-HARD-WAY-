from sys import argv

script, name = argv
prompt = ">"

print "Hi %s, I am %s script." % (name, script)
print "I would like to ask you a few questions"
print "Do you like me, %s" % name
likes = raw_input(prompt)
print "%s" % likes