:: .Ps1 File 

:: Script:                    Ops Challenge 11
:: Author:                    Alex Wise  
:: Date of latest revision:   21 Nov 22   
:: Purpose:                   PowerShell Script practice 

  
:: Sourced from "https://github.com/superswan/Powershell-SysAdmin"


:: Enable File and Printer Sharing
	Set-NetFirewallRule -DisplayGroup "File And Printer Sharing" -Enabled True
:: Allow ICMP traffic	
	netsh advfirewall firewall add rule name="Allow incoming ping requests IPv4" dir=in action=allow protocol=icmpv4
:: Enable Remote management
	reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
:: Remove bloatware
	iex ((New-Object System.Net.WebClient).DownloadString(Set'https://git.io/debloat'))
:: Enable Hyper-V
	Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
:: Disable SMBv1, an insecure protocol0
	Set-SmbServerConfiguration -EnableSMB1netEnablesetProtocol $false -Force
