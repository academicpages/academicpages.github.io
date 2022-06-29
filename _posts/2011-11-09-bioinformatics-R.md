---
layout: post
title: "How to plot length distribution of RNA-seq reads"
date: 2018-11-09
category: ["computer", "R", "genomics", "bioinformatics"]
author: "Sung-Cheol Kim"

---

# How to plot a length ditribution of RNA-seq reads?

One of the basic steps in RNA-seq analysis is to plot a length ditribution. There are several ways of doing it.

## Using unix commands

[link in Biostars](https://www.biostars.org/p/72433/)

```
awk 'NR%4 == 2 {lengths[length($0)]++} END {for (l in lengths) {print l, lengths[l]}}' file.fastq
```

First part of awk commands tell the program to pick up the second line group by each 4 lines. And second part saves length of that line as a component of lengths matrix. And the last part is that at the end of the process, print lengths matrix showing length and count.

```
cat reads.fastq | awk '{if(NR%4==2) print length($1)}' | sort -n | uniq -c > read_length.txt
```

With this command, you can save lengths matrix as a file. This time you can put `sort` and `uniq` to make sure that the list are sorted and has only unique lengths.

## Using BBMap utilities

```
readlength.sh in=reads.fq out=histogram.txt
```

This is really fast and this program can handle multiple formats of read files such as fastq, fastq.gz, fasta, sam, bam

# Text manipulation tools

[link](http://www.tldp.org/LDP/GNU-Linux-Tools-Summary/html/x6993.htm)

## sort

```
sort -t : -k 4 -k 1 -g /etc/passwd | more
```

`-t` is the option for the separator chacter, `-k 4` means to select 4th column for indexing, `-k 1` means to use 1st column after sorting by 4th column. `-g` is used if the numerical sorting is not working. `-r` is for reverse sort.

## join

Will put two lines together assuming they share at least one common value on the relevant line. It won't print lines if they don't have a common value.

## cut

```
cut -d ':' -f 1,7 /etc/passwd
```

`-d` is for the separator character, `-f` is used to select columns.

## ispell/aspell

## chcase

```
cat fileName.txt | tr '[A-Z]' '[a-z]'  > newFileName.txt
```

`chcase` is used for converting lower case chacters to upper case characters, or vice versa. and it can be substituted by the above `tr` command.

## fmt

## paste

```
paste file1.txt file2.txt
```

You can see lists of two files side by side.

## expand

## unexpand

## uniq

- `-c` - count the number of occurances of each duplicate
- `-u` - list only unique entries
- `-d` - list only duplicate entries

## tr (translation)

```
cat some_file | tr '3' '5' > new_file
```

This commands write a new_file with 5 where 3 locates before. `tr` finds all cases and replaces with new character.

## nl

the number lines tool
