---
title: "Helpdesk - Proving Grounds"
excerpt: "A Writeup of the Helpdesk Box from Proving Grounds<br/><img src='/images/Flimsy/initial_cover.png'>"
collection: portfolio
---

Here's another box from [Proving Grounds](https://www.offsec.com/labs/) called Helpdesk. It was recommended as part of TJ Null's OSCP [lab prep list](https://docs.google.com/spreadsheets/u/1/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/htmlview#) which I've been going through as I prepare for my exam. The initial nmap scan revealed these open ports:

135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds  Windows Server (R) 2008 Standard 6001 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
3389/tcp open  ms-wbt-server Microsoft Terminal Service
8080/tcp open  http          Apache Tomcat/Coyote JSP engine 1.1

So I checked out the web page on 8080 while I scanned for directories. 

![Helpdesk Landing Page](/images/Helpdesk/8080login_page.png){: .center-aligned width="800px"}

Right off the bat, we can see we have a service called "ManageEngine Service Desk Plus" with a version of 7.6.0. That should be a big help, especially for a lab described as "Easy" on the Proving Grounds website lol. I searched for some relevant exploits and found a few to try. Exploit-db and searchploit revealed 115 in fact. I noticed one that required authentication, which I obviously didn't have, and moved on to try a few I couldn't get working. Then I checked the directory scans which showed me nothing and continued to move on to other open ports which didn't help either. I got a little stuck for a bit, then decided to check if maybe the default credentials for the service would work. 

![Default Creds](/images/Helpdesk/default_login_help.png){: .center-aligned width="800px"}

Bingo. I mean it is an easy box. I was able to login using the creds, and off we go. 

![Admin Portal](/images/Helpdesk/administrator_login.png){: .center-aligned width="800px"}

I actually looked around for a while before I remember the authenticated exploit from Google, ultmately from [Peter Sufliarsky](https://github.com/PeterSufliarsky/exploits/blob/master/CVE-2014-5301.py). At that point it was just a matter of running the exploit with the default creds.. 

![Exploit Ran](/images/Helpdesk/shell_caught.png){: .center-aligned width="800px"}

Nice we have an nt authority\system shell.

![Proof](/images/Helpdesk/proof.txt.png){: .center-aligned width="800px"}

And there's the proof. It's a quick, simple box, but it's always nice to get some reps in. 
