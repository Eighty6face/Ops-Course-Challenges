#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 2
# Author:                        Alex Wise
# Date of latest revision:       01/17/2023
# Purpose:                       Uptime Sensor

# Task
    # Transmit a single ICMP (ping) packet to a specific IP every two seconds.
    # Evaluate the response as either success or failure.
    # Assign success or failure to a status variable.
    # For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.

# Main


import os
import time
import datetime


while True:
    now = datetime.datetime.now()
    response = os.system("ping -c 1 8.8.8.8")
    if response == 0:
        print("Network Active")
    else:
        print("Network Inactive")
    time.sleep(2)
