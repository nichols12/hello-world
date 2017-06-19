#!/bin/bash
cont=1;
for arq in ls /nfs/project/odysci/customers/precifica/casamentos\ a\ melhorar\ 03.2017/CSVs\ da\ Precifica/05.04.2017/*; do
  iconv -f iso-8859-1 -t utf-8 -o /home/nicholas/Documents/Precifica/Csvutf8/"$cont".csv "$arq"
  echo "$arq"
  cont=$(($cont+1));
done