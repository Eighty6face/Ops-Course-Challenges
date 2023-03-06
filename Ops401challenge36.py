#!/usr/bin/env python3


# Script:                        Ops 401 Challenge 36
# Author:                        Alex Wise
# Date of latest revision:       03/01/2023
# Purpose:                      Socket scanning pt 1

    # task
        # Prompts the user to type a URL or IP address
        # Prompts the users to type a port number
        # Performs a banner grabbing using netcat against a target address as the target port 
            # prints the results to the screen and then moves on to the steps below
        # performs banner grabbing using telnet against the target address at the target port 
            # prints the result to the screen and then moves on to the step below
        # performs banner grabbing using Nmap against the target address of all well-known ports 
            # prints the result to the screen 
        # USE AND DEFINE FUNCTION

# Main

import socket

# Function to perform banner grabbing using Netcat
def netcat_banner(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a new TCP socket object
        s.connect((ip, port)) # Connect to the target IP address and port number
        s.settimeout(2) # Set a timeout value for receiving data from the socket
        banner = s.recv(1024) # Receive up to 1024 bytes of data from the socket
        return banner.decode().strip() # Convert the received bytes to a string and strip whitespace characters
    except:
        return "Error occurred while connecting to the target using Netcat"

# Function to perform banner grabbing using Telnet
def telnet_banner(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a new TCP socket object
        s.connect((ip, port)) # Connect to the target IP address and port number
        s.settimeout(2) # Set a timeout value for receiving data from the socket
        banner = s.recv(1024) # Receive up to 1024 bytes of data from the socket
        return banner.decode().strip() # Convert the received bytes to a string and strip whitespace characters
    except:
        return "Error occurred while connecting to the target using Telnet"

# Function to perform banner grabbing using Nmap
def nmap_scan(ip):
    try:
        nmap_result = "" # Initialize an empty string to store the Nmap results
        for port in range(1, 1024): # Loop through all well-known ports
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a new TCP socket object
            s.settimeout(2) # Set a timeout value for connecting to the socket
            result = s.connect_ex((ip, port)) # Check if the target IP address and port number is open
            if result == 0: # If the port is open
                banner = netcat_banner(ip, port) # Perform banner grabbing using Netcat
                nmap_result += f"Port {port}: {banner}\n" # Append the banner to the Nmap results string
        return nmap_result # Return the Nmap results string
    except:
        return "Error occurred while performing Nmap scan"

# Prompt user for port number
port = int(input("Enter the port number: ")) # Get the port number from the user and convert it to an integer

# Prompt user for URL or IP address
target = input("Enter the URL or IP address: ") # Get the target URL or IP address from the user

# Perform banner grabbing using Netcat
nc_banner = netcat_banner(target, port) # Call the netcat_banner function with the target IP address and port number
print("Netcat result:")
print(nc_banner) # Print the Netcat banner to the screen

# Perform banner grabbing using Telnet
telnet_banner = telnet_banner(target, port) # Call the telnet_banner function with the target IP address and port number
print("Telnet result:")
print(telnet_banner) # Print the Telnet banner to the screen

# Perform banner grabbing using Nmap
nmap_result = nmap_scan(target) # Call the nmap_scan function with the target IP address
print("Nmap result:")
print(nmap_result) # Print the Nmap results to the screen



# Test was against port 22 at scanme.nmap.org SUCCESSFUL 
        # Enter the port number: 22
            #Enter the URL or IP address: Scanme.nmap.org
                #Netcat result:
                    #SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
                        #Telnet result:
                            #SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
                                #Nmap result:
                                    #Port 22: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13