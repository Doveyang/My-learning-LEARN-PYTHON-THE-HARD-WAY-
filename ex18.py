def print_date(number):
	length = len(number)
	if length == 8:
		year = number[0:4]
		month = number[4:6]
		day = number[6:8]
		print("Today is ")
		print("%s.%s.%s") % (year, month, day)
	else:
		print "It's not a valid number"
print_date(raw_input("Put a number...\n>"))