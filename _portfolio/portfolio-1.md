---
title: "MGT6705 Time-Series-Data-Analysis-and-Forecasting Mid-term Project"
excerpt: "Physicochemical Properties Related to the Quality of Red Wines<br/>: Analyzing Numerical properties that affect the quality of red wines using ordered probit regression models<br/><img src='/images/500x300.png'>"
collection: portfolio
permalink: /portfolio/wine-quality-analysis
layout: single
---

## 📝 Project Overview

In this project, I analyzed which physicochemical properties most significantly affect the quality of red wines using data from the UCI Machine Learning Repository.
Motivated by Korea's high import taxes and sensitivity to wine pricing, the analysis aimed to help consumers underrated high-quality wines using accessible numerical indicators and producers to reduce empirical errors when making the wines.

## 🔬 Methodology

- Dataset: 1599 red wine samples (Portuguese “Vinho Verde”)
- Model: **Ordered Probit Regression** (To properly dictate what type of factors affect and how much)
- Feature Selection: Stepwise variable selection + Type II deviance tests
- Final Model Variables: `volatile acidity`, `total sulfur dioxide`, `sulphates`, and `alcohol`

## 📈 Key Findings

- **Volatile acidity** negatively affects quality (higher → worse).
- **Alcohol** and **sulphates** are positively associated with higher quality.
- **Total sulfur dioxide** has a weak negative effect but interacts subtly with sulphates.
- Final model accuracy: **0.61**, AUC: **0.748**

These findings suggest that even without expert critic ratings, consumers and importers can leverage simple physicochemical indicators to select high-quality red wines.

## 📎 Download Full Report

[📄 Download PDF Report](/files/wine_quality_report.pdf)
[🔍 View R Code Markdown Report (HTML)](/files/Midterm-Project.html)

