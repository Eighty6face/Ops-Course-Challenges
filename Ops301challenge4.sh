#!/bin/bash

# Script:                            Ops Challenge 301 04
# Author:                            Alex Wise
# Date of latest revision:           12/15/2022
# Purpose:                           Menu build up

    # task 
        # Create a bash script that launches a menu system with the following options
            # Hello world (prints “Hello world!” to the screen)
            # Ping self (pings this computer’s loopback address)
            # IP info (print the network adapter information for this computer)
            # Exit
    
        # Next, the user input should be requested
        # The program should next use a conditional statement to evaluate the user’s input, then act according to what the user selected.
        # Use a loop to bring up the menu again after the request has been executed.

# main

msg="Please Select from the menu"


echo $msg
  select opt in "Print 'Hello world!'" "Ping Self" "IP Info" "Exit" ; do
        case $opt in
            "Print 'Hello world!'" ) echo "Hello world" && echo -e "\n$again" ;;
            "Ping Self" ) ping 127.0.0.1 -c 3 && echo -e "\n$again" ;;
            "IP Info" ) ip a && echo -e "\n$again" ;;
            "Exit" ) echo "See ya!"; break;;     
        esac    
        REPLY=   
    done

    # end




