import time

hour = time.strftime("%H")
dayOfWeek = time.strftime("%w")

#query Realtime Trains
#Filter Out 2-3 Relevant Trains & Info
#Build In & Out Lists

if (dayOfWeek == 0 or dayOfWeek == 6):
	print("Weekend")
	#Display in & Out Lists
else:
	if (int(hour) > 12 or hour <= 2):
		#Display Out List
		print("Weekday Country")
	else:
		#Display In List
		print("Weekday London")
