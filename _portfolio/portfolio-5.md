---
title: "Astronaut - Proving Grounds"
excerpt: "A Writeup of the Astronaut Box from Proving Grounds<br/><img src='/images/Algernon/Logs.png'>"
collection: portfolio
---

Ok we're back with another [Proving Grounds](https://www.offsec.com/labs/) box, also part of TJ Null's OSCP [lab prep list](https://docs.google.com/spreadsheets/u/1/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/htmlview#). 

Let's dive in with a basic nmap scan which revealed these ports:

PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http

Ny experience so far is that we usually don't find much with port 22, so I went to port 80 while I scanned for additional directories and ran a full port scan (which revealed nothing in the end). The web page reaveals an index with one directory which we follow to an admin page for a CMS called GRAV. 

![Astronaut Directory](/images/Astronaut/80_landingpage.png){: .center-aligned width="800px"}

![Astronaut Grav Admin](/images/Astronaut/grav_admin.png){: .center-aligned width="800px"}

I think we have figured out why the box is called 'Astronaut.' I browsed around for a little bit, but there's not much there, not even a login page even though we're ostensibly looking at the admin page. We get the feroxbuster scan back and see a sub-directory called IP$/grav-admin/admin. That's a pretty good sign. Ultimately after looking through the source code and checking for any additional directories, I couldn't find much. I decided to check for public exploits, but I thought it made sense to try and brute force at the same time with a few basic options in Burp Intruder. That didn't last long. 

![Astronaut Timeout](/images/Astronaut/timeout.png){: .center-aligned width="800px"}

At least know we can pretty much ruling out any kind of brute force. We can see a couple of public exploits, but most of them either require Metasploit, which I'm trying to avoid, authentication, or involve vulnerabilities I wouldn't expect to see in a lab like this. Fortunately there is one for [Arbitrary YAML Write/Update](https://www.exploit-db.com/exploits/49973) that looks promising. Looking through the code it looks like we need to change some of the arguments. 

![Astronaut Exploit](/images/Astronaut/exploit_changes.png){: .center-aligned width="800px"}

And off we go. To be honest, I couldn;'t get this working for a while, but after I found nothing on the full port scan, I figured this had to be the path. I just had to figure out this error. 

![Astronaut Exploit Fail](/images/Astronaut/exploit_fail.png){: .center-aligned width="800px"}

The issue here for me was that the error didn't exactly point me in the right direction because the exploit never really got started. The problem was that the code says the target should look like this: 
<br>
|target= "http://192.168.1.2"|
<br>

But if you look further in the code, you can see this:
<br>
| r = s.get(target+"/admin") |
<br>
The code is going to add /admin to the target, but that won't actually take you anywhere because the IP$/admin directory doesn't exist. In fact the target needs to look like this:

|target= "http://192.168.1.2/grav-admin"|

It's also important not to add the trailing "/" which is actually counter to a previous lab where you must add the "/" yourself. Anyway, once we figured that out it was smooth sailing. We ran the code and caught the shell. 

![Astronaut Exploit Fail](/images/Astronaut/shell_caught.png){: .center-aligned width="800px"}

I enumerated manually for a while which turned out to be a little inefficient now that I think about it, given that only ports 22 and 80 were open. Not that I couldn't find ssh keys in the web directory, but they would have been much more likely to be in the home or root directories which I coudln't access. I wound up checking for running root processes and SUID binaries which wound up being key.  

![Astronaut Exploit Fail](/images/Astronaut/suidphp.png){: .center-aligned width="800px"}

What's that doing there? I checked [gtfobins](https://gtfobins.github.io/gtfobins/php/) and eventually ran the php command from there. 

![Astronaut Exploit Fail](/images/Astronaut/proof.png){: .center-aligned width="800px"}

And there we go. Once again, a pretty simple box, but it's good to get reminders abut reading exploit code carefully and checking for low hanging fruit first. On to the next one. 