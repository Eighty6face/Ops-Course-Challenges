#!/bin/bash

# Script:                            Ops Challenge 301 05
# Author:                            Alex Wise
# Date of latest revision:           12/16/2022
# Purpose:                           Clear Logs

    # Task
        # Print to the screen the file size of the log files before compression
        # Compress the contents of the log files listed below to a backup directory
        # The file name should contain a time stamp with the following format 
        # Clear the contents of the log file
        # Print to screen the file size of the compressed file
        # Compare the size of the compressed files to the size of the original log files

    # Main
# /var/log/syslog
# /var/log/wtmp

# Sets logs as variables
mkdir /var/log/syslog
ls -l sysvar=/var/log/syslog
ls -l wtmpvar=/var/log/wtmp

# Function to print and delete logs
# () means command subsitution (geeksforgeeks) 
deletelog() {              
  cat $1
  cat /dev/null/ > $1
  cat $2
}

rm $sysvar
rm $wtmpvar

# End
