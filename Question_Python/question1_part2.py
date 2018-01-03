# January 1st 1990 was Monday
# Assuming 1990 and 2000 are both inclusive years
days = 0
count = 0
exceed = 0
for year in range(1990,2001):
	if year % 4 == 0:
		days += 366
	else:
		days += 365

days = days - 3
while exceed < days:
	exceed += 7
	count += 1

print("Number of days between 1st Jan 1990 to 31st Dec 2000: {0}".format(count))