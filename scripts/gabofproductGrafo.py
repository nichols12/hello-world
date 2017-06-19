#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unicodedata import normalize
import threading
import sys
import os

arq = open(sys.argv[1],'r')
comparativo = arq.readlines()
arqnovo = open(sys.argv[2],'w')
log = open("casamento.txt",'w')
line = []
novoArqu = []
sair = 1
contthread = 0
familia = []
textlog = ''
scoreA = 0
scoreB = 0
scoreC = 0
scoreD = 0
sitFamilia = "desatualizada"

def threadinOrganizaFamilia():
	x = 0
	flag = 0
	global sitFamilia
	while len(familia) > x :
		n = x + 1
		while n < len(familia):
			if familia[x][0] == familia[n][0]:
				for z in familia[x][1:]:
					for a in familia[n][1:]:
						if z == a:
							print(familia)
							if not familia[x] == familia[n]:
								for pessoa in familia[n][1:]:
									if not pessoa in familia[x]:
										familia[x].append(pessoa)
								del familia[n]
								flag = 1
								break
			n = n + 1					
			if flag == 1:
				break
		x = x + 1
	sitFamilia = "atualizada" 	

def escreveLog():
	global textlog
	count = 0
	for x in familia:
		textlog = textlog + "\n *************** familia " + str(count) + "***********\n"
		for y in x:
			print(y)
			textlog = textlog + y +"\n"
		count = count + 1
		
def threading_countingScore():
	global scoreA
	global scoreB
	global scoreC
	global scoreD
	for x in line:
		if x[2].replace("\"",'') == 'A':
			scoreA = scoreA + 1
		elif x[2].replace("\"",'') == 'B':
			scoreB = scoreB + 1
		elif x[2].replace("\"",'') == 'C':
			scoreC = scoreC + 1
		elif x[2].replace("\"",'') == 'D':
			scoreD = scoreD + 1
def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')

def adicionaFamiliar(familiarA,familiarB,sit):
	x = 0
	pessEnc = 1
	famEnc = 1
	while x < len(familia):
		if familia[x][0] == sit:
			for pessoaA in familia[x]:
				if familiarA == pessoaA :
					for pessoaB in familia[x]:
						if pessoaB == familiarB:
							pessEnc = 0
							break
					if pessEnc == 1:
						familia[x].append(familiarB)
						famEnc = 0
						break
				if familiarB == pessoaA :
					for pessoaB in familia[x]:
						if pessoaB == familiarA:
							pessEnc = 0
							break
					if pessEnc == 1:
						familia[x].append(familiarA)
						famEnc = 0
						break
		x = x + 1
	if famEnc == 1:
		novafamilia = [sit,familiarA,familiarB] 
		familia.append(novafamilia)

def threading_atuFamili(n):
	count = 0
	while count < len(familia):
		for pessoaA in familia[count][1:]:
			for pessoaB in familia[count][1:]:
				threadingList(pessoaA, pessoaB,n, familia[count][0],1000)
		count = count + 1
	
def threadingList(x,y,n,sit,fim):
	n = n + 1
	fim = n + fim
	while n < len(line) and n < fim:
		if x == y and remover_acentos(x.upper().replace(" ",'')) == remover_acentos(line[n][2].upper().replace(" ",'')) and remover_acentos(y.upper().replace(" ",'')) == remover_acentos(line[n][5].upper().replace(" ",'')):
			novoArqu.append(line[n][0]+'\t'+line[n][1]+'\t'+line[n][2]+'\t'+line[n][3]+'\t'+line[n][4]+'\t'+line[n][5]+'\t'+line[n][6]+'\t'+line[n][7]+'\t'+line[n][8].replace("\n","")+"\t"+"1"+"\trobo\n")	
			del line[n]
			n = n + 1
		elif remover_acentos(x.upper().replace(" ",'')) == remover_acentos(line[n][2].upper().replace(" ",'')) and remover_acentos(y.upper().replace(" ",'')) == remover_acentos(line[n][5].upper().replace(" ",'')):
			novoArqu.append(line[n][0]+'\t'+line[n][1]+'\t'+line[n][2]+'\t'+line[n][3]+'\t'+line[n][4]+'\t'+line[n][5]+'\t'+line[n][6]+'\t'+line[n][7]+'\t'+line[n][8].replace("\n","")+"\t"+sit+"\trobo\n")	
			del line[n]
			n = n + 1 
		elif remover_acentos(y.upper().replace(" ",'')) == remover_acentos(line[n][2].upper().replace(" ",'')) and remover_acentos(x.upper().replace(" ",'')) == remover_acentos(line[n][5].upper().replace(" ",'')):
			novoArqu.append(line[n][0]+'\t'+line[n][1]+'\t'+line[n][2]+'\t'+line[n][3]+'\t'+line[n][4]+'\t'+line[n][5]+'\t'+line[n][6]+'\t'+line[n][7]+'\t'+line[n][8].replace("\n","")+"\t"+sit+"\trobo\n")	
			del line[n]
			n = n + 1
		else :
			n = n + 1

def printCabecalho(x):
	os.system('cls' if os.name == 'nt' else 'clear')
	print("\n")
	print("\tTotais\t A: %d\tB: %d\tC: %d\tD: %d\t sitFamilia :%s"%(scoreA,scoreB,scoreC,scoreD,sitFamilia))
	print("\tapoios : %d \tTotal da Lista : %d \t\tTotal verificado %d " % (threading.active_count(),len(line),len(novoArqu)))
	#print("Total da Lista :%d" % len(line))
	print("\n")
	print("\titem n :"+str(x))
	print("\t%s \n" % line[x][3])
	print("\t%s \n" % line[x][6])
	print("\tclissificação\tA\t\tB")
	print('\t\t\t'+line[x][2])

def geraTthread(sit,x):
	if sit == "s" :
		novoArqu.append(line[x][0]+'\t'+line[x][1]+'\t'+line[x][2]+'\t'+line[x][3]+'\t'+line[x][4]+'\t'+line[x][5]+'\t'+line[x][6]+'\t'+line[x][7]+'\t'+line[x][8].replace("\n","")+"\t1\n")
		adicionaFamiliar(line[x][2], line[x][5], sit)
		if(threading.active_count() < 8):
			threading.Thread(target=threading_atuFamili,args=(x,)).start()
		sitFamilia = "desatualizada"
		threading.Thread(target=threadinOrganizaFamilia).start()
		threading.Thread(target=threadingList,args=(line[x][3],line[x][6],x,sit,10000,)).start()

		# t.start()
	elif sit == "n" :
		novoArqu.append(line[x][0]+'\t'+line[x][1]+'\t'+line[x][2]+'\t'+line[x][3]+'\t'+line[x][4]+'\t'+line[x][5]+'\t'+line[x][6]+'\t'+line[x][7]+'\t'+line[x][8].replace("\n","")+'\t0\n')
		adicionaFamiliar(line[x][3], line[x][6], sit)
		if(threading.active_count() < 8):
			threading.Thread(target=threading_atuFamili,args=(x,)).start()
		sitFamilia = "desatualizada"
		threading.Thread(target=threadinOrganizaFamilia).start()
		threading.Thread(target=threadingList,args=(line[x][3],line[x][6],x,sit,10000,)).start()

for lineComp in comparativo:
	line.append(lineComp.split('\t'))

threading.Thread(target=threading_countingScore).start()
if(len(sys.argv) >= 4):
	x = int(sys.argv[3])
else:
	x = 1
if(len(sys.argv) >= 5):
	score = sys.argv[4].upper()
else:
	score = ''
while sair and x < len(line):

	if(score == ''):
		if remover_acentos(line[x][3].upper().replace(" ",'')) == remover_acentos(line[x][6].upper().replace(" ",'')):
			novoArqu.append(line[x][0]+'\t'+line[x][1]+'\t'+line[x][2]+'\t'+line[x][3]+'\t'+line[x][4]+'\t'+line[x][5]+'\t'+line[x][6]+'\t'+line[x][7]+'\t'+line[x][8].replace("\n","")+"\t1\n")
			x = x + 1
		else:

			printCabecalho(x)
			gab = input('\tDigite S para sim e N para não e 0 para sair: ')
			if gab == 's' or gab == 'n':
				geraTthread(gab, x)
				x = x + 1
			if gab == "0" :
				sair = 0
	elif(score == line[x][6].replace("\"",'')):
		if remover_acentos(line[x][2].upper().replace(" ",'')) == remover_acentos(line[x][5].upper().replace(" ",'')):
			novoArqu.append(line[x][0]+'\t'+line[x][1]+'\t'+line[x][2]+'\t'+line[x][3]+'\t'+line[x][4]+'\t'+line[x][5]+'\t'+line[x][6]+'\t'+line[x][7]+'\t'+line[x][8].replace("\n","")+"\t1\n")
			x = x + 1
		else:

			printCabecalho(x)
			gab = input('Digite S para sim e N para não e 0 para sair: ')
			if gab == 's' or gab == 'n':
				geraTthread(gab, x)
				x = x + 1
			if gab == "0" :
				sair = 0
	elif('' == line[x][6].replace("\"",'') and score == line[x][7].replace("\"",'')):
		if remover_acentos(line[x][2].upper().replace(" ",'')) == remover_acentos(line[x][5].upper().replace(" ",'')):
			novoArqu.append(line[x][0]+'\t'+line[x][1]+'\t'+line[x][2]+'\t'+line[x][3]+'\t'+line[x][4]+'\t'+line[x][5]+'\t'+line[x][6]+'\t'+line[x][7]+'\t'+line[x][8].replace("\n","")+"\t1\n")
			x = x + 1
		else:

			printCabecalho(x)
			gab = input('Digite S para sim e N para não e 0 para sair: ')
			if gab == 's' or gab == 'n':
				geraTthread(gab, x)
				x = x + 1
			if gab == "0" :
				sair = 0
	elif('' == line[x][7].replace("\"",'') and score == line[x][8].replace("\"",'')):
		if remover_acentos(line[x][2].upper().replace(" ",'')) == remover_acentos(line[x][5].upper().replace(" ",'')):
			novoArqu.append(line[x][0]+'\t'+line[x][1]+'\t'+line[x][2]+'\t'+line[x][3]+'\t'+line[x][4]+'\t'+line[x][5]+'\t'+line[x][6]+'\t'+line[x][7]+'\t'+line[x][8].replace("\n","")+"\t1\n")
			x = x + 1
		else:

			printCabecalho(x)
			gab = input('Digite S para sim e N para não e 0 para sair: ')
			if gab == 's' or gab == 'n':
				geraTthread(gab, x)
				x = x + 1
			if gab == "0" :
				sair = 0
	elif('' == line[x][8].replace("\"",'') and score == line[x][9].replace("\"",'')):
		if remover_acentos(line[x][2].upper().replace(" ",'')) == remover_acentos(line[x][5].upper().replace(" ",'')):
			novoArqu.append(line[x][0]+'\t'+line[x][1]+'\t'+line[x][2]+'\t'+line[x][3]+'\t'+line[x][4]+'\t'+line[x][5]+'\t'+line[x][6]+'\t'+line[x][7]+'\t'+line[x][8].replace("\n","")+"\t1\n")
			x = x + 1
		else:

			printCabecalho(x)
			gab = input('Digite S para sim e N para não e 0 para sair: ')
			if gab == 's' or gab == 'n':
				geraTthread(gab, x)
				x = x + 1
			if gab == "0" :
				sair = 0
	else:
		x = x+1
escreveLog()
log.write(textlog)	
arqnovo.writelines(novoArqu)
arqnovo.close()
log.close()
print("arquivo %s gerado com sucesso" % sys.argv[2])
arq.close()