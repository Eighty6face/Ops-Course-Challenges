#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 31
# Author:                        Alex Wise
# Date of latest revision:       02/27/2023
# Purpose:                       Malware detection pt 1

    # Task
        # Prompt the user to type in a file name to search for
        # prompt the user for a directory to search in
        # search each file in the directory by name
        # for each positive detection print to the screen the file name and location
         # at the end of the search process, print to the screen how many files were searched and how many hits were found
         ### The script must successfully execute on both Ubuntu Linux 20.04 focal fossa and windows 10

        
# Main

import os

# Prompt the user for a file name to search for
file_name = input("Enter the file name to search for: ")

# Prompt the user for a directory to search in
directory = input("Enter the directory to search in: ")

# Initialize counters for files searched and hits found
files_searched = 0
hits_found = 0

# Search each file in the directory by name
for root, dirs, files in os.walk(directory):
    for file in files:
        if file == file_name:
            # For each positive detection print to the screen the file name and location
            hits_found += 1
            print("Found file:", os.path.join(root, file))

        files_searched += 1

# At the end of the search process, print to the screen how many files were searched and how many hits were found
print("Searched", files_searched, "files and found", hits_found, "hits.")


# To run this script on Ubuntu Linux 20.04, open a terminal and navigate to the directory where the script is saved. Then type python3 Ops401challenge31.py to run the script.
# To run this script on Windows 10, open a command prompt and navigate to the directory where the script is saved. Then type python Ops401challenge31.py to run the script.
