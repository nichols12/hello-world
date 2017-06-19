#!/usr/bin/env python 
# -*- coding: utf-8 -*-
arq1 = open('/home/nicholas/Documents/Precifica/gabaritos/LojaALojaBLiquidificador4.csv','r')
arq2 = open('/home/nicholas/Documents/Precifica/gabaritos/LojaALojaBLiquidificador4Inverso.csv','r')
arq3 = open('/home/nicholas/Documents/Precifica/gabaritos/DiferencaNew4.csv','w')
#newText = []
lineA = []
lineB = []
lojaA = arq1.readlines()
lojaB = arq2.readlines()
result = []
count = 1
for listLojaA in lojaA:
	lineA.append(listLojaA.split('\t'))
for listLojaB in lojaB:
	lineB.append(listLojaB.split('\t'))
	#print "teste"
for ListlineA in lineA:
	for ListlineB in lineB:
		#print(ListlineA[1]+"="+ListlineB[1]+";"+ListlineA[4]+"="+ListlineB[4])
		if ListlineA[1] == ListlineB[1] and ListlineA[4] == ListlineB[4]:
			#print("deu certo")
			result.append(ListlineA[1]+'\t'+ListlineA[2]+'\t'+ListlineA[4]+'\t'+ListlineA[5]+'\t'+ListlineA[6]+'\t'+ListlineA[7]+'\t'+ListlineA[8]+'\t'+ListlineA[9]+'\t'+ListlineA[10].replace('\n','')+'\t'+ListlineB[6]+'\t'+ListlineB[7]+'\t'+ListlineB[8]+'\t'+ListlineB[9]+'\t'+ListlineB[10])
			del ListlineB
	count = count + 1		
arq3.writelines(result)
arq3.close()
arq2.close()
arq1.close()		
#print(result[0][0])