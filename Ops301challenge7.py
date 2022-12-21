#!/usr/bin/env python3

# Script:                       Ops 301 Challenge 7 (python)
# Author:                       Alex Wise
# Date of last revision:        12/20/2022
# Purpose:                      Directories 

# Script must ask the user for a file path and read a user input string into a variable.
# Script must use the os.walk() function from the os library.
# Script must enclose the os.walk() function within a python function that hands it the user input file path.

# Import libraries

import os

# Declaration of variables

root = "root"
dirs = "dirs"
files = "files"


    ### Read user input here into a variable
dir = input(" Enter a directory name: ")

    # Declaration of functions
def os_walk_target(target_arg):

    ### Declare a function here

    for (root, dirs, files) in os.walk(target_arg):

     ### Add a print command here to print ==root==
        # print(" + root + ")---didnt work
        print(root)

    ### Add a print command here to print ==dirs==
        # print(" + dirs + ")---didnt work
        # val = input("dirs")--- didnt work
        print(dirs)

    ### Add a print command here to print ==files==
        #print(" + files + ")---didnt work
        # val = input("files")--- didnt work
        print(files)

    # dir_func(root)---unneeded 
    # dir_func(dirs)----unneeded
    # dir_func(files)----unneeded
os_walk_target(dirs) 

# Main

### Pass the variable into the function here

# End