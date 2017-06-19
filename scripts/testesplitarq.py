#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
param = sys.argv[1:]
print param
arq1 = open(param[0],'r')#arquivo de entrada para teste de diferença
arq2 = open(param[1],'r')#segundo arquivo de entrada para teste de diferença
arq3 = open(param[2],'w')#arquivo de saida
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
print(result[0][0])