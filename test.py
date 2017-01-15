print ("Please enter a number.")
number = raw_input(">")
year = number[0:4]
month = number[4:6]
day = number[6:8]
print("今天是：")
print("%s年%s月%s日") % (year, month, day)