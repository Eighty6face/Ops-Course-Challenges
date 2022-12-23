#!/usr/bin/env python3

# Script:                        Ops 301 Challenge 09
# Author:                        Alex Wise
# Date of latest revision:       12/22/2022
# Purpose:                       Python conditions 

    # Objectives
        # Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.
            # Equals: a == b
            # Not Equals: a != b
            # Less than: a < b
            # Less than or equal to: a <= b
            # Greater than: a > b
            # Greater than or equal to: a >= b
    
    # Task
        # Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.
        # Create an if statement that includes both elif and else to execute when both if and elif are not met.

    # Cites 
        # https://github.com/codefellows/seattle-ops-301d7/blob/main/class-10/challenges/DEMO.md
        # Class DEMO

    # Main

    # Variables 
a = 3
b = 4

    # Equals: a == b

print ("\n1.a == b")
if a == b:
    print("yes")
else:
    print ("no")

# Not Equals: a != b

print("\n2.a != b")
if a != b: 
    print("yes")
else:
    print("no")

# Less than: a < b

print("\n3.a < b")
if a < b:
    print("yes")
else:
    print("no")

# Less than or equal to: a <= b

print("\n4.a <= b")
if a <= b:
    print("yes") 
else:
    print("no")

# Greater than: a > b

print("\n5.a > b")
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# Greater than or equal to: a >= b

print("\n6.a >= b")
if a >= b:
    print("yes")
elif a != b:
    print("no")
else:
    ("no clear answer")

# couldnt get the elif with else to work.


#end 