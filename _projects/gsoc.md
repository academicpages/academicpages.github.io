---
title: "Google Summer of Code"
excerpt: "A weekly notebook of my coding journey with GSoC 2023"
collection: projects
---

Hi! Welcome to my personal notebook on my GSoC 2023 journey. In this summer I worked with Dr. Augustin Luna and Dr. Bo Yuan on converting [CellBox](https://github.com/sanderlab/CellBox), a model predicting cell pertubation effects under various drug combinations, from Tensorflow to Pytorch. This notebook serves as my weekly goals record. For some more detailed comments I have during my coding period, please check out my [Google Docs personal notebook](https://docs.google.com/document/d/1fYkUNYuRcPHByWUYay6yUeTKtBuiwTGKJoztT0LajiA/edit?usp=sharing). This is my final Pytorch [implementation](https://github.com/Mustardburger/CellBox) of CellBox.

## Overview
CellBox (original [repo](https://github.com/sanderlab/CellBox) and [paper](https://www.sciencedirect.com/science/article/pii/S2405471220304646)) is a deep learning model that predicts perturbation effects on cells when applied with different combinations of drugs. It takes in as input a matrix of normalized combinations of drug doses (`shape=(89, 89)`, corresponding to 89 unique drug combinations), and it predicts expressions of different proteins within the cell for each drug combination (`shape=(89, 99)`, corresponding to 99 protein + phenotypic nodes for all 89 drug combinations).
![CellBox model](/images/cellbox.jpg)

The original CellBox [implementation](https://github.com/sanderlab/CellBox) is in Tensorflow 1 and includes many deprecated functions. Therefore, this project aims to convert it to Pytorch so that other researchers are more familiar with the codebase. The resulting [repo](https://github.com/Mustardburger/CellBox) completely removes Tensorflow from the codebase. This repo passes extensive tests that ensure similar performance compared with the original repo, the most significant result being a full replication of Figure 2C in the original paper. This figure was created by training 500 models with different random seeds and taking the average prediction of all 500 models.
![Figure 2C](/images/figure_2C.png)

## Before GSoC
* [Week 0](/gsoc/week_zero/)

## During GSoC

<div style="display: flex; justify-content: space-between;">
    <div style="flex-basis: 30%; background-color: #FFFFFF; padding: 10px;">
        <ul>
            <li><a href="/gsoc/week_one">Week 1</a></li>
            <li><a href="/gsoc/week_two">Week 2</a></li>
            <li><a href="/gsoc/week_three">Week 3</a></li>
            <li><a href="/gsoc/week_four">Week 4</a></li>
        </ul>
    </div>
    <div style="flex-basis: 30%; background-color: #FFFFFF; padding: 10px;">
        <ul>
            <li><a href="/gsoc/week_five">Week 5</a></li>
            <li><a href="/gsoc/week_six">Week 6</a></li>
            <li><a href="/gsoc/week_seven">Week 7</a></li>
            <li><a href="/gsoc/week_eight">Week 8</a></li>
        </ul>
    </div>
    <div style="flex-basis: 30%; background-color: #FFFFFF; padding: 10px;">
        <ul>
            <li><a href="/gsoc/week_nine">Week 9</a></li>
            <li><a href="/gsoc/week_ten">Week 10</a></li>
            <li><a href="/gsoc/week_eleven">Week 11</a></li>
            <li><a href="/gsoc/week_twelve">Week 12-13</a></li>
        </ul>
    </div>
</div>

## After GSoC
* [Final report](/gsoc/final_report)

