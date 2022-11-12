#!/bin/bash

# Script:                         Ops Challenge 5
# Author:                         Alex Wise
# Date of latest revision         11-12-2022
# Purpose:                        Loop Practice

# Write a script that displays running processes, asks the user for a PID, then kills the process with that PID.
# Use a loop in your script.



function proCheck()
{
ps aux
}
proCheck

echo "Enter Process Indentication Number (PID) to terminate"
read PID 

echo "$PID will be terminated"
while [ $PID -gt 697 ]
    do
    kill #(ps aux) $PID
    break
done

# ending message ask for process to be killed
# once entered says process number killed
# Success


