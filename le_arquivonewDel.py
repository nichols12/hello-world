#!/usr/bin/env python 
# -*- coding: utf-8 -*-
arq1 = open('/home/nicholas/Documents/Precifica/Stack/loja-a_loja-b_m29_20170616.csv','r')
arq2 = open('/home/nicholas/Documents/Precifica/loja1-062017_loja2-062017_m16_20170607.gab.csv','r')
arq3 = open('/home/nicholas/Documents/Precifica/gabaritos/GabAeB.csv','w')
newText = []
lojaA = arq1.readlines()
lojaB = arq2.readlines()
lineA = []
lineB = []
count = 1
flag = 1
for linhaLojaA in lojaA :
	#print(linhaLojaA)
	lineA = linhaLojaA.split("\t")
	#print(lineA[1])
	for linhaLojaB in lojaB :
		lineB = linhaLojaB.split("\t")
		#print(lineB[2])
		if lineA[1] == lineB[2] and lineA[4] == lineB[5]:
			print("entrei")
			newText.append(linhaLojaA)
			flag = 0
			#print(flag)
			del linhaLojaB
	print(count)
	count = count + 1

arq3.writelines(newText)
arq3.close()
#print(texto[3])
arq1.close()
arq2.close()
