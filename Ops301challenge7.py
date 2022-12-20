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
dir_func = input("Enter a directory name:")

# Declaration of functions
def dir_func(print):

### Declare a function here

    for (root, dirs, files) in os.walk("dir_func"):

     ### Add a print command here to print ==root==
        # print(" + root + ")---didnt work
        val = input("root")
        print("root")

    ### Add a print command here to print ==dirs==
        # print(" + dirs + ")---didnt work
        val = input("dirs")
        print("dirs")

    ### Add a print command here to print ==files==
        #print(" + files + ")---didnt work
        val = input("files")
        print("files")

dir_func(root)
dir_func(dirs)
dir_func(files)

# Main

### Pass the variable into the function here

# End