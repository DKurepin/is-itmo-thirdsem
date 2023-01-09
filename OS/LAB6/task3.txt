net start > C:\LAB6\net1.txt
net stop dnscache
timeout /t 5
net start > C:\LAB6\net2.txt
fc C:\LAB6\net1.txt C:\LAB6\net2.txt > net_res.txt
net start dnscache