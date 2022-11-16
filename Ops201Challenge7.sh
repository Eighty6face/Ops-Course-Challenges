#!/bin/bash

# Script:                       Pipes
# Author:                       Alex Wise
# Date of latest revision:      11/15/2022
# Purpose:                      Practice 

# Things needed to show-CPU, RAM, Dispaly Adapter, Network Adapter
# What is grep- searches the given files for lines containing a match to a given pattern list
# What is lshw- a small tool to display a complete picture of hardware configuration.
# Organized by file and file 2
# Thanks to wifeys mom for the help & google



a="CPU"
echo $a > file.txt
sudo lshw | grep -A 6 "*-cpu" >> file.txt
grep -v "*-cpu" file.txt >> file2.txt

b="RAM"
echo $b >> file.txt
sudo lshw | grep -A 3 "*-memory" >> file.txt 
grep -v "*-memory" file.txt >> file2.txt

c="Display Adapter"
echo $c >> file.txt
sudo lshw | grep -A 5 "*-display" >> file.txt
sudo lshw | grep -B 5 "*-network" >> file.txt

d="Network Adapter"
echo $d >> file.txt
sudo lshw | grep -A 14 "*-network" >> file.txt
grep -v "*-display" file.txt >> file2.txt

sudo lshw | grep -B 1 "*-generic" >> file.txt
grep -v "*-generic" file.txt >> file2.txt
