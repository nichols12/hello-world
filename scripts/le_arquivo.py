#!/usr/bin/env python 
# -*- coding: utf-8 -*-
arq1 = open('/home/nicholas/Documents/Precifica/gabaritos/Matches/computadormaster_computadormaster_m9_20170407 (copy).csv','r')
arq2 = open('/home/nicholas/Documents/Precifica/gabaritos/Matches/computadores_computadores_m3_20170407Tiago (copy).csv','r')
arq3 = open('/home/nicholas/Documents/Precifica/gabaritos/Matches/LojaALojaB.csv','w')
newText = []
lojaA = arq1.readlines()
lojaB = arq2.readlines()
for linhaLojaA in lojaA :
	print(linhaLojaA)
	for linhaLojaB in lojaB :
		if linhaLojaA == linhaLojaB:

			newText.append(linhaLojaB)
			newText.append('\n')

			pass

		pass
	pass
arq3.write(newText)
arq3.close()
#print(texto[3])
arq1.close()
arq2.close()
