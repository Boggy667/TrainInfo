import time
import requests

hour = time.strftime("%H")
dayOfWeek = time.strftime("%w")

#QUERY RTT
##London
rttLondon = requests.request('GET','https://api.rtt.io/api/v1/json/search/BCE/to/WAT', auth=('user', 'password'))

##Country
rttCountry = requests.request('GET','https://api.rtt.io/api/v1/json/search/WAT/to/BCE', auth=('user', 'password'))

#PARSE LONDON DATA


#PARSE COUNTRY DATA



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
