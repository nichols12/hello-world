#!/bin/bash
# Criado por: Raimundo Portela <rai3mb@gmail.com>
# Objetivo: baixar dados sobre os municípios direto do IBGE
#------------------------------------------------------------------------------
function func_download() {
   for UF in ac al am ap ba ce df es go ma mg ms mt pa pb pe pi pr rj rn ro rr rs sc se sp to
   do
      wget http://www.ibge.gov.br/cidadesat/ufs/download/${UF}_mapa_e_municipios.pdf
      pdftotext -layout ${UF}_mapa_e_municipios.pdf 
      egrep '[0-9]$' ${UF}_mapa_e_municipios.txt > "$UF".lista
      #rm ${UF}_mapa_e_municipios.pdf 
      rm ${UF}_mapa_e_municipios.txt
   done
}

function func_getDados() {
   for UF in ac al am ap ba ce df es go ma mg ms mt pa pb pe pi pr rj rn ro rr rs sc se sp to
   do
      > "$UF".sql
      while read LINHA
      do
         DADOS=( $( echo $LINHA | sed 's/  / /g' | sed 's/  / /g' | sed 's/  / /g' | sed 's/  / /g' | sed 's/  / /g' ) )   
         PENULTIMO=$(( ${#DADOS[@]} - 2 ))
         ULTIMO=$(( ${#DADOS[@]} - 1 ))
         AREA=${DADOS[$ULTIMO]}
         POPULACAO=${DADOS[$PENULTIMO]}
         for i in $(seq $(( ${#DADOS[@]} - 3 )) )
         do
            NOME[$i - 1]=${DADOS[$i -1]} 
         done
         #sqlite3 "$HOME"/Desktop/municipios.db "INSERT INTO municipios(uf, nome, populacao, area) VALUES('$UF', '${NOME[@]}', $POPULACAO, $AREA);"
         echo "INSERT INTO municipios(uf, nome, populacao, area) VALUES('$UF', '${NOME[@]}', $POPULACAO, $AREA);" >> "$UF".sql
         unset NOME
         unset DADOS
      done < "$UF".lista
   done
}

# faz o download de dados sobres os estados em PDF e gera um arquivo .lista com CIDADE|POPULACAO|AREA
func_download
# coleta os dados dos arquivos .lista e gera um arquivo .sql para posterior uso em Banco de dados
func_getDados