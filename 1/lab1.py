import requests
import re
i=0
allemails= []
link = ('http://www.rbc.ru')
def rekursia(link,i):
	global allemails
	if i < 2: 

		response = requests.get(link)

		links = re.findall('"(http://www.rbc.*?)"', response.text)

		for link in links:

			print(link)			
		emails = re.findall(r'[\w\.-]+@[\w\.-]+\.[\w\.-]+', response.text) 

		links = set(links)

		i=i+1		
	
		allemails =  allemails + emails
	
		for link in links:

			rekursia(link,i)
	else: return		
rekursia(link, i)				
allemails = set(allemails)
for allemail in allemails:

	print(allemail)
