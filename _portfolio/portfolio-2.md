---
title: "[MGT6705] Time Series Data Analysis and Forecasting Final-term Project"
excerpt: "Forecasting and Enhancing Japanese Tourism to Korea<br/>: Modeling Japanese tourist arrivals using SARIMA/SARIMAX with search trend-based external regressors.<br/>"
semester: "Spring-2024"
semester_sort: 202401
collection: portfolio
---

## 📝 Project Overview

This project aimed to forecast monthly Japanese tourist arrivals to Korea and identify the impact of Korea-related keyword trends on travel behavior. Using Google Trends data and actual tourist statistics, we developed interpretable models to enhance prediction accuracy and provide tourism policy insights. Served as a team leader, responsible for topic proposal, data analysis, and report writing.

## 🔬 Methodology

- Dataset: Monthly Japanese tourist arrivals (2010–2023) + 9 Korea-related search terms (e.g., "K-pop", "Samgyeopsal", "Myeongdong" in Japanese)
- Model: **SARIMA & SARIMAX** (with lagged external regressors)
- Time Series Decomposition: STL(Seasonal-Trend decomposition using Loess) to separate seasonal/trend components
- Model Selection: Grid search over **15,625 SARIMAX lag combinations**
- Evaluation Metric: Root Mean Squared Error (RMSE)
- Final Selected Variables: `Samgyeopsal`, `K-pop`, `Myeongdong`, `Hangang`, `Dakgalbi` (with optimized lags)

## 📈 Key Findings

- **Samgyeopsal** search interest precedes increases in tourists by ~3 months → strong long-term predictor.
- **Myeongdong** and **Hangang** show short-lag response (0–1 month), suitable for time-sensitive campaigns.
- SARIMAX models significantly outperformed SARIMA baselines in forecast accuracy.
- Seasonal lag patterns provide insight into how cultural and culinary interests shape Japanese tourist flow.

## 💡 Policy Recommendations

- 📍 Promote short-term campaigns for locations like *Myeongdong* with digital ads 1 month in advance.
- 🍲 Launch food-themed cultural promotions (e.g., *Samgyeopsal Weeks*) 2–3 months before peak seasons.
- 🎤 Leverage K-pop concerts (e.g., *Waterbomb*) to stimulate summer visits, traditionally a low-demand season.

These strategies allow tourism stakeholders to act on behavioral lead times reflected in online search trends.

## 📎 Download Final Report

[📄 Download PDF Report](/files/Final-Project Document.pdf)

[📊 View Presentation Slides](/files/presentation.pdf)
