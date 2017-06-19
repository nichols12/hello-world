#!/usr/bin/env python3
import os
import re
newArq = open('/home/nicholas/Documents/Media analizer/tese.csv','w')
arq = open('/home/nicholas/Documents/Media analizer/samsung_fbcrawl_20170403.csv','r')



TextArq = arq.read()
linesSplit = []
linesSplit = TextArq.split('\t')
cel = ""
last = []
line = []
contx = 0
cont = 0
linesNewArc = []

def topComent(listofComent, idofTopComent):
	if not idofTopComent:
		return "sem comentario"
	for x in listofComent:
		#print(x[2])
		id = re.search(idofTopComent,x[0])
		if id:
			return x[5]
	return "sem comentario"

def geraNewLine(linelist,sentiment):
	linha = ""
	for x in linelist:
		linha = linha + x + '\t'
	print(linha)
	input()
	return linha + sentiment + '\n'

for x in linesSplit :
	#print(x)
	cel = cel + x + "\t"
	#print(x + " item " + str(cont))
	if cont == 31:
		line.append(cel.split("\t"))
		last = re.search("(.*)\n(.*)",line[contx][31])
		if last:
			# print(last.group(0))
			# print(last.group(1))
			# print(last.group(2))
			#testt = input()
			line[contx][31] = last.group(1)
			cel = last.group(2) + "\t"
		#print(line[contx])
		contx = contx + 1
		cont = 1
		#celo = input()

	else :
		cont = cont + 1
	#print(contx)
sair = True
x = 0
while sair:
 	if not line[x]:
 		sair = False
 	else:
 		os.system('cls' if os.name == 'nt' else 'clear')
 		#print(linesSplit[x])
 		print("Nome do Usuário: %s" % line[x][10])
 		id = re.search('162523134477_(\d+)',line[x][2])
 		if id:
 			print("Texto Origem: %s" % topComent(line,id.group(0)))
 		else:	
 			print("Texto Origem: Sem Comentario")
 		print("Texto : %s" % line[x][5])
 		escolha = input("digite \'P\' para Positivo , \'n\' para Negativo , \'i\' para indiferente e \'s\' para sair : ")
 		if escolha == 's':
 			sair = False
 		elif escolha == 'p':
 			linesNewArc.append(geraNewLine(line[x],'P'))
 			x = x + 1
 		elif escolha == 'n':
 			linesNewArc.append(geraNewLine(line[x],'N'))
 			x = x + 1
 		elif escolha == 'i':
 			linesNewArc.append(geraNewLine(line[x],'i'))
 			x = x + 1
newArq.writelines(linesNewArc)
arq.close()
newArq.close()