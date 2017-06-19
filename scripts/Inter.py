#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import sys
def creatWriter(listx, listy):
	writer = []
	flag = True
	for x in listx :
		for y in listy :
			if x == y :
				flag = False
				break
		if flag:
			writer.append(x)
		flag = True
	return writer

reader = []
reader2 = []
writer1 = []
writer2 = []
writer3 = []
csvfile = open(sys.argv[1],'r')
reader = csv.reader(csvfile,delimiter='\t')
datacsv = list(reader)
csvfile2 = open(sys.argv[2],'r')
reader2 = csv.reader(csvfile2,delimiter='\t')
datacsv2 = list(reader2)
writer1 = creatWriter(datacsv, datacsv2)
writer2 = creatWriter(datacsv2, datacsv)
print(writer1[0][10])
writecsv = csv.writer(open(sys.argv[3],'w'),delimiter = '\t')
writecsv2 = csv.writer(open("reverse" + sys.argv[3],'w'),delimiter = '\t')
writecsv3 = csv.writer(open("Dif" + sys.argv[3],'w'),delimiter = '\t')
cont = 0
for x in writer1:
	for y in writer2:
		if x[1] == y[1] and x[4] == y[4]:
			writer3.append(list([x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],y[6],y[7],y[8],y[9],y[10]]))
			# print(','.join(writer3))
			# input()
			break
		
writecsv.writerows(writer1)
writecsv2.writerows(writer2)
writecsv3.writerows(writer3)

csvfile.close()
csvfile2.close()
#writecsv.close()
#writecsv2.close()
