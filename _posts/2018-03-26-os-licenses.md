---
title: 'Open Source Licenses Explained'
date: 2018-03-26
permalink: /posts/2018/03/os-licenses/
tags:
  - open source
  - software
  - license
---

I ALWAYS forget to put a license on my work until someone reminds me. I've learned over and over that it's important, but I think the reason why it hasn't stuck is that I was never taught *why* it's important.

So that's the goal of this super quick blog post: to explain what a license is and why it matters that your open source software or other materials has one.

## What is a license?

A **license** is a legal document that specifies the conditions under which someone may use a software or written materials. 
This includes rules for downloading, modifying, or redistributing the materials.
All products should have some sort of license, but it's especially important for people in the open source community to be aware of licensing issues.
Most projects don't have lawyers on hand to handle copyright issues and the whole idea behind open source is to making things open for people to use and contribute to!

## Why do you need a license? 

Copyright and intellectual property laws apply to all works of software and written materials. 
Without a license, a work is under *exclusive copyright*: people who are not the copyright holders cannot use, modify, or share the work.
A license can relax these restrictions.

As the **author**, you want to put a license so:
* people can legally use your work! Imagine academics using your software in their papers; that wouldn't be allowed without a sensible license. 
* some licenses protect you from liability if your software or materials cause problems for its users.
* people can contribute to your work in such a way that preserves your copyright permissions

As a **user**:
* you want to be sure you're protected against copyright infringement. The license lies out instructions so you don't use software improperly, share materials without permission, or fail to properly cite the authors.
* you can always *technically* fork a GitHub repository and download the code. But without a license, exclusive copyright supercedes: you do not have permission to use, modify, or share the materials.

## How do you choose a license?

[There's a website for that!](https://choosealicense.com/)

But this site only lists a few of the possible licenses you could use.
There are tons of premade licenses for different types of works (e.g. software, scientific papers).
You don't have to write your own - just search for a prewritten one that fits your criteria.

This website breaks down possible considerations into three categories:

* Permissions - what are users allowed to do with the materials?
* Conditions -  what do you require a user to do in exchange?
* Limitations - what are users *not* allowed to do?

Certain licenses are more or less stringent in each of these categories.
For my software projects, I tend to use the [BSD-2](https://opensource.org/licenses/BSD-2-Clause) or [MIT](https://opensource.org/licenses/MIT) license.
They're both permissive licenses that limit the author's liability.
For papers, I use a Creative Commons license, specifically [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
Creative Commons allows people to share and adapt the work freely, with proper attribution to the authors.