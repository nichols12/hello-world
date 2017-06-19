#!/bin/bash
 num=1
 flag=true

produto=$@
touch /home/nicholas/Documents/produtos/teste1/marcaproduto.txt
echo "	">/home/nicholas/Documents/produtos/teste1/marcaproduto.txt
for produtos in $produto
 do
 	
 	flag=true;
 	while read -ra line; 
	do
    	for word in "${line[@]}";
    		do

        	wordClea="${word//[}"
        	#echo $word1;
        	wordClea="${wordClea//]}"
        	#echo $wordClea;
        	if [[ $word == $produtos ]]; then
        		echo "Marca ja cadastrada $produtos";
        		flag=false;
        		#echo "falso"
        		#echo $flag
        		#statements
        	fi
    	done;
	done < /home/nicholas/workspace.odysci_ecommerce/e-commerce-admin/conf/groups-pro/lists/marca/novasmarcas.txt
	echo $flag
	if [[ $flag = true ]]; then
		echo "Marca nova $produtos"
		echo "	"[[$produtos]]>> /home/nicholas/Documents/produtos/teste1/marcaproduto.txt
		echo "	""	"$produtos>> /home/nicholas/Documents/produtos/teste1/marcaproduto.txt
		#statements
	fi
	
	
done

