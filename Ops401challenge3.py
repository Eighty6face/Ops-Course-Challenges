#!/usr/bin/env python3

# Script:                        Ops 401 Challenge 3
# Author:                        Alex Wise
# Date of latest revision:       01/21/2023
# Purpose:                       Uptime Sensor part 2

# Task
    # Ask the user for an email address and password to use for sending notifications.
    # Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
    # Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.

    # Note to self: First portion was too simple, However due to injury Ive been able to take notes and configure and "Complicate"the code
    # "continued" I have used a VM (win10)for the local IPV4 as to hopefully run into issue and take the hardway out instead of 8.8.8.8

    
    # NOTE TO GRADER-----MY VS CODE KEPT GIVING ME ERRNO2 and wouldnt execute the code. as a CITATION i rewatched the class a few times and did my best to plug and play.
    # (Cont-) Once i figure out the issue I will try it but needed to get this turned in.


# Main

    # import libraries
import datetime
import time
import os
import smtplib
from getpass import getpass
        # decouple from class 4 listening to Ben and Kevin speak on it 

from decouple import config

    # Define variables




# Ask for input from the user
def send_email():
        today = datetime.today()
        if current_ping == 0:
                message = "Tony Stark is Oscar Mike", str(today)
        else:
                message = "Tony Stark is Splashed", str(today)
        email.sendmail(username, username, message)

email = smtplib.SMTP('smtp.gmail.com', 465)

email.starttls()
username = config('username', default='')
password = config('password', default='')

email.login(username, password)

message = os.system("ping -c 1 10.0.2.15")

while True:
        last_ping = current_ping    
        current_ping = os.system("ping -c 1 10.0.2.15")
        print("ping -c 1 10.0.2.15")
        time.sleep(2)
        today = datetime.today()
        
        if current_ping == 0:
                print(str(today) + " Network Active to 10.0.2.15")
                #  print("Network Active")
        else:
                print(str(today) + " Network Inactive to 10.0.2.15")

        if current_ping != last_ping:
                send_email()
