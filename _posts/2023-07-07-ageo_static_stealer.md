---
title: 'AgeoStealer malware - static analysis'
date: 2023-07-07
permalink: /posts/2023/07/ageo_info_stealer_static_analysis/
tags:
  - Malware Analysis
  - Reverse Engineering
brief: 'Ageo (or Space) stealer is info stealer malware distributed as electron based app and posed as a free game'
---

Ageo (or Space) stealer is info stealer malware distributed as electron based app and posed as a "free game".
but as we know there's nothing for free, specially when it comes from an untrusted source or developer. today we'll perform a static analysis trying to dissect this app.

first step to identify some facts about this executable we have, we just use [DIE](https://github.com/horsicq/Detect-It-Easy) which detected it as a `NullSoft` installer.

![die](/images/nullsoft-installer.png)

as we already know that electron based application are just compressed inside that installer executable, so next step is to uncompress it! and then jump into that directory to see that it's pretty straight forward that we the javascript file we're interested in at **resource** directory. and by checking `main.js` we can see it does nothing except call the function exported by `coreAES.js` file. 

![main_file_content](/images/main_js.png)

and when it comes to `coreAES.js` itself, it seems it decrypts a JS payload which was encrypted using AES but thanks to the malware author we have already the key and the function to decrypt the payload!!

![core_aes_file_content](/images/coreAES.png)

so basically we don't need to make any effort to decrypt that payload more than just copying the same function to local or [remote](https://www.tutorialspoint.com/execute_nodejs_online.php) IDE with NodeJs support and just run it with just editing the last line, so instead of it returns the decrypted payload it just prints it!

**SPOILER ALERT!!** the decrypted payload is 2500+ LOC !! so we wouldn't like to paste it here but you still can take a look at it on my github repo [decrypted_payload](https://github.com/abuisa/MalwareZoo/tree/master/malwares/Source/Original)

Ok, so i think we know are ready to go completely static here, since we already go the whole code in JS infront of us. just i'd like to share that virustotal report at the time i did the analysis first time (06-07-2023) showed that it was detected only by less that 30% of the AVs although the malware was created on 2018!! it was just detect June-July! [virtus total report](https://www.virustotal.com/gui/file/dca13fc006a3b55756ae0534bd0d37a1b53a219b5d7de236f20b0262f3662659/detection) 

anyway, let's take a look at the JS code was decrypted and check what this nasty malware did over the past 5 years in the wild.