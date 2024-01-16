---
title: 'How to set up a shared cache for HuggingFace libraries'
date: 2024-01-16
venue-type: blog
permalink: /posts/2024/01/shared-hf-cache/
tags:
  - blog-post
  - tooling
image: '/files/unsplash/duy-pham-Cecb0_8Hx-o-unsplash.jpg'
imagealt: 'people holding shoulders sitting on wall'
imageoffset: "30%"
imagecredit_id: '@miinyuii'
imagecredit_name: 'Duy Pham'
---

# TL;DR
I set up a shared cache for HuggingFace libraries like `transformers` and `datasets`.
See the repository: [https://github.com/bstee615/shared-hf-cache](https://github.com/bstee615/shared-hf-cache).
To use it, create a shared directory which can be edited by all interested users and set the environment variable `export HF_HOME="/huggingface"`.

# The problem: duplicated model checkpoints and datasets

My lab members and I use a shared machine to run, among other things, large language model inference using the `transformers` and `datasets` libraries. HuggingFace libraries download the model weights or datasets, and the downloaded files can be very large (over 50GB).
By default, the weights and datasets are downloaded to some folders under `~/.cache/huggingface/`. Different users will download copies of the same models. This causes the storage requirements to grow much larger than what is needed.

# How to set up a shared HF cache

In order to cut down the amount of storage used, I set up a shared directory `/huggingface` so users can all use the same folder to download their models and datasets. Users need only to set an environment variable using `export HF_HOME="/huggingface"`, then the HF libraries will download all files to the shared folder.

Here's the script I used:

```bash
#!/bin/bash

# Create a group for permissions to the directory
sudo groupadd hf-users
sudo usermod -aG hf-users $USER

# Create shared directory and make it owned by the group
sudo mkdir --mode=u+rwx,g+rwxs,o-rwx /huggingface # Give the directory rwx for user and group, and make files the directory inherit these permissions
sudo chown $USER /huggingface/
sudo chgrp hf-users /huggingface/

# Add to .bashrc
cat <<EOF >> $HOME/.bashrc
export HF_HOME="/huggingface" # Download HF cache items to /huggingface
umask 002 # Give user and group rw/rwx by deefault
EOF

# Optional: join the group in this shell, or restart the shell
newgrp hf-users
```

# Testing it out

The shared cache must be activated with these two commands. The script above adds these to your profile in ~/.bashrc.

```bash
export HF_HOME="/huggingface" # Download HF cache items to /huggingface
umask 002 # Give user and group rw/rwx by default
```

Here's the script I used to test it out, running the same script on two different users at the same time:

```python
# Dependencies:
# pip install transformers torch accelerate bitsandbytes

from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer

# Do inference with Mistral-7B. Load the model weights ten times in a row to simulate loading the weights at the same time as another user.
for i in range(10):
    print("Loading model...")
    model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1", device_map="auto", load_in_4bit=True)
    tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1", padding_side="left")
    model_inputs = tokenizer(["A list of colors: red, blue"], return_tensors="pt").to("cuda")
    print("Generating tokens...")
    generated_ids = model.generate(**model_inputs, do_sample=True, temperature=1.0, max_new_tokens=10)
    print(tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0])
```

# Concurrency

The libraries include a file locking system to prevent concurrency issues from multiple users using the same files at the same time. When I tested it by trying to load the checkpoint with user B while downloading the checkpoint with user A, this gave me an error on user B like so, without interrupting user A:

```bash
PermissionError: [Errno 13] Permission denied: '/huggingface/hub/.locks/models--mistralai--Mistral-7B-v0.1/9742cb4764964155b7a5f35eefad651f590006091ddeb536863d6c5865cca1b9.lock
```
