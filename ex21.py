def date(number = 0):
	length = len(number)
	if length == 8:
		year = number[0:4]
		month = number[4:6]
		day = number[6:8]
		return "%s.%s.%s" % (year, month, day)
	else:		
		return 0
out_date = date(raw_input("Put a number...\n>"))
if out_date == 0:
	print "It's not a valid number"
else:
	print "Today is", 
	print out_date