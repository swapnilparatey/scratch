# Code to create your 12-week streak date-ranges
import datetime
from datetime import timedelta

# add the starting date
x = datetime.datetime(2022, 5, 15)

# end of the week date
d = datetime.timedelta(days=6)

# start of the new week date
n = datetime.timedelta(days=7)

for i in range(0,12):
	xd = x + d
	print(x.strftime("%d %b"), "-", xd.strftime("%d %b"))
	x = x + n