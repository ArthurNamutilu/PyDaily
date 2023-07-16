#!/usr/bin/python3

montConversions = {
	"Jan": "January",
	"Feb": "February",
	"Mar": "March",
	"Apr": "April",
	"May": "May",
	"Jun": "June",
	"Jul": "July",
	"Aug": "August",
	"Sep": "September",
	"Oct": "October",
	"Nov": "November",
	"Dec": "December",
}

print(montConversions["Dec"])
print(montConversions.get('Feb'))  # get() method
print(montConversions.get("Mon"))
