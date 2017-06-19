#!/bin/bash

var1="teste"
var2="fsdf"

cat > file1 << EOF1
do some commands on "$var1" 
and/or "$var2"
EOF1

cat > file2 << "EOF2"
do some commands on "$var1" 
and/or "$var2"
EOF2