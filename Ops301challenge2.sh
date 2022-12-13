#!/bin/bash

# Script:                            Ops Challenge 301 02
# Author:                            Alex Wise
# Date of latest revision:           12/13/2022
# Purpose:                           Append date and time 

# Task
    # Copies /var/log/syslog to the current working directory
    # Appends the current date and time to the filename

# Cites
    # https://www.cyberciti.biz/faq/unix-linux-getting-current-date-in-bash-ksh-shell-script/



# Main

day=$(date +%D%T)

cp /var/log/syslog .

mv syslog syslog_$day

# End