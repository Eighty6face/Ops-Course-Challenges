#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 13
# Author:                        Alex Wise
# Date of latest revision:       02/01/2023
# Purpose:                       Port scanner pt3

 # Task
    # In Python, combine the two modes (port and ping) of your network scanner script.
    # Eliminate the choice of mode selection.
    # Continue to prompt the user for an IP address to target.
    # Move port scan to its own function.
    # Call the port scan function if the host is responsive to ICMP echo requests.
    # Print the output to the screen.



# Main

# Import library
from scapy.all import sr1, IP, TCP, ICMP, srp
import sys
import ipaddress

def port_scan(host, port_range, src_port):
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

# Prompt the user for an IP address to target.
host = input("Enter target host: ")

# Set the target host and port range to scan
port_range = [int(p) for p in input("Enter port range separated by space (e.g. 22 80 443): ").split()]
src_port = 22

# Check if the host is responsive to ICMP echo requests
resp = sr1(IP(dst=host)/ICMP(), timeout=1, verbose=0)
if resp is None:
    print(f"{host} is down or unresponsive")
elif resp.getlayer(ICMP).type == 3 and resp.getlayer(ICMP).code in [1, 2, 3, 9, 10, 13]:
    print(f"{host} is actively blocking ICMP traffic")
else:
    print(f"{host} is responding")

# Call the port scan function
    port_scan(host, port_range, src_port)


# END

# The reduction of the menu from the previous challenge to the indtroduction of both functions bing executed makes sense and stream lines the script and process
# THis tool would be valueable to find potential open ports and vulenrabilities that would otherwise go unoticed

