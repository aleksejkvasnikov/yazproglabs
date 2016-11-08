import re
#считывание файла
with open ("access.log", "r") as myfile:
	data=myfile.read()
ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', data)
nets = dict()
#заполнение подсети
for ip in ips:
	net = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3})\.\d{1,3}', ip)
	if str(net) in nets:
		nets[str(net)].add(ip)
	else:
		nets[str(net)] = set([ip])
#вывод
for k in nets:
	if len(nets[k]) == 1:
		ip = ips.pop()
		print(ip)
	else:
		print("_-=*PODSET*=-_ " + k+".0/24")
		for ip in nets[k]:
			print("\t" + ip )			
