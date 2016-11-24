import requests
import json
import calendar
from datetime import datetime
day = datetime.now()
response = requests.get('https://api.meetup.com/2/open_events.xml?zip=60290&format=json&text=python+hackathon+javascript&time=,1w&key=c3c5c5a3b2d537537d1553375c447')
parsed_string = json.loads(response.text)
with open("Output.html", "w") as text_file:
	for x in parsed_string['results']:		
		tempday = datetime.fromtimestamp(x['time']/1000)
		if day.weekday()!=tempday.weekday():
			day=tempday
			print('<h1>',calendar.day_name[day.weekday()],'</h1>',file=text_file)			
		print('<h1>','<br>',x['name'],'</h1>','<br>', 'TIME ', tempday, '<br>', x['venue']['city'],x['venue']['address_1'],'<br>', x['description'], '<br>','<br>',file=text_file)