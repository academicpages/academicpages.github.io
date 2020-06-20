---
title: 'Checking Progress with Bash'
date: 2019-09-24
permalink: /posts/2019/09/progress-with-bash/
excerpt_separator: <!--more-->
toc: true
tags:
  - bash
  - data
---

I'm currently cleaning and wrangling a large (> 2 billion observations) dataset. Due to its size, I'm running code in batch mode on a remote cluster. Not running interactively makes it harder for me to check on my code's progress.
<!--more-->
Many functions will provide a progress bar option which will show up in a log file even when you're running in batch mode. Unfortunately for me, my code consists of a lot of basic operations performed over and over, so there's no built in progress bar I can harness. 

# The Easy Way

One option here is good the old fashioned `print` function. For smaller datasets this is an excellent solution. The basic idea is to just print a status message every iteration (or every $n$ iterations) telling the user. I've used this approach before when the dataset I was working with was much smaller (~30K observations). However, with billions of observations to work through, this would make the log file excessively long and tedious to page through.

An alternative is to only print status messages at some meaningful interval. For this specific task, I'm constructing directed dyadic international trade portfolios from the [UN Comtrade data](https://comtrade.un.org/), so printing a status message after finishing each country is a good trade off. Now I'll be honest, there are only 159 countries in my data, so adding a print statement after each country is completed would add functionally no extra time to my code. I just forgot to add one. I didn't realize this until after my code had been running for several hours, and I didn't want to restart my code just to find out how far along it was.

This may seem like a minor inconvenience; the code will take as long as it takes, and knowing it status will just make the wait seem longer. Unfortunately for me, I can't just let my code take its sweet time. My data are split into yearly files, so I'm running on a high performance computing cluster that lets me run 44 processes simultaneously so I can process each year of data in parallel. The trade off is that my code is run through a job scheduler that ensures that the cluster's resources are distributed fairly among all users. That means I set a time limit on my job when I submitted it, and if my code doesn't look like it will be done in that time limit, I'd like to know so I can email the cluster admins and request an extension. Luckily I did make one decision in my code that saved me here...

# The Hard Way

Thanks to a colleague's suggestion, my code doesn't wait until it finishes to write the results to disk. Normally when cleaning a dataset, I will write a bunch of code to manipulate the data, do any reshaping necessary, and then save the output to disk in `.csv` or `.RDS` format. If the code only takes a couple seconds or minutes to run, this is fine because even if it's interrupted due to a programming error or system crash, it won't take long to re-run it. Even though my data are split up by year, the earliest and shortest of the datasets still contains over 300,000 observations.

To make my life easier in the event of an unforeseen problem, my code writes each line to a `.csv` as its completed. This is a good idea when you're dealing with large datasets and starting from scratch would waste a lot of time. To get an idea of progress, I could just count the number of lines in each output file and compare it to the number in each input file. This isn't super useful as rows in the original data represent exporters, importers, and commodities, and my code uses nested for loops that iterate over countries. Instead, I want to know how many countries have been completed in each in-progress output dataset.

To do this, I need to count the number of unique values in the `Exporter` field of my output dataset. This is (relatively) straightforward to do in Bash using a loop and a couple of basic functions.

## Finding Files

To start, we need to get a list of all the incomplete datasets. My code writes them to a directory called `processed` so we can view them all using

```bash
ls processed/*.csv
```

Add `*.csv` to the end ensures that we don't get any non-text files which could cause an error later in our code.

## Looping

Next, we need to loop over our files. Bash loop syntax is a little different from R or Python loop syntax in that you need to include `do` before the loop contents and `done` afterwards. The loop below just prints out the name of each file and running it is a good starting point.

```bash
for FILE in processed/*.csv
do
	echo $FILE
done
```

## Processing the Files

Now that we've got a loop to iterate through our files, we need a way to extract the relevant information from each file. If we want to know the number of countries completed in each file, we just need to count the number of unique values in the `Exporter` column. To do this, we need to pull out the first column of each dataset, get all the unique values, and then count how many there are.

We do this by using the `cut` function to split each line on commas, and then take the first occurrence to get just the `Exporter` column. The `-d ,` argument specifies commas as separators and the `-f1` argument tells the function to pull out the first of the separated chunks. Next, we use the `sort` function with the `-u` argument to get only unique values, and then finally count the number of lines left.[^1] Putting it all together with pipes yields:

```bash
FIN=$(cut -d , -f1 ${FILE} | sort -u | wc -l)
```

This will give us a count of how many countries show up in the `Exporter` column of the data file.

## Counting it all Up

The last step is to compare the number of unique values of `Exporter` in each data file with the total number in the data. These data contain 159 countries for the time period I'm working with, so I want to divide the result for each file by 159. To do this, I assign a variable to hold the result for each file, and then divide it by 159 using the `bc` utility.

`bc` is an ancient calculator that uses a similarly ancient syntax. Briefly, you need to echo a math equation and then pipe it to `bc`. However, the default precision of `bc` is integer, and we're trying to calculate a proportion, so if we just write `echo "$FIN / 159" | bc` our answer will be zero. To avoid this, we need to set the scale as follows `echo "scale=2; $FIN / 159" | bc`

## Combining it all

Now I can finally put all the moving pieces together and check the progress of my data cleaning.

```bash
for FILE in processed/*.csv
do
	FIN=$(cut -d , -f2 ${FILE} | sort -u | wc -l)
	echo "scale=2; $FIN / 159" | bc
done
```

# Results

Running this code in my project directory gives me the following output

    .35
    .33
    .31
    .25
    .24
    .26
    .26
    .27
    .28
    .25
    .29
    .25
    .27
    .24
    .24
    .28
    .23
    .22
    .22
    .27
    .22
    .25
    .25
    .27
    .25
    .27
    .21
    .22
    .24
    .16
    .13
    .13
    .13
    .12
    .12
    .11
    .11
    .10
    .11
    .11
    .11

My files currently range from 35% done at the beginning of the data in 1963 to 11% in 2005! And I've definitely learned my lesson about including progress messages when working with big data.

As a quick bonus, you can add an extra line to the script to print out the name of the file before the completion percentage. My files are all named `trade_xxxx.csv`, so I can again use the `cut` function to quickly extract the four digits of the year and print it out.

```bash
for FILE in processed/*.csv
do
	FIN=$(cut -d , -f2 ${FILE} | sort -u | wc -l)
	echo $FILE | cut -d _ -f2 | cut -d . -f1
	echo "scale=2; $FIN / 159" | bc
done
```

------
[^1]: Thanks to this fantastic Stack Exchange [answer](https://stackoverflow.com/a/2781511) for the solution to this part of the problem.