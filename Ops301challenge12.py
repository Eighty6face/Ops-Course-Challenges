#!/usr/bin/env python3

# Script:                        Ops 301 Challenge 12
# Author:                        Alex Wise
# Date of latest revision:       12/28/2022
# Purpose:                       request libraries 

    # Objectives
        # Create a Python script that performs the following:
           #  Prompt the user to type a string input as the variable for your destination URL
            # rompt the user to select a HTTP Method of the following options
                # Get
                # Post
                # Put
                # Delete
                # Head
                # Patch
                # Options
        
        # Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
        # or the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
        # or the given URL, print response header information to the screen.

    # main

import requests

target = "http://info.cern.ch"

# Http Menu

print("choose Http Mmthod:")
print("1. Get\n2. Post\n3. Put\n4. Delete\n5. Head\n6. Patch\n7. Options:")

http_choice = input()

if http_choice == 1:
    response = requests.get(target)
elif http_choice == 2:
    response = requests.post(target)
elif http_choice == 3:
    response = requests.put(target)
elif http_choice == 4:
    response = requests.delete(target)
elif http_choice == 5:
    response = requests.head(target)
elif http_choice == 6:
    response = requests.patch(target)
elif http_choice == 7:
    response = requests.options(target)    
else  print("Please make another selection")
    return None

if



Its Late and I will continue this tomorrow 

# ENd
