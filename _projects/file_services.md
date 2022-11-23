---
title: 'views on education'
date: 2022-10-19
permalink: /posts/2022/10/views-on-education/
tags:
  - English
---

# Background

If the user wants to upload their data onto our platform and take an overview at it, however, the web backend is not able to parse the table file(like CSV and Apache orc), so we design and develop a service to make up this defect. 

> Flask, Pandas

# Design and implement	

I develop this application as a microservice, which runs in a container in Kubernetes. 

key features

- Automatically save data in Object Storage Series via Amazon S3 and return a unique path for this user
- Automatically creates the directories 
- Automatically parse file metadata (eg, row count, column count, first ten rows of this table ) to the web frontend, which support CSV and Apache orc format. 

