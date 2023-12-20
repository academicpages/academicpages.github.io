---
title: 'How to fix `docker-compose: command not found` error with newer versions of Docker'
date: 2023-12-20
venue-type: blog
permalink: /posts/2023/12/docker-compose/
tags:
  - stream
  - tooling
---

The `docker-compose` command is missing from recent versions of Docker, replaced by a plugin built into Docker: `docker compose`.
To restore compatibility with scripts which use `docker-compose`, we can create a wrapper script which forwards its arguments to `docker compose`.
Here's the script:
```bash
# Switch to root
sudo su -
# Write script to file
cat << EOF > /usr/local/bin/docker-compose
#!/bin/bash
docker compose $@
EOF
# Make the script executable so that we can invoke it directly from the shell
chmod +x /usr/local/bin/docker-compose
```

This avoids the error `docker-compose: command not found` which I faced, for example, trying to install https://github.com/amithkoujalgi/ollama-pdf-bot.
