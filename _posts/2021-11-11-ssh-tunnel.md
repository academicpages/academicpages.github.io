---
# layout: single
title:  "SSH tunneling"
date: "2021-11-11"
permalink: /posts/2021/11/ssh-tunnel
tags: 
  - ssh
  - ubuntu
# tags:
#   - edge case
---

To forward local port `local_port` to remote port `remote_port` while connecting vis `ssh` on port `ssh_port`, run
<pre>
 ssh -p ssh_port -L local_port:remote_host:remote_port username@remote_host
</pre>

You can forward multiple ports by adding multiple `-L` options.

If `ssh-agent` is not available, include the key by adding `-i path/to/key`.