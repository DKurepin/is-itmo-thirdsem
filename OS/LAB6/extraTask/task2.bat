hostname
cd C:\
mkdir test
net share temp=C:\test /grant:"Все",FULL
echo robocopy /z C:\Windows\ \\%computername%\temp explorer.exe > copy.cmd
schtasks /create /tn copy /sc MINUTE /tr C:\copy.cmd
schtasks /query | find "copy"
schtasks /delete /tn copy
taskkill /f /im "robocopy.exe"

fc C:\Windows\explorer.exe \\%computername%\temp\explorer.exe

robocopy /z C:\Windows\ \\%computername%\temp explorer.exe