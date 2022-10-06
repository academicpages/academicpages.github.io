---
title: "Ship detection from passive underwater acoustic recordings using machine learning"
collection: talks
type: "Talk"
permalink: /talks/11/1/21-talk-4
venue: "Acoustical Society of America"
date: 11/1/21
location: "Seattle, WA"
---

[More information here](https://asa.scitation.org/doi/pdf/10.1121/10.0007848)

The Ocean Observatories Initiative (OOI) hydrophone data contains a rich collection of ship passage events that can be leveraged for passive ship detection. This study uses 6 years of OOI acoustic data collected by the hydrophone located at the southern foot of the Axial Seamount volcano with a sampling rate of 200 Hz. Ship location data from the Automatic Identification System (AIS) is used to predict the presence or absence of ships within an effective radius of the hydrophone, estimated to be 15 km. After, identifying ships with similar acoustic profiles, such as commercial carrier, tanker, cargo, container, and supply ships, a balanced dataset is created with an even distribution of ships within and outside of the estimated radius. The final dataset is separated into a training (70%), validation (10%), and test (20%) dataset, and then used to create k-nearest neighbors (KNN) and logistic regression models using the scikit-learn Python library. The KNN model achieves the best performance and classifies the ships with an accuracy of 98.04%. This shows that it is possible to determine the presence of ships from passive underwater acoustic recordings with high accuracy. [Work supported by the SURIEA program and ONR.]
