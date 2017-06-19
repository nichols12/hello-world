#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from unicodedata import normalize
import threading
import sys
import os

arc = open(sys.argv[1],'r')
newcsv = open(sys.argv[2],'w')
line = []
newarq = []
lines = []
flag = True
flag2 = True
for lineComp in arc:
	line.append(lineComp.split("\t"))
x = 0
while x < len(line):
	flag2 = True
	if flag:
		print('entrei no flag1')
		newarq.append(line[x])
		flag = False
	else:
		for comp in newarq:
			if comp[2].replace('\n','') == line[x][2].replace('\n',''):
				flag2 = False
				#del line[x]
				break
	if flag2:
		newarq.append(line[x])
		#del line[x]
	print("posição atual :%d \ttotal da lista:%d"%(x,len(line)))
	x = x + 1

for x in newarq:
	if '\n' in x[2]:
		print('entrei')
		lines.append("%s\t%s\t%s"%(x[0],x[1],x[2]))
	else:
		lines.append("%s\t%s\t%s\n"%(x[0],x[1],x[2]))
newcsv.writelines(lines)
newcsv.close()
arc.close()