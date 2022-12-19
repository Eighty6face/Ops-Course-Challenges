

# Script:                       Ops 301 Challenge 6 (python)
# Author:                       Alex Wise
# Date of last revision:        12/19/2022
# Purpose:                      Specific commands prints

# main

import os

whoami_output = os.system("whoami")
ip_a_output = os.system("ip a")
ishw_output = os.system("ishw -short")

print(whoami_output)
print(ip_a_output)
print(ishw_output)

# end 