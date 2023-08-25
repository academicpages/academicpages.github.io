---
title: "Evaluating the Impact of Experimental Assumptions in Automated Fault Localization"
collection: talks
type: "Conference Talk"
permalink: /talks/2023-05-17-ICSE2023Melbourne
venue: "ICSE 2023, Melbourne Convention Exhibition Centre | MCEC"
date: 2023-05-17
location: "Melbourne, Australia"
---

[More information here](https://conf.researchr.org/profile/icse-2023/ezekielsoremekun#)

[Website](https://debugging-assumptions.github.io/)

**Abstract:** Much research on automated program debugging often assumes that bug fix location(s) indicate the faults? root causes and that root causes of faults lie within single code elements (statements). It is also often assumed that the number of statements a developer would need to inspect before finding the first faulty statement reflects debugging effort. Although intuitive, these three assumptions are typically used (55% of experiments in surveyed publications make at least one of these three assumptions) without any consideration of their effects on the debugger's effectiveness and potential impact on developers in practice. To deal with this issue, we perform controlled experimentation, split testing in particular, using 352 bugs from 46 open-source C programs, 19 Automated Fault Localization (AFL) techniques (18 statistical debugging formulas and dynamic slicing), two (2) state-of-the-art automated program repair (APR) techniques (GenProg and Angelix) and 76 professional developers. Our results show that these assumptions conceal the difficulty of debugging. They make AFL techniques appear to be (up to 38%) more effective, and make APR tools appear to be (2X) less effective. We also find that most developers (83%) consider these assumptions to be unsuitable for debuggers and, perhaps worse, that they may inhibit development productivity. The majority (66\%) of developers prefer debugging diagnoses without these assumptions twice as much as with the assumptions. Our findings motivate the need to assess debuggers conservatively, i.e., without these assumptions.