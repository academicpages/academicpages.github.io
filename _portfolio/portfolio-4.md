---
title: "Algernon - Proving Grounds"
excerpt: "A Writeup of the Algernon Box from Proving Grounds<br/><img src='/images/Algernon/Logs.png'>"
collection: portfolio
---

Alright, this is a pretty quick writeup of Algernon from [Proving Grounds](https://www.offsec.com/labs/), part of TJ Null's OSCP [lab prep list](https://docs.google.com/spreadsheets/u/1/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/htmlview#). 

Right off the bar we get started with an nmap scan which revealed these ports:

PORT      STATE SERVICE
21/tcp    open  ftp
80/tcp    open  http
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
5040/tcp  open  unknown
9998/tcp  open  distinct32

A little bit of enumeration revealed that the FTP server allowed anonymous login, so I checked that out while I scanned the web page for directories. 

![Algernon FTP](/images/Algernon/ftp_connected.png){: .center-aligned width="800px"}

We search around in the FTP server to reveal a bunch of logs, including a few that say administrative. That could be a clue.

![Algernon Logs](/images/Algernon/Logs.png){: .center-aligned width="800px"}

Unfortunately I didn't really find anything in there, and in fact later realized that new administrative logs continued to be written as I checked out the web page. Port 80 returned the default Microsoft IIS landing page and no interesting sub-directories. So that was a dead end, and I decided to check out port 9998. 

![Algernon SmarterMail](/images/Algernon/SmarterMail.png){: .center-aligned width="800px"}

So that could be something. We can see the software is called SmarterMail, so we'll check the web for any exploits while fuzzing for more sub-directories (which also didn't show anything particularly interesting.) Side note - I also ran a full port scan at this port which returned an unknown open port on 17001, a clue for later. 

![Algernon Exploits](/images/Algernon/smartermail_exploits.png){: .center-aligned width="800px"}

After checking through a few of these exploits, we ultimately settle on the RCE exploit for Build 6985. At that point, I didn't know the build, but it felt worth checking out. As I looked through the exploit I noticed that the ports and addresses are hardcoded and need to be changed to my port and IP, as well as the target point and IP. 

![Algernon Ports and IPs](/images/Algernon/change_this.png){: .center-aligned width="800px"}

And we see 17001 as the target port. I think I might have assumed 9998 because that's where the SmarterMail application was hosted, but it helped to realize that the unknown open port I'd already found was also being used for the exploit. After that we ran the exploit, caught the root shell, and checked for proof.txt. 

![Algernon Root](/images/Algernon/caught_root_shell.png){: .center-aligned width="800px"}

Bingo! Another quick box here, I should probably start writing up some of the more complex ones, but these go nice and quick. 