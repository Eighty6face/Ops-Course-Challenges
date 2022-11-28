#!/bin/bash

# Script:                    Challenge 13
# Author:                    Alex Wise   
# Date of latest revision:   27 Nov 22   
# Purpose:                   Practice 


  # Create a script that asks a user to type a domain, then displays information about the typed domain. 
    # Operations that must be used include:
        # whois
        # dig
        # host
        # nslookup
        
# Reference sites below:
	# https://www.howtogeek.com/680086/how-to-use-the-whois-command-on-linux/
	# Catherines Mom (MIL) lol

    
continue_search="X"

function f1 {
    whois $newfile > domainsearch.txt
}

function f2 {
    dig $newfile > domainsearch.txt
}
    
function f3 {
    host $newfile > domainsearch.txt
}

function f4 {
    nslookup $newfile > domainsearch.txt
}

while [ $continue_search == "X" ]
do 
    read -p "Enter domain name to search for (i.e. SpeedSociety.com):" newfile
   f1
   f2
   f3
   f4
    read -p "Would you like to create another search? (y/n)" continue_search
    
done

echo "Search Complete"
