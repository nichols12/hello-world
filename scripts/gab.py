#!/usr/bin/env python 
# -*- coding: utf-8 -*-
arq = open('/home/nicholas/Documents/Precifica/gabaritos/DiferencaNew4.csv','r')
comparativo = arq.readlines()
arqnovo = open('/home/nicholas/Documents/Precifica/gabaritos/DiferencaGab4.csv','w')
line = []
novoArqu = []
for lineComp in comparativo:
	line.append(lineComp.split('\t'))
sair = 1
x = 0
while sair:
	import os
	os.system('cls' if os.name == 'nt' else 'clear')
	print("item n :"+str(x))
	print(line[x][1]+'\n')
	print(line[x][3]+'\n')
	print("clissificação\tA\t\tB")
	print('\t\t'+line[x][4]+','+line[x][5]+','+line[x][6]+','+line[x][7]+','+line[x][8]+'\t'+line[x][9]+','+line[x][10]+','+line[x][11]+','+line[x][12]+','+line[x][13])
	#print(line[x][9]+','+line[x][10]+','+line[x][11]+','+line[x][12]+','+line[x][13])
	gab = raw_input('Digite S para sim e N para não e 0 para sair: ')
	print(gab)
	if gab == "s" :
		novoArqu.append(line[x][0]+'\t'+line[x][1]+'\t'+line[x][2]+'\t'+line[x][3]+'\t'+line[x][4]+'\t'+line[x][5]+'\t'+line[x][6]+'\t'+line[x][7]+'\t'+line[x][8]+'\t'+line[x][9]+'\t'+line[x][10]+'\t'+line[x][11]+'\t'+line[x][12]+'\t'+line[x][13].replace("\n","")+'\t1\n')
		x = x + 1
		#novoArqu[x][13] = novoArqu[x][13].replace("\n",'')
		#novoArqu[x].append("1\n")
		#print(novoArqu)
	elif gab == "n" :
		novoArqu.append(line[x][0]+'\t'+line[x][1]+'\t'+line[x][2]+'\t'+line[x][3]+'\t'+line[x][4]+'\t'+line[x][5]+'\t'+line[x][6]+'\t'+line[x][7]+'\t'+line[x][8]+'\t'+line[x][9]+'\t'+line[x][10]+'\t'+line[x][11]+'\t'+line[x][12]+'\t'+line[x][13].replace("\n","")+'\t0\n')
		x = x + 1
		#novoArqu[x][13] = novoArqu[x][13].replace("\n",'')
		#novoArqu[x].append("0\n")
		#print(novoArqu)
	elif gab == "0" :
		sair = 0
	#gab =raw_input("f")
	#x = x + 1
arqnovo.writelines(novoArqu)
arqnovo.close()
arq.close()