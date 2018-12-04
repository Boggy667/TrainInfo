import time
import requests
import json

hour = time.strftime("%H")
dayOfWeek = time.strftime("%w")

#QUERY RTT
##London
rttLondon = requests.get('https://api.rtt.io/api/v1/json/search/BCE/to/WAT', auth=('un', 'pw')).json()

##Country
rttCountry = requests.get('https://api.rtt.io/api/v1/json/search/WAT/to/BCE', auth=('un', 'pw')).json()

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
