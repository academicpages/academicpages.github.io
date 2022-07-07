---
date: 2022-06-28
tags:
- stream
- tips
title: Use hard links to replicate log files in a generated directory
---

Recently I wanted to write program logs to a file, then copy it to the directory where I store my checkpoints. Because I want to log things before I create the checkpoint directory, I attached my logger to a file in my root directory.

At first, I copied the log file after the program was done running. This approach was error-prone - sometimes the log file didn't make it into the checkpoint directory, for example on OOM kill or KeyboardInterrupt, thus data was loss. It also added unnecessary complexity. Here's what it looked like:

```python
logger = logging.getLogger()
logfile = "output_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".log"
logger.addHander(logging.FileHandler())

try:
	# do setup, which might involve creating a bunch of logs...
	checkpoint_dir = create_checkpoint_dir()
	# do work...
finally:
	shutil.copyfile(logfile, os.path.join(checkpoint_dir, "output.log"))
```

I solved the problem by creating a hard link to the log file in my root directory later in the program, after my checkpoint directory was created.

```python
logger = logging.getLogger()
logfile = "output_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".log"
logger.addHander(logging.FileHandler())

# do setup...
checkpoint_dir = create_checkpoint_dir()
os.link(logfile, os.path.join(checkpoint_dir, "output.log"))
# do work...
```

This way, I can stack up log files in my root directory which are named with the date+time, and delete them at will, and they will still be stored in the appropriate checkpoint directory.