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
 # rm = remove file 
 # ls -lH 
 # tilde = ~
 # tar cfz- Comepresses big file 

 target1=syslog
 target2=wtmp

 backup_folder=~/backups


clear_log () {
    target_size$(stat -c%s /var/log/$1)

# print size before compression
    echo "the size of $s1 is $target_size"

 #  compress the contents of the log files to a backup directory
    back_name=$1.$(date +%F%H%M%S).zip
    zip $backup_folder/$back_name /var/log/$1
    target_size_compressed=$(stat -c%s $backup_folder/$backup_name)

# clear the log file
# cat /dev/null > /var/log/$1
# target_size_afterclearing+$ (stat  ~c%s /var/log/$1)
    echo "Size of original log: $target_size"
    echo "Size of compressed log: $target_size_compressed"
# echo "Size of cleared"
}

clear_log $target1
clear_log $target2301



# End
