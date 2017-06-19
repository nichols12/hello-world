#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unicodedata import normalize
import threading
import sys
import os

arq = open(sys.argv[1],'r')
comparativo = arq.readlines()
arqnovo = open(sys.argv[2],'w')
line = []
novoArqu = []
sair = 1

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')

def threadingList(x,y,n,sit):
	n = n + 1
	while n < len(line):
		if remover_acentos(x.upper().replace(" ",'')) == remover_acentos(line[n][2].upper().replace(" ",'')) and remover_acentos(y.upper().replace(" ",'')) == remover_acentos(line[n][5].upper().replace(" ",'')):
			novoArqu.append(line[n][0]+'\t'+line[n][1]+'\t'+line[n][2]+'\t'+line[n][3]+'\t'+line[n][4]+'\t'+line[n][5]+'\t'+line[n][6]+'\t'+line[n][7]+'\t'+line[n][8]+'\t'+line[n][9]+'\t'+line[n][10].replace("\n","")+"\t"+sit+"\n")	
			del line[n]
			n = n + 1 
		elif remover_acentos(y.upper().replace(" ",'')) == remover_acentos(line[n][2].upper().replace(" ",'')) and remover_acentos(x.upper().replace(" ",'')) == remover_acentos(line[n][5].upper().replace(" ",'')):
			novoArqu.append(line[n][0]+'\t'+line[n][1]+'\t'+line[n][2]+'\t'+line[n][3]+'\t'+line[n][4]+'\t'+line[n][5]+'\t'+line[n][6]+'\t'+line[n][7]+'\t'+line[n][8]+'\t'+line[n][9]+'\t'+line[n][10].replace("\n","")+"\t"+sit+"\n")	
			del line[n]
			n = n + 1
		else :
			 n = n + 1 

def printCabecalho(x):
	os.system('cls' if os.name == 'nt' else 'clear')
	print("Total da Lista :%d" % len(line))
	print("item n :"+str(x))
	print("%s \n" % line[x][2].upper())
	print(line[x][5].upper()+'\n')
	print("clissificação\tA\t\tB")
	print('\t\t'+line[x][6]+','+line[x][7]+','+line[x][8]+line[x][9]+','+line[x][10])

def geraTthread(sit,x):
	if sit == "s" :
		novoArqu.append(line[x][0]+'\t'+line[x][1]+'\t'+line[x][2]+'\t'+line[x][3]+'\t'+line[x][4]+'\t'+line[x][5]+'\t'+line[x][6]+'\t'+line[x][7]+'\t'+line[x][8]+'\t'+line[x][9]+'\t'+line[x][10].replace("\n","")+"\t1\n")
		t = threading.Thread(target=threadingList,args=(line[x][2],line[x][5],x,"1"))
		t.start()
	elif sit == "n" :
		novoArqu.append(line[x][0]+'\t'+line[x][1]+'\t'+line[x][2]+'\t'+line[x][3]+'\t'+line[x][4]+'\t'+line[x][5]+'\t'+line[x][6]+'\t'+line[x][7]+'\t'+line[x][8]+'\t'+line[x][9]+'\t'+line[x][10].replace("\n","")+'\t0\n')
		tn = threading.Thread(target=threadingList,args=(line[x][2],line[x][5],x,"0"))
		tn.start()

for lineComp in comparativo:
	line.append(lineComp.split('\t'))

if(len(sys.argv) >= 4):
	x = int(sys.argv[3])
else:
	x = 1
if(len(sys.argv) >= 5):
	score = sys.argv[4].upper()
else:
	score = ''
while sair and x < len(line):

	# if(score == ''):
	if remover_acentos(line[x][2].upper().replace(" ",'')) == remover_acentos(line[x][5].upper().replace(" ",'')):
		novoArqu.append(line[x][0]+'\t'+line[x][1]+'\t'+line[x][2]+'\t'+line[x][3]+'\t'+line[x][4]+'\t'+line[x][5]+'\t'+line[x][6]+'\t'+line[x][7]+'\t'+line[x][8]+'\t'+line[x][9]+'\t'+line[x][10].replace("\n","")+"\t1\n")
		x = x + 1
	else:
		printCabecalho(x)
		print(score)
		gab = input('Digite S para sim e N para não e 0 para sair: ')
		geraTthread(gab, x)
		x = x + 1
		if gab == "0" :
			sair = 0
	# elif(score == line[x][6] or score == line[x][7] or score == line[x][8] or score == line[x][9] or score == line[x][10]):
	# 	if remover_acentos(line[x][2].upper()) == remover_acentos(line[x][5].upper()):
	# 		novoArqu.append(line[x][0]+'\t'+line[x][1]+'\t'+line[x][2]+'\t'+line[x][3]+'\t'+line[x][4]+'\t'+line[x][5]+'\t'+line[x][6]+'\t'+line[x][7]+'\t'+line[x][8]+'\t'+line[x][9]+'\t'+line[x][10].replace("\n","")+"\t1\n")
	# 		x = x + 1
	# 	else:
	# 		printCabecalho(x)
	# 		print(score)
	# 		gab = input('Digite S para sim e N para não e 0 para sair: ')
	# 		geraTthread(gab, x)
	# 		x = x + 1
	# 		if gab == "0" :
	# 			sair = 0
	
arqnovo.writelines(novoArqu)
arqnovo.close()
print("arquivo %s gerado com sucesso" % sys.argv[2])
arq.close()