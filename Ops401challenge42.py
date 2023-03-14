#!/usr/bin/python3

# Script:                        Ops 401 Challenge 42
# Author:                        Unknown
# Date of latest revision:       03/14/2023
# Purpose:                       Nmap Automation 
# Revised by                     Alex Wise

import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Full TCP port Scan\n""")
print("You have selected option: ", resp)

# Prompt the user to enter a port range for the scan
# and store it in the 'port_range' variable
# port_range = input("Enter port range to scan (e.g. 1-100): ")

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    # Use the '-v -sS' options for the SYN ACK Scan
    scanner.scan(ip_addr, '1-100', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    # Use the '-v -sU' options for the UDP Scan
    scanner.scan(ip_addr, '1-100', '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    # Use the '-v -sT' options for the third scan option
    scanner.scan(ip_addr, '1-100', '-v -sT')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
else:
    print("Please enter a valid option")

    # End 