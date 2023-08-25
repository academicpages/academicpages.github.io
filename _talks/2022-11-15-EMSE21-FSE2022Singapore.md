---
title: "Locating Faults with Program Slicing: An Empirical Analysis"
collection: talks
type: "Conference Talk"
permalink: /talks/2022-11-15-ICSE2023Melbourne
venue: "ESEC/FSE 2022, NUS U-Town"
date: 2022-11-15
location: "Singapore, Singapore"
---

[More information here](https://2022.esec-fse.org/profile/ezekielsoremekun)

**Abstract:** Statistical fault localization is an easily deployed technique for quickly determining candidates for faulty code locations. If a human programmer has to search the fault beyond the top candidate locations, though, more traditional techniques of following dependencies along dynamic slices may be better suited. In a large study of 457 bugs (369 single faults and 88 multiple faults) in 46 open source C programs, we compare the effectiveness of statistical fault localization against dynamic slicing. For single faults, we find that dynamic slicing was eight percentage points more effective than the best performing statistical debugging formula; for 66% of the bugs, dynamic slicing finds the fault earlier than the best performing statistical debugging formula. In our evaluation, dynamic slicing is more effective for programs with single fault, but statistical debugging performs better on multiple faults. Best results, however, are obtained by a hybrid approach: If programmers first examine at most the top five most suspicious locations from statistical debugging, and then switch to dynamic slices, on average, they will need to examine 15% (30 lines) of the code. These findings hold for 18 most effective statistical debugging formulas and our results are independent of the number of faults (i.e. single or multiple faults) and error type (i.e. artificial or real errors).