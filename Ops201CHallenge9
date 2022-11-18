:: Script:                            Batch task Challenge
:: Author:                            Alex Wise
:: Date of latest revision:           11/17/2022
:: Purpose:                           Practice    




:: Output all events from the System event log that occurred in the last 24 hours to a file on your desktop named last_24.txt.
$Begin = Get-Date -Date '11/17/2022 00:00:00'
$End = Get-Date -Date "11/17/2022 '23:59:59'
Get-Eventlog - Logname System- After $Begin -Before $End >C:\Users\admin\Desktop\Last_14.txt
:: Output all “error” type events from the System event log to a file on your desktop named errors.txt.
Get-Eventlog -Logname System - Entrytype Error >C:\Usersadmin\Desltop\eorrors.txt
:: Print to the screen all events with ID of 16 from the System event log.
Get-Eventlog -Logname System - InstanceID 16
:: Print to the screen the most recent 20 entries from the System event log.’
Get-Eventlog -Logname System - Newest 20
:: Print to the screen all sources of the 500 most recent entries in the System event log. Ensure that the full lines are displayed (get rid of the … and show the entire text)
Get-Eventlog -Logname System -Newest 500 | Format Table -wrap 
