import requests
import re
i=0
allemails= []
link = ('http://mosigra.ru')
def rekursia(link,i):
	global allemails
	if i < 2: ##глубина 3
		#получили страницу
		response = requests.get(link)
		#собрали все ссылки	
		links = re.findall('"(http://www.mosigra.*?)"', response.text)
		## собрали всю почту
		for link in links:
		# выводим почту
			print(link)			
		emails = re.findall(r'[\w\.-]+@[\w\.-]+', response.text) 
		#убрали повторения
		links = set(links)
		#шаг в глубину	
		i=i+1		
		#сохранили			
		allemails =  allemails + emails
		#для каждой почты		
		for link in links:
			# рекурсивный вызов
			rekursia(link,i)
	else: return		
rekursia(link, i)				
allemails = set(allemails)
for allemail in allemails:
	# выводим почту
	print(allemail)

