:: .PS1 

:: Script:                    Ops Challenge 12
:: Author:                    Alex Wise  
:: Date of latest revision:   20 Nov 22   
:: Purpose:                   PowerShell Script practice 

  

:: Create a local file called network_report.txt that holds the contents of an ipconfig /all command.
ipconfig /all >network_report.txt
notepad network_report.txt
:: Use Select-String to search network_report.txt and return only the IP version 4 address.
Select-String -Path "network_report.txt" -Pattern "IPv4"
:: Remove the network_report.txt when you are finished searching it
Remove_Item -Path "network_report.txt"
