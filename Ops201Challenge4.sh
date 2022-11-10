# !/bin/bash

# Script:                      Challenge 4   
# Author:                      Alex Wise 
# Date of latest revision:     11-10-2022 
# Purpose:                     Array Practice  

mkdir dir1
mkdir dir2
mkdir dir3
mkdir dir4

my_array=(dir1 dir2 dir3 dir4)

touch ./${my_array[0]}/newfile.txt
touch ./${my_array[1]}/newfile.txt
touch ./${my_array[2]}/newfile.txt
touch ./${my_array[3]}/newfile.txt
