import time

hour = time.strftime("%H")
dayOfWeek = time.strftime("%w")

#Set Up RTT Connection
#Query In
#Query Out
#Close Connection

#Format In & Out Lists

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
		
#FUTURE
	#Add Graphical Elements and text colours
