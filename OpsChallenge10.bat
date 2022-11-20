:: .bat file 

:: Script:                    Ops Challenge 10
:: Author:                    Alex Wise  
:: Date of latest revision:   18 Nov 22   
:: Purpose:                   PowerShell Script practice 

  


:: Print to the terminal screen all active processes ordered by highest CPU time consumption at the top.
Get-Process | Sort-Object -Property 'CPU' -Descending :: | Select-Object -First 50
:: Print to the terminal screen all active processes ordered by highest Process Identification Number at the top.
Get-Process | Sort-Object Id -Descending | Select-Object -First 50
:: Print to the terminal screen the top five active processes ordered by highest Working Set (WS(K)) at the top.
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 5
:: Start the process Internet Explorer (iexplore.exe) and have it open https://owasp.org/www-project-top-ten/
Start-Process -file iexplore "https://owasp.org/www-project-top-ten/"

:: Start the process Internet Explorer (iexplore.exe) ten times using a for loop. Have each instance open https://owasp.org/www-project-top-ten/.
:: Couldnt get for loop to work and made my PC freeze twice. WIll wait for explanation 


:: Close all Internet Explorer windows
Stop-Process -name iexplore

:: Kill a process by its Process Identification Number. Choose a process whose termination won’t destabilize the system, such as Internet Explorer or MS Edge
Stop-Process -Id 41620
