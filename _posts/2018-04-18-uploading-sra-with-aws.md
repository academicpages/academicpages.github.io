---
title: Uploading data to the SRA with AWS
permalink: /posts/2018/04/upload-sra-aws
date: 2018-04-17
tags:
    - aws
    - data
---

ZOMG you can upload files to the SRA automatically via Amazon S3!! Here are notes for when I necessarily need to do this again or help someone in my lab do this again.

A note that these notes are basically the instructions that the SRA gives, so if you actually read the SRA's notes and follow them you'll figure it out too.

When you're at the step where you need to submit files to the SRA (i.e. you're on a page with a link like `https://submit.ncbi.nlm.nih.gov/subs/sra/<submissionID>/files`):

## Follow their directions to generate a policy

Use the [AWS Policy Generator](https://awspolicygen.s3.amazonaws.com/policygen.html) with the following settings to create a Bucket Policy:

- **Policy type:** S3 Bucket Policy    
- **Effect:** Allow    
- **Principal:** arn:aws:iam::228184908524:user/SA-SubmissionPortal-S3    
- **AWS Service:** Amazon S3    
- **Actions:**    
	- s3:ListBucket    
	- s3:GetObject    
- **Amazon Resource Name (ARN):** arn:aws:s3:::<your bucket name>

Copy the policy text and attach it to a *bucket*. Note that this doesn't mean you make a new policy through IAM, instead follow [these directions](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/add-bucket-policy.html
) (go to the bucket on aws.amazon.com, click on "Permissions", and paste in the policy text).

If you get an error, you might need to also add `arn:aws:s3:::<your bucket name>/*` to the Resources on the policy.

AND THAT'S IT!

(JK getting the metadata all in order is a bit of pain, but you can also upload a tab-delimited file so it's not that bad tbh...)

OMG THAT WAS SO EASY!

P.S. I double-checked with the SRA help desk, and they confirmed that once you've gotten the confirmation email from the SRA that your data has been successfully uploaded and processed, you can delete the bucket that you used for the upload.
