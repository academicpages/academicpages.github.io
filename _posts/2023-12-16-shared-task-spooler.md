---
title: 'How to use task-spooler as a shared queueing system'
date: 2023-12-16
venue-type: blog
permalink: /posts/2023/12/shared-task-spooler/
tags:
  - blog-post
  - tooling
image: '/files/unsplash/super-snapper-sdTL4qTynfM-unsplash.jpg'
imagealt: 'Playmobil people queuing for a gallery while a fancy red sports car whizzes past'
# imageoffset: "61%"
imagecredit_id: '@supersnapper27'
imagecredit_name: 'Super Snapper'
---

# TL;DR
I set up a wrapper around task-spooler.
See the repository: https://github.com/bstee615/shared-task-spooler.

To use it, create a file containing this script and invoke it using the same arguments as task-spooler:

```bash
#!/bin/bash
# Dependencies: sudo apt install -y task-spooler
TS_SOCKET=$(dirname -- "$0")/TS_SOCKET exec tsp -L "$USER" $@
```

Example usage:

```bash
alice@shared-box:~$ q echo hello
0
alice@shared-box:~$ q
ID   State      Output               E-Level  Times(r/u/s)   Command [run=0/1]
0    finished   /tmp/ts-out.t7NbRs   0        0.00/0.00/0.00 [alice]echo hello
alice@shared-box:~$ sudo su - bill
bill@shared-box:~$ q
ID   State      Output               E-Level  Times(r/u/s)   Command [run=0/1]
0    finished   /tmp/ts-out.t7NbRs   0        0.00/0.00/0.00 [alice]echo hello
```

# Why?

I share a machine with several labmates. This machine has a single high-powered GPU which we share for our experiments. However, only one of us (usually) can use it at a time. This means that if someone else is running an experiment, I have to write down my command, wait for their experiment to be over (which can run several hours), get pinged by them, then check back when they're done and run by experiment. If I run my experiment without checking if the GPU is in-use, it can my program can experience an error, or worse, the other person's in-progress program may experience an error and they'll have to reset it. How can we efficiently run our experiments?

There are several shared queueing systems, such as [Slurm](https://slurm.schedmd.com/documentation.html) or [HTCondor](https://htcondor.org/) or [sqs](https://sqs.sourceforge.net/), but these are overkill - they tend to require a lot of work to set up and administrate. Additionally, these often require structuring your scripts around the format of the queueing tool, which slows down our work.
Instead, I set up a shared queue using `task-spooler` ([link](https://vicerveza.homeunix.net/~viric/soft/ts/))!
This solution generally works best when the users are somewhat technical and will not overrun the resources of the machine and interrupt other users' projects. Also, it only works on one machine and can't manage jobs distributed over a cluster. For more advanced systems which can limit resources or run on a cluster, see the alternatives listed above.

# How I developed it

`task-spooler` tool is used to _spool_ Bash scripts, or execute them in sequence.

However, while it's intended to be used from multiple terminals, it isn't intended for multiple users - each user has their own queue of tasks. This is because a different socket is created for each user.

```bash
alice@shared-box:~$ tsp
ID   State      Output               E-Level  Times(r/u/s)   Command [run=0/1]
alice@shared-box:~$ tsp echo hello
0
alice@shared-box:~$ tsp
ID   State      Output               E-Level  Times(r/u/s)   Command [run=0/1]
0    finished   /tmp/ts-out.YZiMxq   0        0.00/0.00/0.00 echo hello
alice@shared-box:~$ sudo su - bill
bill@shared-box:~$ tsp
ID   State      Output               E-Level  Times(r/u/s)   Command [run=0/1]
bill@shared-box:~$ tsp echo hello
0
bill@shared-box:~$ tsp
ID   State      Output               E-Level  Times(r/u/s)   Command [run=0/1]
0    finished   /tmp/ts-out.LjNllC   0        0.00/0.00/0.00 echo hello
```

In order for two users to share a queue, they must share the same socket file, which is specified using the environment variable `TS_SOCKET`.

```bash
alice@shared-box:~$ TS_SOCKET=/tmp/shared-socket tsp echo hello
0
alice@shared-box:~$ TS_SOCKET=/tmp/shared-socket tsp
ID   State      Output               E-Level  Times(r/u/s)   Command [run=0/1]
0    finished   /tmp/ts-out.XItzuo   0        0.00/0.00/0.00 echo hello
alice@shared-box:~$ sudo su - bill
alice@shared-box:~$ TS_SOCKET=/tmp/shared-socket tsp
c: cannot connect to the server
```

Uh oh, now `bill` ncannot access the same queue.
Looking into the source code, we see this is because when bill's tsp tries to open the socket file, they receive the error `ENOACCESS`, which spouts the error message.

```c
```

Now we can make the socket file accessible by all users using `chmod 777`. If you want more restrictive permissions (for example, to restrict access to a specific group of users), you can use [Linux permission groups](https://www.redhat.com/sysadmin/manage-permissions).

```bash
alice@shared-box:~$ chmod 777 /opt/shared-queue/TS_SOCKET
alice@shared-box:~$ TS_SOCKET=/tmp/shared-socket tsp -L "$USER" echo hello
0
alice@shared-box:~$ TS_SOCKET=/tmp/shared-socket tsp
ID   State      Output               E-Level  Times(r/u/s)   Command [run=0/1]
0    finished   /tmp/ts-out.t7NbRs   0        0.00/0.00/0.00 echo hello
alice@shared-box:~$ sudo su - bill
bill@shared-box:~$ TS_SOCKET=/tmp/shared-socket tsp
ID   State      Output               E-Level  Times(r/u/s)   Command [run=0/1]
0    finished   /tmp/ts-out.t7NbRs   0        0.00/0.00/0.00 echo hello
```

Works great!

Finally, we want to distinguish jobs submitted by different users, so that each user can manage their own jobs in the shared queue.
We can do this by giving a label to the jobs using the `-L` option (see [man pages](https://vicerveza.homeunix.net/~viric/soft/ts/#:~:text=-l%20%3Clab%3E%20name%20this%20task%20with%20a%20label%2C%20to%20be%20distinguished%20on%20listing)).


```bash
alice@shared-box:~$ TS_SOCKET=/tmp/shared-socket tsp -L "$USER" echo hello
0
alice@shared-box:~$ TS_SOCKET=/tmp/shared-socket tsp
ID   State      Output               E-Level  Times(r/u/s)   Command [run=0/1]
0    finished   /tmp/ts-out.t7NbRs   0        0.00/0.00/0.00 [alice]echo hello
```

The final version is wrapped into a convenient helper script `q` in this repository: https://github.com/bstee615/shared-task-spooler.
To install it, you can clone it into a directory shared by all users (we have it in `/opt/shared-queue`), add the directory to the `PATH` variable, and start using `q`!
