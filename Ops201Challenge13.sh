#!/bin/bash

# Script:                    Challenge 13
# Author:                    Alex Wise   
# Date of latest revision:   28 Nov 22   
# Purpose:                   Practice 


  # Create a script that asks a user to type a domain, then displays information about the typed domain. 
        # Operations that must be used include:
        	 # whois
       		 # dig
        	 # host
		 # nslookup
        
# Reference 
	# https://www.howtogeek.com/680086/how-to-use-the-whois-command-on-linux/
	# https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_02.html
	# https://linuxconfig.org/bash-script-while-loop-examples
  
  # Redone after VM and Unbuntu failure - 11/27/2022
	


  

function 1 {
    whois $newfile > domainsearch.txt
}

function 2{
    dig $newfile > domainsearch.txt
}
    
function 3 {
    host $newfile > domainsearch.txt
}

function 4 {
    nslookup $newfile > domainsearch.txt
}

     read -p "Enter domain name to search for (i.e. Google.com):" newfile
   function 1
   function 2
   function 3
   function 4
    read -p "Would you like to create another search? (y/n)" continue_search
    


echo "Complete"
