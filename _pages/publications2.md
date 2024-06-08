# Preliminary Scanning 
## nmap
-   Basic scan - Nmap $IP
	- Checks 1000 most common ports
-   Then more detailed - Nmap -A -p $IP
	- Where the open ports from the previous scan follow the -p flag
	- Ex: -p22,80,445
-   Nmap -p- $IP
	- Checks all ports - run this after getting started on the first scan because it takes a while
-   Nmap -sU $IP
- Nmap Scripting Engine
	- The nmap scripting engine can also be used for more thorough scanning
	- nmap --script=\<script1>\.nse, \<script2>\.nse $IP
		- Find scripts: grep \<search term>\ /usr/share/nmap/scripts/*.nse
		- Help on script: nmap --script-help=\<script.nse>
## nmapautomator
- https://github.com/21y4d/nmapAutomator
- ./nmapAutomator.sh --host 10.1.1.1 --type All (or Network/Port/Script/Full/UDP/Vulns/Recon)
# Web
## Directory Scanning
### Gobuster
- gobuster dir -u http://host -w /usr/share/wordlists/$wordlist.txt
- gobuster dir -u http://hosts -w /wordlists/Discovery/Web-Content/big.txt -t 4 --delay 1s -o results.txt
	- Where the resulting output is called results.txt
- gobuster dir -u https://host -w /wordlists/$wordlist.txt  -x .php, .txt  -t 4
	- Where you are searching for php and txt files
### feroxbuster 
- feroxbuster -u \<url>
- feroxbuster -u \<url> -w \<wordlists>
- feroxbuster -u \<url> -t \<number_of_threads>
- feroxbuster -u \<url> --timeout \<timeout_in_seconds>
- feroxbuster -u \<url> --filter-status 404,403,400 --thorough -r
- feroxbuster -u \<url>:\<alternative port>

## Directory Traversal
On Linux, we can use the /etc/passwd file to test directory traversal vulnerabilities. On Windows, we can use the file C:\Windows\System32\drivers\etc\hosts to test directory traversal vulnerabilities, which is readable by all local users. In Linux systems, a standard vector for directory traversal is to list the users of the system by displaying the contents of /etc/passwd. Check for private keys in their home directory, and use them to access the system via SSH.

## XSS

## SQLi

## LFI

## RFI
- 

  

# SMTP

  

# Windows Foothold
## Enumeration

## Privilege Escalation
  

# Linux Foothold
## Enumeration

## Privilege Escalation

  

# File Sharing

  

# Tool Syntax
## Hydra
- hydra -l \<user> -P /usr/share/wordlists/rockyou.txt -s \<alternate port> ssh://$IP
- hydra -L /usr/share/wordlists/dirb/others/names.txt -p "\<found password>" rdp://$IP
- hydra -l \<user>-P /usr/share/wordlists/rockyou.txt $IP http-post-form " /index.php:fm_usr=user&fm_pwd=\^PASS^:Login failed. Invalid"
- Basic Auth
	- hydra -l admin -P /usr/share/wordlists/rockyou.txt 192.168.206.201 http-get
## Hashcat
- hashcat -m 0 \<hashfile> /usr/share/wordlists/rockyou.txt -r 15222.rule --force --show
- hashcat -m 13400 \<keepass hash> /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/rockyou-30000.rule --force --show
### check hash cat for which mode to use (searching for KeePass in this case)
- hashcat --help | grep -i "KeePass" 
- hashcat -h | grep -i "ssh"
## john the ripper
- ssh2john id_rsa > ssh.hash 
- keepass2john \<database_name>.kdbx > keepass1.hash
