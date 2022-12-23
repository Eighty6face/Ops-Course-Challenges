#!/usr/bin/env python3

# Script:                        Ops 301 Challenge 10
# Author:                        Alex Wise
# Date of latest revision:       12/23/2022
# Purpose:                       File creation and alterations 

    # Objectives
        #Using file handling commands, create a Python script that creates a new .txt file, 
        # appends three lines, prints to the screen the first line, then deletes the .txt file.

    # Cites
        # Class Demo



        # Main
    
import os

    # Create new .txt file
f = open("TodaysChallenge.txt", "a")

    # Appends three lines
line1 = "Coding\n"
line2 = "drives me\n"
line3 = "CRAZY"

f.write(line1)
f.write(line2)
f.write(line3)

    # Remember to close the file otherwise you will get an error 

    # Print the first line of the .txt file 
f = open("TodaysChallenge.txt", "r")

print(f.readline())

    # Delete the .txt. file 
os.remove("TodaysChallenge.txt")

