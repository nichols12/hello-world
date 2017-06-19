#!/usr/bin/env python 
# -*- coding: utf-8 -*-
arq1 = open('/home/nicholas/Documents/scripts/unhas.txt','r')
arq3 = open('/home/nicholas/Documents/testeUnhas.txt','w')
newText = []
lojaA = arq1.readlines()
lineA = []
count = 1
flag = 1
for linhaLojaA in lojaA :
	#print(linhaLojaA)
	newText.append("[["+linhaLojaA.replace("\n","")+"]]\n")
	newText.append("\t"+linhaLojaA)

arq3.writelines(newText)
arq3.close()
#print(texto[3])
arq1.close()
