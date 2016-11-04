import re
#считывание файла
with open ("access.log", "r") as myfile:
	data=myfile.read()
ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', data)
#сортировка
ip = sorted(ip, key=lambda x:tuple(map(int, x.split('.'))))
#удаление повторов
cleanlist = []
[cleanlist.append(x) for x in ip if x not in cleanlist]
for i in cleanlist: 
	print(i)


		
		