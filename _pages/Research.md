---
permalink: /Research/
title: "Research"
excerpt: "About me"
author_profile: true
redirect_from: 
  
---
**1. Developing Physically-interpretable Models for Traffic Flow Dynamic**

In order to study the impacts of ACC vehicles on traffic flow characteristics, it is important to have accurate vehicle-level models of ACC dynamics. \textit{The first contribution of my research is focused on developing physically-interpretable car following models to accurately describe ACC vehicle dynamics. While many car following models have been used to simulate ACC car following behavior, existing models are simplistic, and use a single continuous function for vehicle acceleration which does not properly describe the true acceleration and braking behavior. These functions may lead to inaccurate and unrealistic analysis results on traffic flow characteristics including highway throughput, fuel consumption and emissions.

*	Developed accurate and physically interpretable microscopic car following models to capture the asymmetric driving behavior of commercially available adaptive cruise control (ACC) vehicles
 
* Calibrated car following model parameter values with the Vanderbilt ACC car following datasets and utilized the \textbf{interior-point algorithm} to optimize the discrepancy between simulated trajectories and real data 

* Simulated and conducted model performance comparisons with statistical methods (e.g., F-test) using Matlab%the F-test method by calculating F-statistics  %which indicated that the proposed model reduced 38\% prediction error


2. 

In order to study the impacts of ACC vehicles on traffic flow characteristics, it is important to have accurate vehicle-level models of ACC dynamics. \textit{The first contribution of my research is focused on developing physically-interpretable car following models to accurately describe ACC vehicle dynamics}~\cite{shang2022novel, shang2022modelingITSC}. While many car following models have been used to simulate ACC car following behavior, existing models are simplistic, and use a single continuous function for vehicle acceleration which does not properly describe the true acceleration and braking behavior. These functions may lead to inaccurate and unrealistic analysis results on traffic flow characteristics including highway throughput, fuel consumption and emissions. Specifically, I proposed an \emph{asymmetric model} that is based on the symmetric car-following model and switch parameters under different conditions to realize and reproduce car following dynamics of ACC vehicles. Moreover, I utilize mathematical tools to conduct an \emph{analytical string stability analysis} and a string stability criterion is derived, which offers a guideline on how the transportation community obtains accurate model parameter values. Further, I have calibrated model parameters using experimental ACC driving data to obtain best-fit model parameter values. Utilizing statistics, I have conducted \emph{statistical comparisons} between the proposed asymmetric ACC model and other existing and well-known models. The calibration and simulation results show that \textit{the proposed asymmetric ACC model outperforms other commonly used asymmetric car following models, which reduces spacing error by 44.8\% in describing ACC car following behavior.}
