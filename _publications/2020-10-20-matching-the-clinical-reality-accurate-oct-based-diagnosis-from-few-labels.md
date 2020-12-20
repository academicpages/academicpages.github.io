---
title: "Matching the Clinical Reality: Accurate OCT-Based Diagnosis From Few Labels"
collection: publications
authors: 'V. Melnychuk, E. Faerman, I. Manakov, T. Seidl'
date: 2020-10-20
excerpt: "![oct-diagn](/images/oct-diagn.png){: style='float: left; width: 350px'}  Recently proposed MixMatch and FixMatch algorithms have demonstrated promising results in extracting useful representations while requiring very few labels. Motivated by these recent successes, we apply MixMatch and FixMatch in an ophthalmological diagnostic setting and investigate how they fare against standard transfer learning. We find that both algorithms outperform the transfer learning baseline on all fractions of labelled data."
venue: 'KDAH-CIKM, Third workshop on knowledge-driven analytics and systems impacting human quality of life'
paperurl: 'https://arxiv.org/abs/2010.12316'
---

Unlabeled data is often abundant in the clinic, making machine learning methods based on semi-supervised learning a good match for this setting. Despite this, they are currently receiving relatively little attention in medical image analysis literature. Instead, most practitioners and researchers focus on supervised or transfer learning approaches. The recently proposed MixMatch and FixMatch algorithms have demonstrated promising results in extracting useful representations while requiring very few labels. Motivated by these recent successes, we apply MixMatch and FixMatch in an ophthalmological diagnostic setting and investigate how they fare against standard transfer learning. We find that both algorithms outperform the transfer learning baseline on all fractions of labelled data. Furthermore, our experiments show that exponential moving average (EMA) of model parameters, which is a component of both algorithms, is not needed for our classification problem, as disabling it leaves the outcome unchanged. Our code is available online: [URL](https://github.com/Valentyn1997/oct-diagn-semi-supervised).