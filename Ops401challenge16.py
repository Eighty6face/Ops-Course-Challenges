#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 16
# Author:                        Alex Wise
# Date of latest revision:       02/06/2023
# Purpose:                       Brute Force Wordlist attack pt1

 # Task
        # Mode 1: Offensive; Dictionary Iterator
            # Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
            # Add a delay between words.
            # Print to the screen the value of the variable.
        
        # Mode 2: Defensive; Password Recognized
            # Accepts a user input string.
            # Accepts a user input word list file path.
            # Search the word list for the user input string.
            # Print to the screen whether the string appeared in the word list.

# Main

# Import the time library to be able to use the sleep function
import os
import time

# Define a function to handle the offensive mode
def offensive_mode(file_path, delay):
  # Open the word list file
  with open(file_path, "r") as f:
    # Read each line of the file
    for line in f:
      # Strip the newline character from each line
      word = line.strip()
      # Assign the word to a variable
      current_word = word
      # Print the value of the variable
      print(current_word)
      # Sleep for the specified delay
      time.sleep(delay)

# Define a function to handle the defensive mode
def defensive_mode(user_input, file_path):
  # Set a flag to keep track of whether the user input was found in the word list
  found = False
  # Open the word list file
  with open(file_path, "r") as f:
    # Read each line of the file
    for line in f:
      # Strip the newline character from each line
      word = line.strip()
      # Check if the user input matches the current word
      if user_input == word:
        # Set the flag to True
        found = True
        break
  # Print whether the user input was found in the word list
  if found:
    print("Password Accepted")
  else:
    print("Wrong Password")

# Ask the user to choose a mode
mode = input("Which mode? (Offensive/Defensive): ")

# Handle the mode selected by the user
if mode.lower() == "offensive":
  # Ask the user for the file path
  file_path = input("Enter the word list file path: ")
  # Ask the user for the delay
  delay = float(input("Enter the delay (in seconds): "))
  # Call the offensive mode function
  offensive_mode(file_path, delay)
elif mode.lower() == "defensive":
  # Ask the user for the user input
  user_input = input("Enter the password: ")
  # Ask the user for the file path
  file_path = input("Enter the word list file path: ")
  # Call the defensive mode function
  defensive_mode(user_input, file_path)
else:
  # If the user selects an invalid mode, display an error message
  print("Invalid mode selected")

# END 