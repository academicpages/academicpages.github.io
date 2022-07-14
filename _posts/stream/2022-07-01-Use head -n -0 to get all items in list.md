---
date: 2022-07-01
tags:
- stream
- tips
title: Use head -n -0 to get all items in list
---

You may know that you can use `head -n $n` to get the first N lines of a list. But you may not know that you can supply `n=-0`  to get all items in the list.

I use this frequently when I want to test some preprocessing script on a sample of a dataset before running on the whole dataset. Here is a snippet I use sometimes. It gets the first N lines if an argument is given, otherwise all lines.

```bash
#!/bin/bash
n="$1"
if [ -z "$n" ]
then
    n="-0"
fi

head -n $n data.txt
```

Here is the snippet in action.
```bash
$ seq 1 10 > data.txt
$ bash head_script.sh 1
1
$ bash head_script.sh 5
1
2
3
4
5
$ bash head_script.sh
1
2
3
4
5
6
7
8
9
10
```