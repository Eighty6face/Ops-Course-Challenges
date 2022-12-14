#!/bin/bash

# Script:                            Ops Challenge 301 03
# Author:                            Alex Wise
# Date of latest revision:           12/14/2022
# Purpose:                           chmod

# task
    # Prompts user for input directory path.
    # Prompts user for input permissions number 
    # Navigates to the directory input by the user and changes all files inside it to the input setting.
    # Prints to the screen the directory contents and the new permissions settings of everything in the directory

# Cites
    # Replit example
    # Team help
    # Previous Challenges 


# Main

echo "Enter directory path: "
read dirpath
mkdir $dirpath
cd $dirpath

touch testfile.txt
echo "Enter permission number request for file: "
read $perm 
chmod --recursive $perm .
ls -al .

# end 