#!/bin/bash

# Script:                               Challenge 6                      
# Author:                               Alex Wise           
# Date of latest revision:              11-14-22      
# Purpose:                              Practice 


echo "does file.txt exist?"

Xs=("f1.txt" "f2.txt" "f3.txt" "f4.txt" "f5.txt")

for X in "${Xs[@]}"
do
    if [ -e ./$X ]
    then 
        echo yes
    else
        touch ./$X
        echo "No, but $X has now been created"
    fi
done
# create a script that detects a file or directory exsist, then creates it if it does not exsist
# Must use one Array, one loop and one conditional

#Thanks Grant for the help and walk through. SUPER CONFUSING TO ME
