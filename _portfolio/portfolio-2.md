---
title: "Flimsy - Proving Grounds"
excerpt: "A Writeup of the Flimsy Box from Proving Grounds<br/><img src='/images/Flimsy/initial_cover.png'>"
collection: portfolio
---

Here's another relatively simple box from [Proving Grounds](https://www.offsec.com/labs/) called Flimsy. It turned out to be a decent reminder to be patient and diligent when I'm working through these labs because I would have saved a lot of trouble if I had just done a better job of one simple thing. Right off the bat I ran a simple nmap scan showing ports 22, 80, and 3306 as open. That's going to point toward web exploits or some kind of SQLi, so it makes sense to check out the web page while running a more detailed scans. 

![Flimsy Landing Page](/images/Flimsy/initial_cover.png){: .center-aligned width="800px"}

Overall, the web page doesn't seem to have much, but a contact page, and subsequent feroxbuster scans seemed to only show /js, /css and /img sub-directories which I couldn't find anything interesting in. Knowing that there is a running MySQL server, I attempted to perform SQLi on the contact form, but everything I submitted returned a 405 Not Allowed response from nginx. 

![Contact Page](/images/Flimsy/contact_sqli.png){: .center-aligned width="800px"}

By this point, I had also run a full port scan on the target IP, and found that port 43500 was open. 

PORT      STATE SERVICE VERSION
43500/tcp open  http    OpenResty web app server
|_http-server-header: APISIX/2.8
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).

When visiting the port in the browser, I found this page. 

![Port 43500](/images/Flimsy/43500.png){: .center-aligned width="800px"}

Not a lot of information there, but I checked exploit-db to see if I could find any available exploits and found an [RCE exploit for Apache APISIX 2.12.1](https://www.exploit-db.com/exploits/50829). Not knowing the version, I decided to give it a shot. Initially I couldn't get it working, but I realized that this was due to the target url parameter I passed. Initially I had tried: "http://target:43500," but the response showed that I did in fact need the slash at the end. 

![Initial Response](/images/Flimsy/initial_response.png){: .center-aligned width="800px"}

After that, I got it working. 

![Shell caught](/images/Flimsy/exploit_and_shell.png){: .center-aligned width="800px"}

Terrific. I looked around for a little bit, and found a local.txt file in the home directory of the user, but I was unable to find anything else that stuck out, so I ran linpeas and found a couple of interesting things - namely a suspicious cron job and an unusual directory to write to. 

![Cron Job](/images/Flimsy/linpeas_cron.png){: .center-aligned width="800px"}

![Directory](/images/Flimsy/linpeas_directory.png){: .center-aligned width="800px"}

The two seemed related so I searched for an exploit using apt-get and found this [blog post](https://systemweakness.com/code-execution-with-apt-update-in-crontab-privesc-in-linux-e6d6ffa8d076). From that point it was just a matter of creating a file in the /etc/apt/apt.conf.d - easy peasy right? Except I couldn't get this working either because I didn't have an interactive shell, and I intially couldn't get that working either using this "python -c 'import pty; pty.spawn("/bin/bash")'" because the target used python3, and it took me way too long to realize that. Eventually I actually wrote the same code from the linked exploit myself, and served it to the apt.conf.d directory. That eventually worked. 

![Success](/images/Flimsy/root_shell_proof.png){: .center-aligned width="800px"}

Success! And then I did the whole thing again because I forgot to submit the flag like a ding dong. Lessons reinforced:
1. Try different versions of python when trying to create an interactive shell. 
2. Read the error output. 
3. Honestly recognize that you may need to revert. When re-doing this box, I had to revert for the exploit to work, and I'm honestly not sure why. Looking back it's possible that I had done what was required already, but I couldn't tell because I hadn't reverted the box. Oopsie. 

Thanks for reading!
