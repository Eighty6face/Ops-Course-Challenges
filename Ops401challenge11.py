#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 11
# Author:                        Alex Wise
# Date of latest revision:       01/30/2023
# Purpose:                       

    # Create a TCP port range scanner that tests whether a TCP port is open or closed
        # Define IP host
        # Define port ranges on a specific set of ports to scan
        # Test each port in the specified range using a for loop
        # If flag 0x12 is received, send an rst packet to graciously close the open connection. notify the user the port is open
        # If flag 0x14 is received, notify the user the port is closed
        # If no flag received, notify the user the port is filtered and silently dropped 

# Main

# Import necessary modules from Scapy library
from scapy.all import sr1, IP, TCP
import sys

# Set the target host and port range to scan
host = 'scanme.nmap.org'
port_range = [22, 80, 443, 3389, 143]
src_port = 22

# Iterate over each port in the specified range
for dst_port in port_range:
  # Craft and send a TCP SYN packet to the target host and port
  response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port,flags="S"),timeout=1,verbose=0)

  # Check the response flags to determine if the port is open, closed, or filtered
  if response[TCP].flags == 0x12:
    print("Port %d is open." % dst_port)
    sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags="R"))
  elif response[TCP].flags == 0x14:
    print("Port %d is closed." % dst_port)
  else:
    print("Port %d is filtered." % dst_port)


#  the number of packets sent to port 22 can be limited by modifying the port_range list to exclude port 22 or by adding a condition to skip port 22 in the for loop.