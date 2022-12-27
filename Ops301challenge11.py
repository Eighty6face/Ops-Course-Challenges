#!/usr/bin/env python3

# Script:                        Ops 301 Challenge 11
# Author:                        Alex Wise
# Date of latest revision:       12/27/2022
# Purpose:                       Libraries 

    # Objectives
        # Install Psutil
        # Create a Python script that fetches this information using Psutil
            # Time spent by normal processes executing in user mode-1
            # Time spent by processes executing in kernel mode-2
            # Time when system was idle-3
            # Time spent by priority processes executing in user mode-4
            # Time spent waiting for I/O to complete.-5
            # Time spent for servicing hardware interrupts-6
            # Time spent for servicing software interrupts-7
            # Time spent by other operating systems running in a virtualized environment-8
            # Time spent running a virtual CPU for guest operating systems under the control of the Linux ker-9

    # Main

import psutil

output = psutil.cpu_times()
print(output)

print("\n1.Time spent in normal user mode:")
print(output.user)

print("\n2.Time spent by processes executing in kernel mode:")
print(output.system)

print('\n3.Time when system was idle:')
print(output.idle)

print("\n4.Time spent by priority processes executing in user mode:")
print(output.nice)

print("\n5.Time spent waiting for I/O to complete:")
print(output.iowait)

print('\n6.Time spent for servicing hardware interrupts:')
print(output.irq)

print("n/7.Time spent for servicing software interrupts:")
print(output.softirq)

print("\n8.Time spent by other operating systems running in a virtualized environment:")
print(output.steal)

print("\n9.Time spent running a virtual CPU for guest operating systems under the control of the Linux ker:")
print(output.guest)

    # Emd
