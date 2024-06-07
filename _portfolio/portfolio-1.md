---
title: "Codo - Proving Grounds"
excerpt: "A Writeup of the Codo Box from Proving Grounds<br/><img src='/images/codo/initial_web_page.png'>"
collection: portfolio
---

This is a pretty simple box from Offensive Security's [Proving Grounds](https://www.offsec.com/labs/) so I figured it would be a good place to start. As always, I began with an nmap scan of the given IP, which in the case returned two ports open - 22 and 80. I then ran a more detailed scan > nmap -sC -A $IP while checking out the web page on port 80. Upon first visiting the web page, we are greeted with this screen:
![Codo Landing Page](/images/codo/initial_web_page.png){: .align-center width="400px"}

One very helpful cluse we can derive from this page is the phrasing "The only user available to login in the front-end is admin." So we know if we are going to brute force any login pages, we're just going to be using the username "admin." We're also able to click on the admin user right under the title of the post revealing the page for the admin user. 
![Admin User Page](/images/codo/admin_user_page.png){: .align-center width="400px"}

I noticed that the URL says >index.php?u=/user/profile/2 so I wanted to see if I could find any other users by changing the user id. I found one for anonymous, but it ultimately led nowhere.
![Anonymous Landing Page](/images/codo/anonymous_user_page.png){: .align-center width="400px"}

Next I checked the more detailed nmap scan but didn't find anything interesting, so I enumerated the directories using feroxbuster. The only especially interesting page there I found was the IP$/admin page, which led to this login screen. Interesting. 

![Admin Login](/images/codo/admin_login.png){: .align-center width="400px"}

I did want to try to brute force this using hydra, but ran a few quick checks on the password first, knowing that the username was likely to be admin as explained above. To my surprise (I knew it was an easy box, but still), the creds admin:admin worked. Cool. I clicked around in this portal looking for a place to upload a shell or something so I could call it back to my machine, and I tried a few options there like uploading smileys, but I ultiamtely couldn't find a way to call them or prove that the file itself had even uploaded to a directory I could call from the browser. I finally just checked exploit-db, and found [this](https://www.exploit-db.com/exploits/50978), an authenticated RCE exploit. Bingo. I knew I already had the admin creds, so it should be easy-peasy. I downloaded the exploit and tried to run it from my machine. 
![Exploit Usage](/images/codo/exploit_usage.png){: .align-center width="400px"}

Unfortunately I could not get it to work, it actually crashed multiple times. So I tried to look through it, basically just to see if I could find anywhere that it was trying to upload a shell to so I could do it manually. Then I saw at the bottom of the exploit:
>  print("[-] Something went wrong, please try uploading the shell manually(admin panel > global settings > change forum logo > upload and access from " + payloadURL +"[file.php])")

Perfect. I just needed to change the forum logo. I guess I hadn't tried that one yet, oops. I created a shell using msfvenom, and uploaded there before calling it from the payloadURL, which, in checking the exploit again, was "options.target + '/sites/default/assets/img/attachments/'" so ultiamtely http://IP$/sites/default/assets/img/attachments/shell.php, and I called that after setting up my listener. 
![Exploit Usage](/images/codo/shell_caught.png){: .align-center width="400px"}

Got it. I enumerated around this machine, looking for ssh creds in particular because I knew port 22 was open, but I couldn't find anything. I then downloaded linpeas from a python server on my kali machine and combed through the output to find this: 
![Exploit Usage](/images/codo/password_found.png){: .align-center width="400px"}

Damn, that was simple. I knew I had only two users to check, offsec and root, and tried root first. 
![Exploit Usage](/images/codo/root.png){: .align-center width="400px"}

And there it is. Overall a pretty simple box. I took too long figuring it out to be honest. I should have checked exploit-db, but I wanted to look around in the admin portal, and I probably should have run linpeas sooner as well. Sometimes I like to do a manual check on these things first, but that probably took a little too much time this time around. But hey, it helps to hammer that lesson home sometimes. 






