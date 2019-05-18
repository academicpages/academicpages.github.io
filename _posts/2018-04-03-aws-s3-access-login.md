---
title: Getting access, logging into, and using AWS S3
permalink: /posts/2018/04/aws-s3-access
date: 2018-04-03
tags:
    - coding
    - aws
    - portfolio
---

Like I've written about [before](/posts/2018/02/aws-data-sharing), we use our lab's AWS account to share data with collaborators.
This post explains the different options for getting access to and interacting with S3 buckets.

# Two ways to access S3

There are two main ways to interact with an S3 bucket and the objects in it: through the AWS **command-line interface** (AWS CLI) via your terminal, or through the AWS **console** via the internet (i.e. at [aws.amazon.com](http://aws.amazon.com)).

The **AWS command-line tools (AWS CLI)** are good for uploading and downloading data, but not great to just poke around all folders.
AWS CLI doesn't have tab-complete, takes a while to return requests, and is just generally pretty clunky.
It's also a set of command-line tools, so this may be daunting to some less computationally proficient collaborators.
That said, the command-line tools are the only way to do batch upload and download of files.

The **AWS console** is much more user-friendly to navigate and look through directory structures and available files.
You access it online by logging into [aws.amazon.com](http://aws.amazon.com) and then can just click through folders like in a normal file explorer.
You can also download files this way, but only one by one.

In my opinion, it's very nice for people who do a lot of data management in S3  have both programmatic and console access to their relevant bucket(s).
On the other hand, collaborators who are just accessing data to download it really only need programmatic access.

# Getting set up

Now that you understand the difference between accessing buckets via the command-line vs. the console, let's talk about setting up the access.

Your AWS admin will have set you up with an account that's attached to a certain security policy, which restricts your access to different functionalities.
AWS is incredibly flexible in how much access users can be given: as the admin, I get to decide which buckets (and folders within the buckets) you can view, download from, or write to.
When you're clicking around the console or trying out some commands with the AWS CLI, if you're running into `AccessDenied` or `Forbidden` errors, it's probably because your admin hasn't given you access to do the thing you're trying to do.
This is actually very nice, because in most cases it means that it's very difficult to accidentally mess something up very badly!
(Now that I'm an admin, I'm terrified I'll accidentally give someone access that allows them to mess something up! In the end, that would be my fault not theirs...)
It also means that some errors are likely to not be your fault - if you run up into these errors, don't spend a lot of time trying to debug without first reaching out to your admin to make sure it's not on their side.

When creating your account, your admin gets to choose whether to generate **programmatic** and/or **AWS management console** access.
They are given the access keys and passwords at the time that they create the user.
For the following instructions, you should have received the necessary information, like access keys or usernames and passwords, from your admin.

## AWS command-line interface

To access your bucket via the command line, you first need to install the `aws cli` tools.
You should be able to follow Amazon's [installation instructions]((https://docs.aws.amazon.com/cli/latest/userguide/installing.html)) fairly straightforwardly (unless you have a Windows computer, in which case everything computational will probs be harder for you sry.)

Once everything is installed, you just type `aws configure` and follow the prompts.
You'll see something like each of the following lines pop up:

```
AWS Access Key ID [****************H24Z]:
AWS Secret Access Key [****************Du+/]:
Default region name [us-east-1]:
Default output format [None]:
```

The text in the brackets shows you the current configuration.
If you press enter, nothing changes.
If you're configuring for the first time or with a new access policy, however, you'll want to paste in the `AWS Access Key` and `AWS Secret Access Key` that your admin provided.
Note that the default region name should match the one that the bucket is configured in - again, ask your admin for this info.
Finally, `Default output format` seems to be about the format of information returned by certain AWS queries, like getting bucket configurations or access policies.
If you're just planning to upload/download data, you don't need to worry about this.

Once you've configured your AWS CLI with the correct access, you're all set.
You don't need a username or password or anything else - all the information AWS needs is in the unique access codes you've input already.
You should be able to try out different AWS commands and see if they work.
For example, if you have view access you can now do:

```
aws s3 ls s3://my.bucket/
```

Try uploading a test file to your bucket, and see if you have write access:

```
touch hello.txt
aws s3 cp hello.txt s3://my.bucket/
```

Finally, try downloading a file in your bucket to see if you have access to that:

```
aws s3 cp s3://my.bucket/a_file_you_know_is_there.txt .
```

Note that these commands are not "smart" about identifying directories vs. files - for example, if you're trying to upload a file into a folder by typing `aws s3 cp file.txt s3://bucket/my_folder`, it will instead upload the `file.txt` to a _file_ named `my_folder`.
You need to explicitly include the trailing slash for it to work as expected:

```
aws s3 cp file.txt s3://bucket/my_folder/
```

I recommend adding `--dryrun` to all of your commands before running them for real -  this will show you what it will do without actually doing it.
This is a great way to make sure your files are going _into_ your folders as opposed to a file name, and to just double check you're not accidentally deleting anything.

## AWS console

To get access to the AWS console, your admin needs to have made a user account for you with an associated password that you can use to log in to your account.
Usually, AWS will auto-generate a password for a new user, and then you'll be prompted to change it the first time you log in.

To log in, you should be able to go to [aws.amazon.com](http://aws.amazon.com) and sign in from there.
However, sometimes that re-directs to the main Amazon login page and you can't login with my AWS credentials.
In that case, you can ask your admin for the unique login site to their AWS account.
It's usually something like `https://<account>.signin.aws.amazon.com/console`.

Once there, just put in your username and password.
Then, navigate to the S3 service by clicking on `Services` in the top left, going to `Storage` and clicking on `S3`.

<div style="width: 755px; border: 0;">
  <p>
    <img class="aligncenter" src="http://cduvallet.github.io/images/2018/02/aws_landing.png" alt="AWS landing page" width="810" height="265"/>
  </p>
</div>

And voila, now you can just click around the different S3 buckets.
Here again you'll probably get a lot of `AccessDenied` errors, if you try to go into a bucket that you don't have view access to.
