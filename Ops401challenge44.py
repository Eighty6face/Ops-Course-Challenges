#!/usr/bin/python3

# Script:                        Ops 401 Challenge 44
# Author:                        Unknown
# Date of latest revision:       03/16/2023
# Purpose:                       Create a port scanner 
# Revised by                     Alex Wise

    # Task
        # Complete the demop script to be a functional port scanner 

# Main

import socket

# Create a socket object
sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set a timeout value for socket operations
timeout = 10  # 10 seconds
sockmod.settimeout(timeout)

# Prompt user for host IP address and port number
hostip = input("Enter the host IP: ")
portno = int(input("Enter the port number: "))

# Define a function to scan for open ports
def portScanner(portno):
    # Use connect_ex() to check if the port is open
    if sockmod.connect_ex((hostip, portno)) == 0: 
        print("Port open")
    else:
        print("Port closed")

# Call the portScanner function to check the specified port
portScanner(portno)


# End 