formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
	"I had  this thing.",
	' ',
	"56",
	""
)