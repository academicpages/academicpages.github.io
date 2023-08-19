---
title: 'Cyber Security Datasets'
date: 2023-08-19
permalink: /posts/2023/08/datasets/
tags:
  - cyber-AI
  - datasets
  - machine learning
---

Cyber Security Datasets and Code
======

Data is important for machine learning models. Data is extremely  important for developing AI/ML solutions to cyber problems. There have been numerous posts, technical reports, and articles on cyber datasets. They seem to get outdated very quickly and often focus on specific niche areas. You can find these in the reference lists. This post aims to provide a review of the current datasets for the training and evaluation of deep learning models in cybersecurity. 


Summary
======

| Dataset                      | Year | URL                              | Record Data        | Availability     | Security Problem     | Realistic         | Num. Citation | Labels |
|------------------------------|------|----------------------------------|--------------------|------------------|----------------------|-------------------|---------------|--------|
| ISP data                     |      | \cite{ispdataset}                | Flow               | Partially Public | N/A                  | Real              | N/A           | N      |
| UNB datasets                 |      | \cite{unbdataset}                |                    |                  |                      |                   |               |        |
| Firewalls data               |      | \cite{firewalldataset}           |                    |                  |                      |                   |               |        |
| UNSW NB15                    |      | \cite{UNSWNBdataset}             | Packet and Flow    | Public           | Worm/DDos/Recon      | Semi-Synthetic    | 1080          | Y      |
| MAWI                         |      | \cite{mawidataset}               | Packet             | Public           | N/A                  | Real              | 284 (*)       | N      |
| CAIDA                        |      | \cite{caidadataset}              | Packet             | Partially Public | DDos/Worm            | Real              | N/A           | N      |
| UHN (LANL)                   | 2018 | \cite{lanldataset}               | Flow, Host Log     | Public           | N/A                  | Real              | 83            | N      |
| CMSCSE (LANL)                | 2015 | \cite{lanldataset}               | Flow, Host Log     | Public           | APT-style attack     | Semi-Synthetic    | 84            | Y(**)  |
| PicoDomain                   | 2020 | \cite{picodomaindataset}         | Flows (Zeek log)   | Public           | APT-style attack     | Synthetic         | 1             | Y (**) |
| TWOS                         |      | \cite{twodataset}                | Logs               | On Request       | Insider Threat       | Synthetic         | 45            | Y      |
| CMU-CERT                     |      | \cite{CERTdataset}               | Logs               | Public           | Insider Threat       | Synthetic         | 181           | Y(**)  |
| DAPT                         | 2020 | \cite{dapt20dataset}             | Flow               | Public           | APT Style attack     | Synthetic         | 5             | Y      |
| DARPA opTC                   | 2021 | \cite{darpaoptcdataset}          | Logs               | Public           | APT Style Attack     | Synthetic         | 3             | Y(**)  |
| UGR'16                       | 2016 | \cite{ugr2016dataset}            | Flow               | Public           | Dos/PS/Botnet        | Semi-Synthetic    | 113           | Y      |
| Malware training datasets    | 2016 | \cite{malwaretrainingdataset}    | Log                | Public           | Malware              | Synthetic         | 13            | NA     |
| CTU-13                       | 2011 | \cite{ctu13dataset}              | Packet and Flow    | public           | Botnet               | Synthetic         | 512           | Y      |
| IoT-23                       | 2020 | \cite{botiotdataset}             | Flows (Zeek log)   | Public           | IoT related          | Synthetic         | 39            | Y      |
| ToN-IoT                      | 2021 | \cite{moustafa2021new}           | Packet/Flow/Logs   | Public           | IoT related          | Synthetic         | 12            | Y      |
| Bot-IoT                      | 2018 | \cite{iot23dataset}              | Packet and Flows   | Public           | Botnet               | Synthetic         | 332           | Y      |
| EMBER-Malware                |      | \cite{emberdataset}              | PE file (Log??)    | Public           | Malware              | Synthetic         | 143           | Y      |
| SUEE                         | 2017 | \cite{sueedataset}               | Packet             | Public           | DoS (Slowloris-ng)   | Synthetic         | NA            | Y      |
| CSE-CIC-IDS-2018             | 2018 | \cite{sharafaldin2018toward}     | Flow               | Public           | Network-Related      | Synthetic         | 1257          | Y      |
| CICDDoS2019                  | 2019 | \cite{sharafaldin2019developing} | Flow               | Public           | Network-Related      | Synthetic         | 170           | Y      |
| USB-IDS                      | 2021 | \cite{usbidsdataset}             | Flow               | Public           | DoS/DDoS             | Synthetic         | 1             | Y      |
| BETH                         | 2021 | \cite{bethdataset}               | Log (kernel-level) | Partially Public | Botnet               | Real (Honeypot)   | NA            | Y(***) |
| KitSune                      | 2018 | \cite{kitsunedataset}            | Packet             | Public           | IoT related          | Synthetic         | 369           | Y      |
| KDDCup/NSL-KDD               | 1999 | \cite{kddcupdataset}             | Packet             | Public           | DoS/Probe/R2L/U2R    | Synthetic         | NA            | Y      |
| Malware training exercises   | 2016 | \cite{malwaretrafficdataset}     |                    |                  | Malware              |                   |               |        |
| Sherlock                     |      | \cite{sherlockdataset}           | Log                | Public           | Malware (Smartphone) | Semi-Synthetic    | 52            | Y      |
| SABU IDS Alerts              | 2019 | \cite{sabudataset}               |                    | Public           | Many                 | Real (Anonymised) | 4             | NA     |
| Another Warden IDS Alerts    | 2021 | \cite{wardendataset}             |                    |                  |                      |                   |               |        |
| Shell Command Logs           | 2021 | \cite{shelldataset}              | Logs               | Public           | Many                 | Synthetic         | 0             | NA     |
| Hornet 40 (Honeypots data)   | 2021 | \cite{hornetdataset}             | Flow               | Public           | Not Specified        | Real (Honeypot)   | 0             | NA     |
| Security dataset (Mordor)    | 2019 | \cite{mordordataset}             | Logs               | Public           | APT Style Attack     | Synthetic         | NA            | NA     |


Note (\*\*): not directly label on the dataset, but supply a file with ground true malicious activities

\* List of datasets containing lateral movement activities: Unified Host and Network Data Set (LANL) Comprehensive, Multi-Source Cyber-Security Events (LANL) PicoDomain DARPA opTC DAPT-2020 Security dataset (Mordor) repository APTGen


APT Style Datasets
======
## Unified Host and Network Data Set (LANL)
### When it was created 

This dataset is released in 2018 by Los Alamos National Laboratory as a part of the LANL dataset collection (one out of three datasets). This is the latest dataset in the LANL dataset collection.

### How it was created

This data set contains the host and network-based data which were captured within a real environment, the LANL (Los Alamos National Laboratory) enterprise network. To ensure the privacy of the enterprise network, IP addresses and timestamps in the dataset were anonymized in bidirectional flow-based network traffic files. Most of the computers in the monitored enterprise are Windows-based machines which host and network data are collected over a period of 90 days.

### What is in the dataset?

To capture the network information of the enterprise, this dataset captures 2 types of data: host and network data. The network data is provided in .csv format, the data represented a bidirectional network flow data by providing several fields such as Time, eventID, LogHost, Logon Type, LogonTypeDescription, user name, etc. The host data is provided in .json file which captures a subset of Window log events collected from all Window-based machines in the enterprise. Some examples for the Window event log capture in this dataset: Kerberos authentication ticket was requested (4768), Kerberos service ticket was requested (4769), An account was successfully logged on (4624), An account was logged on (4634), etc.

### What type of security problems does it focus on?

As this dataset mainly captures the host and network data from a real enterprise network in a normal operation, this data set does not contain malicious activities.

### Who has been using it?

Since there is no malicious event in this dataset, some current research only uses this data to enrich the benign sample. As this data is collected from a real company network, this dataset could represent the real background data. For example, [1] [com](#_page22_x85.04_y153.30)bine 2 versions of LANL, Unified Host and Network Data Set which only contain benign samples and Comprehensive, Multi-Source Cyber-Security Events which contain both benign and malicious samples to train and evaluate several Machine Learning models for the detection of malicious RDP sessions which abused by attackers during the lateral movement stage. Their LogitBoost model produced the highest performance with an F1 score of 0.997

### Can it be used to train neural networks - such as GCN?

As it only contains benign activities, this dataset can not be used for the training of the Neural network. However, some research used this dataset to enrich their benign sample in their own dataset.

## Comprehensive, Multi-Source Cyber-Security Events (LANL)

### When it was created 
Published in 2015, Comprehensive, Multi-Source Cyber-Security Events datasets is one out of three datasets in the LANL dataset collection.

### How it was created

The dataset contains the data collected from 4 sources of the internal computer network of Los Alamos National Laboratory’s corporate. The monitored network included Windows-based operation system machine with centralized Active Directory domain controller (AD DC) servers. The 4 sources of data included: Windows-based authentication events from both individual computers and AD DC servers; Domain Name Service (DNS) lookups as collected on internal DNS servers; process events (including start and stop events) from individual Windows computers; network flow data collected on at several key router locations.

### What is in the dataset?

This dataset provided a set of 12 gigabytes of compressed network data. The data contain 5 files of data including 4 captured file from different sources (authentication, process, flow, DNS) and 1 additional file that provide well-defined red teaming events that present bad behavior within the 58 days. In total, the dataset presents 1,648,275,307 events for 12,425 users, 17,684 computers, and 62,974 processes after 58 consecutive days.

### What type of security problems it focuses on?

This dataset capture synthetic APT-style attack activities, and relevant authentication log entries were labeled as either malicious or benign. No further details were provided in the dataset as to what types of attacks were performed during the exercise. This is a limiting factor of this dataset.

### Who has been using it?

This dataset is widely used for lateral movement forensic and detection research. Bowman et al. [\[2](#_page22_x85.04_y199.63)] used this dataset to evaluate their unsupervised graph-based machine learning. They introduced a technique to generate an abstract of network user authentication using a graph of authentication and then perform the unsupervised learning on node-level embedding. They obtained the best performance on the LANL dataset using the Graph Learning with Global View (GL-GV) learning model with the True Positive Rate of 85 % and False Positive Rate of 0.9 %. [1] [com](#_page22_x85.04_y153.30)bine 2 version of LANL (Comprehensive, Multi-Source Cyber-Security Events and Unified Host and Network Data Set) to train and evaluate their Machine Learning models (Logistic Regression, Gaussian-NB, Decision Tree, Random Forest, and LogitBoost) for the detection of malicious RDP session which abused by an attacker during the lateral movement stage. Their LogitBoost model produced the highest performance with the F1 score of 0.997

### Can it be used for to train neural networks - such as GCN?

Provided a rich source of information on the network including authentication, processes, etc. This dataset could be used to train the Neural Network for the detection of malicious activities.

## PicoDomain

https://github.com/iHeartGraph/PicoDomain

### When it was created

This in-house generated data set is published in Aug 2020 (according to the first commit of their Github) with the aim to provide a dataset for the cyber security research community.

### How it was created

This in-house generated data is designed as a scaled-down version of a real enterprise network which still contains the most critical elements commonly found in enterprise-level domains. The compact network used to simulate this dataset included a small Windows-based environment with five workstations, a domain controller, a gateway firewall and router, and a small-scale internet that hosted several websites as well as the adversarial infrastructure. To monitor and collect network activities, they use a Zeek network sensor which is installed inside the network in the place such that it had visibility of all traffic in the network.

### What is in the dataset?

The simulation lasted 3 days from July 19th 2019 to July 21st 2019 where the attack campaign was conducted on days 2 and 3 with the background of benign activities. The dataset is provided in the Zeek monitored log file. The logs available are the following types: conn, dce~~ rpc, dhcp, dns, files, http, kerberos, known~~ hosts, known~~ services, NTLM, pe, smb~~ files, smb~~ mapping, software, ssl, weird, and x509. The detailed information on this dataset which included the dataset itself, paper, and Red team log could be found in their Github [3].

### What type of security problems does it focus on?

To generate the PicoDomain dataset, they ran a synthetic APT-style attack campaign which included all stages of the cyber kill chain (CKC). The attack campaign started with a malicious file downloaded from an e-mail attachment. This gave the attacker the initial foothold in the network. The attacker then proceeded to perform various malicious actions typically associated with APT-level campaigns. This included exploiting system vulnerabilities for privilege escalation, registry modifications to maintain persistence, credential harvesting via the tool Mimikatz, domain enumeration, and lateral movement to new systems via the legitimate Windows Management Instrumentation (WMI) service. At the end of the campaign, the attacker compromises a domain admin account, resulting in full network ownership by the attacker

### Who has been using it?

[\[2](#_page22_x85.04_y199.63)] (same author of this dataset) employ an authentication graph and an unsupervised graph-based machine learning pipeline on PicoDomain to detect malicious authentication events associated with lateral movement. They also evaluate their model with Comprehensive, Multi-Source Cyber-Security Events (LANL).

### Can it be used to train neural networks - such as GCN?

This dataset is provided along with the detailed Red Team log which could be used as the ground truth label for the malicious activities. With the compact size when it only monitors a small-scale network, this dataset could be used to train or evaluate neural networks.

## DARPA opTC
### When it was created and Published 

in 2020, this dataset is the result of the DARPA-TC Program (Defence Advanced Research Project Agency - Transparent Computing Program). The Transparent Computing (TC) pro- gram aims to make the currently opaque systems transparent by allowing the component interactions of system operations across all layers of software abstraction to have high-fidelity visibility. The aim is to study APT attacks and potentially provide instant detection to APTs, as well as complete inference to the source of the attack, or the damage that is imposed.

### How it was created

Operationally Transparent Cyber (OpTC) is a technology transition pilot study to determine if the DARPA-TC program could scale without loss of detection performance. Its system architecture is based on Kafka, which is an open-source stream-processing server that is used to pass information among system components. Each host in the monitored network was equipped with an endpoint sensor that monitors the host events, which are then packed into JSON records before being sent to Kafka for further processing and analytics. The resulting dataset contains a large amount of both benign and malicious activities that represent real-world APT scenarios. The dataset contains more than 17 billion events, captured from 1000 hosts that operate on Windows 10 operating systems.

### What is in the dataset?

The dataset contains more than 17 billion events, captured from 1000 hosts that operate on Windows 10 operating systems. In its current form, the data contain around 1,100 gigabytes of data in the compressed JSON format. The events were obtained during a capture period that lasts for 6 days, during which the first 3 days were the White Team carrying out benign activities, while the last 3 days consists of both benign and malicious activities performed by the Red Team. The events were stored in eCAR (Extended Cyber Analytics Repository) format that can describe an action over a host in a network. Each event has three core components, namely objects, actions and fields. An object is an entity that is captured from their network and each individual host, including files, processes, tasks or modules. Temporal information is also included for each event in the form of a timestamp, enabling the potential of observing the sequential attributes of the data. The unique aspect of this dataset is the high granularity level of information that when it can capture the interaction of each individual computer with internal components such as files, modules, registry keys, etc. The dataset also captured processes of each individual computer in a hierarchical manner where they monitored the child and parent of computer processes.

### What type of security problems does it focus on?

The dataset provided a completed capture of APT attack campaigns. On the first day, Red Team conducts a PowerShell empire staging scenario. The attacker (Red Team) carried out the initial check-in to the system and then conduct the foothold establishment incorporated with lateral movements and privilege escalations. At the end of day 1, the attacker already reached the Domain Controller of the network. A different attack campaign occurred on the second day which is called Custom Empireshell Empire. On this day, the Red team uses an automated domain compromise tool running on top of Empire PowerShell called DeathStar to automate the process of exploring the network, credential stealing, privilege escalation, and lateral movement. After reaching the Domain Controller and capturing several critical hosts, they start the exfiltrating data to an external Command and Control server. The third day contains instances of malicious software upgrades.

### Who has been using it?

T. Cochrane et al. [4[\] ](#_page22_x85.04_y275.35) is one of the first researchers using this novel dataset to evaluate their sk- tree model, a supervised learning method developed for detecting malware on streaming trees. They represent computer processes as streaming trees, which reflect the hierarchical relationships between processes within one host. Event logs in the DARPA-opTC dataset were modeled naturally in a streaming tree structure, where each branch of the parent node follows the events that are associated with a particular process. The evaluation of Sk-tree conduct on Day 1 of the attack campaign of DARPA OpTC dataset and achieving an AUROC score of 98 %. [5]

### Can it be used to train neural networks - such as GCN?

The records in this data are not inherently labelled with benign/malicious tags. However, this dataset is provided with a description of the malicious activities provided by the red team actors on their active days. The sheer volume of data up to 17 billion instances of data and eCAR model encapsulated richness of features make it an excellent candidate for the training and evaluation of Neural Network. The class unbalancing of this dataset also reflect the problem of the real-world cyberattack campaign.

## DAPT-2020

### When it was created 
This network-based dataset is introduced in 2020 with the purpose to replicate the character of the APT of the enterprise on a cloud platform for five days where each day can be considered as analogous to 3 months in a real-world scenario.

### How it was created

This dataset is captured from a scale-down synthetic network whose infrastructure involved 2 machines: a Public VM which contains public accessible services and a Private VM which represented an internal network of an enterprise. The simulation was conducted on five consecutive days during the weekday from Monday to Friday. On the first day of the simulation, a set of normal users will conduct normal routine business operations such as updating to WordPress website, interacting with files and folders, etc. To ensure the realisticness of the data, they generate the data with normal labels by collecting data from real users who were involved in the experiment. The synthetic attack campaign was performed in the remaining day and conducted by the Red team.

### What is in the dataset?

This dataset provided network-level data in 2 formats: .csv flow data and .pcap packet data. The raw network data directly captured all the network interfaces of the simulated network. After that, they use CICFlowMeter [6][ to](#_page22_x85.04_y350.51) to extract the traffic flow data along with 80 flow features from the raw data.

###  What type of security problems does it focus on?

With the aim to simulate the behavior of APT campaign on an enterprise, this data involved many attack techniques which cover 4 stages of the APT attack Reconnaissance, Foothold Establish- ment, Lateral Movement, and Data Exfiltration. For example, The attacker activities during the lateral movement stage conducted Credential Compromise techniques (Key Loggers, Hash retrieval, LDAP, Metasploit) Privilege Escalation techniques (Buffer Overflow, Loadmodule, Rootkit, Perl, Sqlattack, Xterm, PS).

### Who has been using it?

S. Lei et al.[[7\]](#_page22_x85.04_y382.39) used DAPT-2020 as benchmarking data for their proposal of a low-order correlation and high-order interaction (LCHI) model for the malicious traffic. The LCHI model selectively extracts the beneficial low-order correlation between the same-type features by the multivariate correlation analysis (MCA) model and attention mechanism. The low-level feature correlation is incorporated with the high-level information extracted from high-order. The experimental results show that LCHI improved 0.64 % of accuracy in DAPT-20 dataset compared to the Deep Neural Network alone.

### Can it be used to train neural networks - such as GCN?

This dataset is suitable for the training of Neural Network since this dataset contain a large amount of feature (up to 80 feature) on flow level, a number of data sample in both classes and well-labelled.

## Security dataset (Mordor)

https://securitydatasets.com/introduction.html

### When it was created

The Security Datasets project is an open-source initiative that contributes malicious and benign datasets, from different platforms to the infosec community to expedite data analysis and threat research. This dataset was previously known as the Mordor dataset.

### How it was created

This dataset was created by replicating various attack techniques. The log data of each attack simulation is captured from an emulated environment. The event log is recorded, ingested, and analyzed by HELK [[8\]](#_page22_x85.04_y426.22) platform.

### What is in the dataset?

The dataset provides pre-recorded security events generated by simulated adversarial techniques in the form of JavaScript Object Notation (JSON) files. The dataset included recorded logs and raw network packets. The simulation contains the attack tactic on Linux, Windows-based machines and the AWS cloud platform.

### What type of security problems it focuses on

The dataset contains various attack techniques categorized by platforms, adversary groups, tactics and techniques defined by the Mitre ATT&CK Framework including discovery, defence evasion, credential access, lateral movement, persistence, privilege escalation.

### Who has been using it?

N/A

### What it be used for to train neural networks - such as GCN?

Contains a large number of malicious samples that are well categorised by techniques, this dataset could be used to enrich the training of the Neural Network for the detection of a malicious event.

Malware
======

## Malware Training Sets
### When it was created 
Published in 2016, this dataset was released at that time with the purpose to provide the classified dataset for malware analyses and the training of machine learning models
### How it was created

The dataset collects the pattern from malware using 2 common malware analysis: Static analysis (examining the given malware binary without actually running) and Dynamic analysis (Running the malware code in systematically a controlled environment). The analyses were performed through the sample detonation in several SandBoxes (free and commercial ones) which defined the first stage of ontologically homogeneous blocks called “Analyses Results” (AR). The AR latter, will be translated by Malware Instruction Set for Behaviour Analysis (MIST) component which will be encoded into a MIST elaborated meta language to be software agnostic and to give freedom to data scientists.

### What is in the dataset?

The dataset has multiple features extracted from a wide variety of executable malware. The dataset is initially composed of 4764 malware records from 5 different families of malware including APT (292 records), Crypto (record 2020), Locker (431), Zeus (2019 records) and 1270 shadow brokers. As mentioned above, the data was generated by using 2 types of analysis which will produce 2 types of features namely Static and Dynamic. Every feature represents a specific characteristic or behaviour of malware. The extracted features covered a wide range of malware operations such as file activity (open, read, delete, modify, move), Registry activity(open, create, delete, modify, move, query, close), Service activity(open, start, create, delete, modify), Mutex (create, delete), Processes(start, terminate), Run- time DLLs, Network activity(TCP, UDP, DNS, HTTP), Hooking activity, Anti-analysis behaviours, Self-hiding behaviours, etc.

### What type of security problems does it focus on?

This dataset focuses on malware-related attacks including 5 malware families: APT, Crypto, Locker, Zeus and Shadow-brokers.

### Who has been using it?

There have been many recent research that use this dataset for benchmarking malware detection models. E. Masabo et al. [9[\] ](#_page22_x85.04_y458.66)use this dataset to evaluate their malware detection 3-layer neural network model and achieved an accuracy of 97 % and AUC-ROC score of 0.99. [10[\] ac](#_page22_x85.04_y500.00) achieved an accuracy of 94 % when deploying their novel feature engineer approach along with the Gradient Boost model.

### Can it be used to train neural networks - such as GCN?

Contains multiple features extracted from 2 different analyses and contains a large variety of malware families, this dataset could be potentially used in future research to train and evaluate different types of learning models.

## EMBER-Malware
### When it was created 
The EMBER dataset has been published in 2018 with the purpose is to provide a labelled benchmark dataset for the training of a machine learning model to detect malicious Windows portable executable files. Currently, there is 2 version of this dataset: EMBER2017 dataset contained features from 1.1 million Window Portable Executable (PE) files scanned in and before 2017 and the EMBER2018 dataset contains features from 1 million PE files scanned in and before 2018.

### How it was created

N/A

### What is in the dataset?

The EMBER dataset consists of eight groups of raw features that include both parsed features and format-agnostic histograms and counts of strings. Those groups included General file information, Header information, imported function, Exported functions, Section information, Byte histogram, Byte-entropy histogram, and String information. To the pre-processing step easier for future research, they split the data into training and testing sets. There are 900,000 records in the training set contained in 6 files (train0,.., train5) and 200,000 records in the testing set (test). Each data sample file in the training set is collected from a distinct time period.

### What type of security problems does it focus on?

This dataset contains a sample of activities of Window Malware

### Who has been using it?

Beside introduced this dataset in their published work [11],[ the](#_page22_x85.04_y545.78) authors of this dataset implement a malware detection model based on LightGBM model and achieved a 98.2% detection rate with a 1%false positive rate. [[12\] ](#_page22_x85.04_y578.21)who have also used LightGBM model and further improved the performance by reducing the feature space by using file-format agnostic features and achieved the detection up to 99.4% with an AUC value of 0.9997.

### Can it be used to train neural networks - such as GCN?

Providing a large number of data samples and a large set of features, this dataset could be used to train neural networks for the detection of malware

## Sherlock - smartphone malware
### When it was created

 Sherlock dataset provides a significant number of ongoing long-term data collection experiments obtained from smartphone sensors. The data collection process is launched in 2014.

### How it was created

The testbed of the simulation included 50 Galaxy S5 smartphones which is provided to volunteers and required them to use it as the sole smartphone for at least two years. To design the realistic simulate environment for the generation of this dataset, they used 2 tools: SherLock for the data collection and Moriarty for the malicious activities simulation. These smartphones are installed with Moriarty which is a benign application with malicious behaviour. Every few weeks Moriarty is updated to a new version (app + behaviour) via the Google Play store. This dataset could replicate a realistic scenario that malware or spyware  masquerades as a normal application. The victim installs the app from a marketplace without realizing the consequences of the requested permissions.

![ref1]

Figure 1: Sherlock app and malicious behaviour in 2016

### What is in the dataset?

Sherlock dataset contains host-based data captured from seven probes for the PUSH sensors and five probes for PULL sensors. The dataset can provide up to 27 features such as Call Log, SMS Log, App Packages, Hardware Info, WiFi Scan, Battery, and Location (anonymized) which can provide the state of hardware and software as well as the behaviour of user or services/application on the smartphone. By the time of this review, the dataset contain 10 billion data records monitored from 50 users (30 users over 2 year period with the addition of 20 users for 10 months). The SherLock dataset collected samples at a significantly higher frequency (from 5 seconds/sample to a couple of minutes/sample depending on the type of sensor) which will capture the smallest change of the smartphone. The dataset is provided with labelled data which could potentially be used for classification problems. As their Moriarty application simulates the malware behaviour, data related to this application could be considered as a malicious sample.

### What type of security problems it focuses on

This dataset provided the log data that capture the smartphone system behaviour when there is a malicious application which contains smartphone malware running in the background.

### Who has been using it?

As this dataset captures the temporal information (timestamp), several research works which analyse the behaviour of smartphone in the consideration of time series analysis [13, [14,](#_page22_x85.04_y621.49) [15](#_page22_x85.04_y665.88)].[ \[](#_page22_x85.04_y697.21)16][ suggest](#_page23_x85.04_y56.69) the potential of this dataset for malware detection research when their malware detection model which considers the per-user basis and statistical behaviour of each user produce high performance. [17] deployed seven different machine learning models (Logistic Regression, Isotonic Regression, Random Forest, Gradient Boosted Trees, Decision Trees, Support Vector Machine, and Multilayer Perceptron) for classification to either benign or malware. Their gradient-boosted trees model provided the highest on the 35 GB subset of the Sherlock dataset with above 90 % overall accuracy, recall, precision, and F1 score.

### What it be used for to train neural networks - such as GCN?

Currently, there has not been any research on the use of this type of dataset for GCN. Providing a significant number of features and malicious activities, GCN could be potentially used for the detection of the malware present on the phone.

IoT-related
======
## Iot-23
### When it was created 
This dataset was first published in January 2020, with captures ranging from 2018 to 2019. This IoT network traffic was captured in the Stratosphere Laboratory, AIC group, FEL, CTU University, Czech Republic. Its goal is to offer a large dataset of real and labeled IoT malware infections and IoT benign traffic for researchers to develop machine learning algorithms

### How it was created

IoT-23 is a new dataset of network traffic from the Internet of Things (IoT) devices. To simulate the real IoT network, they set up a network with 3 different commercial off-the-shelf IoT devices: a Philips HUE smart LED lamp, an Amazon Echo home intelligent personal assistant and a Somfy smart door lock. The dataset is designed with 23 different scenarios, 20 of which present the execution of malware, only 3 scenario capture network information of these in-test IoT devices in normal operation.

### What is in the dataset?

The data set contains a total of 325,307,990 captured traffic flow, of which 294,449,255 are malicious. This dataset is provided in 2 types of files: .pcap files, which are the original packet capture files, and conn.log.labeled files, which are generated by Zeek network analyzer. This dataset considers IoT-related attacks which consider several families of IoT botnet malware in the dataset such as Mirai, Oriku, Muhstik, Gagfyt, etc. In the attack simulation, the infected devices with this malware botnet will be controlled through C2C server to conduct malicious activities such as DDoS on another victim machine, FileDownload, Port Scan. The dataset is provided in an explicit folder where each folder will contain data captured from different scenarios. This dataset is well labelled since the dataset are labelled based on either the footprint of a type of malware when installed on a device or the activities of the botnet devices (C2C connection, Ddos, Port Scan, FileDownload, etc).

### What type of security problems does it focus on?

This dataset focuses on IoT-related attacks and provided several attack techniques such as DDoS, malware, Botnet, etc.

### Who has been using it?

AK Sahu et al. [[18\] ](#_page23_x85.04_y128.37)used IoT-23 dataset to evaluate their Hybrid Deep Learning model using a Convolution Neural Network (CNN) to extract the accurate feature representation of data and further classify those by Long Short-Term Memory (LSTM) Model. The model produces an accuracy of 96 percent when evaluate on this. [[19\] use](#_page23_x85.04_y160.25) IoT-23 dataset to evaluate an ensemble method that leverages deep models such as the Deep Neural Network (DNN) and Long Short-Term Memory (LSTM) and a meta-classifier (i.e., logistic regression) following the principle of stacked generalization. Their technique achieved 99.7 per cent of accuracy.

### Can it be used to train neural networks - such as GCN?

Providing 2 types of data format (raw and featured), this dataset makes room for future research on the development of a learning model for detecting malicious activities in an IoT environment.

## ToN-IoT
### When it was created 
Released in 2020, The TON-IoT datasets are new generations of Industry 4.0/Internet of Things (IoT) and Industrial IoT (IIoT) datasets for evaluating the fidelity and efficiency of different cybersecurity applications based on Artificial Intelligence (AI)

### How it was created

The datasets were simulated based on a realistic testbed that includes the properties of SDN, NVF and SO which can simulated three layers that comprise modern IoT networks – edge, fog, and cloud. The datasets were gathered in parallel processing to collect labeled data of normal and cyber-attack events from the proposed testbed above. The test-bed architecture of this dataset included five components: Orchestrated server, Middleware server, Client Systems, Offensive systems, and Data management systems.

### What is in the dataset?

Data are collected from a realistic representation of a medium-scale network designed at the Cyber Range and IoT Labs at the UNSW Canberra. The ToN-IoT datasets include heterogeneous data   sources gathered from the Telemetry data of IoT/IIoT services, as well as the Operating Systems logs and Network traffic of IoT network. The datasets were gathered in parallel processing to collect both normal and malicious events from several sources including network traffic (.pcap, Zeek logs), Windows audit traces (Window .blg), Linux audit traces, and telemetry data of IoT services. The raw   data of this dataset is collected from 4 sources which came from different entities of the simulation network: IoT/IIoT, Network, Linux, and Windows. Datasets are provided in 5 different directories:

+ Raw datasets: contain 4 datasets from different sources
+ Processed datasets: Contain four datasets that have been filtered and pre-processed to generate

standard features and their label

+ Train Test datasets: Contain samples of the four datasets in a CSV format that were selected![](Aspose.Words.91fd896a-5dd5-4ed9-9698-3f8fc222ecaf.002.png)![](Aspose.Words.91fd896a-5dd5-4ed9-9698-3f8fc222ecaf.003.png)

to split into hands-on training and testing set. This directory is useful for DL/ML-focused research.

+ Description~~ stats~~ datasets: Contains a description of the features and statistical information of four dataseta

+ SecurityEvents~~ GroundTruth~~ datasets: Contain 4 datasets recorded when the malicious event happening

### What type of security problems it focuses on?

The following attack types are represented in the dataset: Scanning attack, DoS, DDoS, Ran- somware, Backdoor, Injection, Cross-site scripting, Password cracking, and Man-In-The-Middle attacks.

### Who has been using it?

Capturing network activities from 4 different sources make this a versatile dataset when it provides not only network-based data (packet and flow data) but also host-based data (log data from Window, Linux and IoT devices). Gou et al. [20[\] presen](#_page23_x85.04_y192.13)t this dataset to evaluate their ML-based IDS scheme for attack detection in IoT networks by employing an ensemble feature selection approach. Their Random Forrest model achieves the highest accuracy and F1-score of 99.22 and 98.90.

### Can it be used for to train neural networks - such as GCN?

Contains heterogeneous data sources (network data and log data from Windows, Linux and IoT devices), this dataset could be potentially used for the training of various types of detection systems.

## Bot-IoT
### When it was created 
The BoT-IoT dataset was created in 2018 by capturing the network packet from a realistic network environment in the Cyber Range Lab of UNSW Canberra with the purpose to capture the network information of the network under the Botnet attack.

### How it was created

To simulate the Bot-IoT dataset, a test-bed is designed with 2 components: The network platforms include normal and attacking virtual machines (VMs) with additional network devices such as a firewall and tap; and the simulated IoT services, which contain some IoT services such as a weather station. The simulated network of VMs consists of four Kali machines, an Ubuntu Server, Ubuntu, mobile, Windows 7, Metasploitable and an Ubuntu Tap machine. The Kali VMs, which belong to the attacking machines, performed port scanning, DDoS and other Botnet-related attacks by targeting the Ubuntu Server, Ubuntu mobile, Windows 7, and Metasploitable VMs. In the Ubuntu Server, a number of services had been deployed, such as DNS, email, FTP, HTTP, and SSH servers, along with simulated IoT services, in order to mimic real network systems. Node-red middleware is used to simulate the IOT devices in VM environment. The raw network packets (pcap files) of the network are captured by using the tshark tool, a terminal-based Wireshark. The network flow information is also extracted from the raw network packet using the Argus tool. MQTT protocol, a lightweight communication protocol primarily used for real-world IoT devices, is also used to simulate realistic communication between IoT devices.

### What is in the dataset?

The dataset provided 69.3 GB of raw network traffic (.pcap) which contain more than 72.000.000 records. The compact network flow extracted using Argus tool are also take up to 16.7 GB.

### What type of security problems it focuses on?

This dataset considers IoT-related attacks which includes several attack technique such as DDoS, DoS, OS and Service Scan, Keylogging, and Data exfiltration attacks, with the DDoS and DoS attacks further organized, based on the protocol used.

### Who has been using it?

[\[21](#_page23_x85.04_y236.52)] develop a feed-forward neural networks model for binary and multi-class classification of difference attack vectors such as denial of service, distributed denial of service, reconnaissance and information theft attacks. This technique achieves results close to 0.99 across all evaluation measures including accuracy, precision, recall and F1 score.

### Can it be used for to train neural networks - such as GCN?

Containing a large volume of data samples, this dataset could be potentially used for the training of various types of Neural Networks.

## KitSune
### When it was created 
This dataset is obtained from either an IP-based commercial surveillance system or a network full of IoT devices.

###  How it was created

The simulation infrastructure of the dataset consists of two deployments of four HD surveillance cameras. The camera in each deployment is connected to the DVR server via a site-to-site VPN tunnel. An additional network which included a WiFi network populated with 9 IoT devices, and three PC are used to create a more realistic simulation environment (noisier network). Kitsune monitor their network through one of the routers in their network, so in the case of the attack packet is not go direct to the monitored router, the attack activities will be monitored (implicitly) from the change in the statistics of the network’s behaviour causing by the malicious activities.

### What is in the dataset?

In order to provide a snapshot of the network which could capture the statistical information of hosts and their behaviour, Kitsune use AfterImage to extract 115 features from each data record (packet data) in the dataset. Data is stored in both .pcap (raw format) and .csv (with feature) format.

### what type of security problems it focuses on

This dataset focuses on the attack activities on a camera surveillance system with the consideration of the noise from the IoT network. There are 9 attack techniques used to generate this dataset which could be categorised into 4 types: Reconnaissance, Man in the Middle, DoS, Botnet. The attack technique included: OS Scan, Fuzzing, Video Injection, ARP MitM, Active Wiretap, SSDP Flood, SYN DoS, SSL Renegotiation, Mirai. Considering variety

### Who has been using it?

Apart from proposing Kitsune dataset, the author of this dataset also introduce KitNet, a lightweight and online anomaly detection model based on the ensemble autoencoders model. KitNet obtained high performance with an AUC score above 0.9 in 7 out of 9 attack techniques in the Kitsune dataset (0.79 for ARP MitM and 0.8 for Video Injection)

### What it be used for to train neural networks - such as GCN?

![ref1] Figure 2: Kisune 9 attack scenario Each packet (data sample) in the dataset could represent as a node in GCN. However, there is a concern about the explosion of the number of nodes and edges in the GCN model since there is a lot of packet when monitoring a network e.g. a payload is usually split into many small pieces of packets.

Insider Threat
======
## TWOS
### When it was created 
TWOS dataset is delivered along with their paper [22][ whic](#_page23_x85.04_y280.35)h published in 2017. This is a miscel- laneous dataset aim to provide the representation of insider threat behaviours through the gamified simulation approach.

### How it was created

In order to obtain data containing the near-realistic instances of insider threats, the author of TWOS dataset design a multi-player competition where each team mimic a company and tried to sell their product to a common set of customers. The game designed with 3 phases: normal periods, firing and hiring and wildcard. While during the normal phase, the simulation tried to capture the data for normal user behaviour, the other 2 stages tried to stimulate players to conduct behaviours of insider threat such as traitor and masquerader.

### What is in the dataset?

During the game, the author tried to capture user behaviour data through 7 sources: mouse traces, keystrokes, Host monitor Logs (Process and File-System Monitor), network, SMTP Logs – Email Bodies, SMTP Logs – Meta-Information (Excluding Email Bodies), Logon/logout Activities, Psychological Questionnaires. In total, they captured 320 hours of activities from 24 volunteer users spanning 5 days. For each instance of insider threat, 18 hours of masquerader data were recorded and at least two instances of traitor data are also included in the final release of the dataset.

### What type of security problems it focuses on?

The TWOS dataset by using the gamified approach for the simulation to provides instances of insider threat attack scenarios including masqueraders and traitors.

### Who has been using it?

Containing data which capture from various sources, this dataset shows its potential in multiple areas of cyber security that relate to the insider threat area such as authorship verification and identification, continuous authentication, and sentiment analysis. [23] [emplo](#_page23_x85.04_y323.64)y several unsupervised machine learning models for  anomaly detection such as Autoencoder (AE), Isolation Forest (IF), Lightweight On-Line Anomaly Detection (LODA), and Local Outlier Factor (LOF). Their unsupervised AE outperformed others with the highest AUC of 0.794.

### Can it be used for to train neural networks - such as GCN?

Despite containing both examples of traitor and masquerader, this dataset hardly represents the wide variety of insider threat scenarios that take place in real-world settings. There are two main reasons for these shortcomings, involving the synthetic nature of the dataset, and the game theoric approach that was adopted to simulate the insider threat activities. In reality, the masquerader behaviour in the internal network is closely similar to APT behaviours in the stage where they are already in the network (Foothold Establishment, internal Reconnaissance, Lateral Movement, Data Exfiltration).

## CMU-CERT
### When it was created 
CMU-CERT dataset was first introduced in the paper [24][ in ](#_page23_x85.04_y367.47)2013. CMU-CERT dataset is a synthetic dataset that is widely used by current state-of-the-art insider threat detection proposals.

### How it was created

To capture the data instance for insider threat, they designed a synthetic medium-sized organisational intranet and simulated five insider threat scenarios along with normal activities, including: (1) using removable drives to upload data to wikileaks.org, (2) surfing job websites and soliciting employments from competitors, (3) keylogger usage, (4) steal credential files through email and (5) uploading credentials accredited documents to Dropbox for personal gain.

### What is in the dataset?

In the newest iteration of this dataset (r6.2), the dataset contains approximately 200 GB of log data from 4000 users which capture their daily activities between January/2010 and June/2011. For the simulation of attack scenarios, there are 5 users who have taken malicious actions and affected other 23 users.

### What type of security problems it focuses on?

This dataset simulates the malicious activities of insider threat in an enterprise. Attacker activities included collecting other user data, data theft and data exfiltration. These activities will be recorded in the log file provided by this dataset. The dataset provided various security logs including authentication, system (removable drive usage activities), web proxy, email, file access, LDAP and psychometrics. It is noteworthy that these log have been transformed and correlated through a pre-processing procedure resulting in a cleaner and tidier format and stored in several .csv files namely http, file, device, logon and email.

### Who has been using it?

Since this is one of the rare datasets that contain instances of insider threat, this dataset is popularly used in insider threat research. Jiang et al. [25][ used](#_page23_x85.04_y399.35) a combination of a graph-based approach and an anomaly detection technique, utilising multidimensional inputs given by CMU-CERT r4.2 dataset such as user activities, emails correspondence and psychometric measures. A bipartite graph was constructed using the information of user interactions to hosts, each was represented by two distinct sets of vertices. Interactions between users and hosts are reflected by edges with their associated weight. The weights are determined solely from the number of ”logoff” activities during the entire duration of the dataset. [[25\] ](#_page23_x85.04_y399.35)applied a feature engineering process based on statistical analysis, sentiment and topic analysis of all the activities from 1000 users in a stimulated organisation represented in the CMU-CERT r4.2 dataset. They then leverage Graph Convolutional Networks [26] to[ learn](#_page23_x85.04_y443.74) the deeper latent embeddings for detecting malicious insiders.

### Can it be used for to train neural networks - such as GCN?

CMU-CERT dataset [[24\] is](#_page23_x85.04_y367.47) a synthetic dataset that is widely used by current state-of-the-art insider threat detection proposals. It includes system logs of both insider threats and benign activities based on scenarios that contain both traitor and masquerader instances.

Network-related (DDos/Dos/PS/Worm)
======
## UNSW NB15
### When it was created 
The dataset was created in the Cyber Range Lab of the Australian Centre for Cyber Security (ACCS) (Australian Center for Cyber Security (ACCS), 2014) using the IXIA PerfectStorm tool. This data aim to deliver the realistic of the network traffic by using real normal traffic and contemporary synthesized attack traffic. By the time this dataset was released, it aim to address the issue of the lack of modern normal and attack network traffic for the training of machine learning models.

### How it was created

This is semi-synthetic data since it contains the hybrid of real modern normal activities and synthetic contemporary attack behaviours. The test-bed for the simulation in this dataset use emulated environment with 3 virtual servers where one of which formed abnormal/malicious activities in the network traffic. Both normal and attack traffic in the simulation is generated by the IXIA PerfectStorm tool, a network security platform that can generate malicious traffic for test and validating network infrastructure. After the simulation, the dataset contain approximately 100GB of raw data captured by using tcpdump tool. Data is available in 2 formats: raw packet format (.pcap) and flow feature format (.csv). The feature is extracted from raw network data by using the Argus tool and Bro-IDS which generate 2 separate output files. To generate feature-rich flow data, they matched the output file based on the flow identities: Source IP address, Source port number, Destination IP address, Destination port number, Transaction protocol.

### What is in the dataset?

With the aim to produce a feature-rich dataset for the classification task, the generated flow feature data (.csv) contain 42 features (not including flow identity and labels), 30 features are gathered information from data packets, 12 additional feature. The total number of traffic records is two million and 540,044 which are stored in the four CSV files. This dataset aim to provide a bench-marking for evaluating the Network Intrusion Detection System (NIDS) performance.

### What type of security problems it focuses on?

The IXIA tool used to generate this dataset are able to simulate millions of real-world end-user environments. Using this tool, they have generated malicious traffic represented for nine type of attacks: Fuzzers, Analysis, Backdoors, DoS, Exploits, Generic, Reconnaissance, Shellcode and Worms. This dataset not tried to simulate the whole APT campaign when they only contain Reconnaissance and Foothold Establishment stage. The malicious scenario in this dataset focuses on the traffic-level attacks.

### Who has been using it?

Chkirbene et al. [[27\] ](#_page23_x85.04_y475.07)achieved accuracy and F1 score of 95.37 % and 0.92, respectively when using the hybrid anomaly-based intrusion detection model which used the Random Forest (RF) for feature selection and then used RF and Regression Trees for classification. [28] [prop](#_page23_x85.04_y519.46)osed an Anomaly Detection IoT (AD-IoT) system based on Random Forrest. Their model achieved an accuracy up to 99.34 % with an F1 score of 0.98. [[29\] ](#_page23_x85.04_y572.76)proposed to use of deep learning network (DNN) architecture for anomaly detection with an accuracy of 94.04 % and above 0.95 for precision and recall

### Can it be used for to train neural networks - such as GCN?

The attack technique is simulated at the network level which is well-labelled on the flow level based on the attack technique type. The dataset was provided along with the feature-rich flow data, the data have been used to train the Neural Network models for the anomaly detection models.

## CAIDA
### When it was created 
This dataset is proposed by the Center of Applied Internet Data Analysis, which contains different datasets, including, CAIDA DDOS, CAIDA Worm, and RSDoS Attack Metadata (2018-09).

### How it was created

The CAIDA dataset includes a collection of network traffic monitored by the UCSD Network Telescope. The UCSD Network Telescope is a passive traffic monitoring system built on a globally routed, but lightly utilized /8 network. The data observe traffic targeting the dark (unused) address space of the network, or Internet Background Radiation (IBR).

### What is in the dataset?
### What type of security problems it focuses on?

Since monitoring traffic to unused address space, the dataset contains vastly real malicious traffic data with possible network attacks including Ddos from back-scatter resulting from spoofed sources, random scanning of internet attackers, malware, virus, and worm. Traffic data from the misconfiguration of IP addresses of normal users also monitored in the dataset. This dataset does not contain traffic of normal users (no benign data sample).

### Who has been using it?
Authors in [30] use CAIDA DDoS 2007 along with DARPA 1998 and UIDS DDoS dataset to evaluate their information metric measures model for the detection of both low-rate and high-rate DDoS attacks in real-life DDoS datasets.

### Can it be used for to train neural networks - such as GCN?

As most of the data samples in this dataset are malicious, this dataset (solely) is not capable of training Neural networks. However, providing a rich source of data for the network-related attack, this dataset could be used to enrich the attack sample for the training of Neural Networks.

## UGR’16
### When it was created 
Published in 2016, the dataset was designed to allow the training of anomaly detection algorithms that consider the cyclostationary nature of traffic data.

### How it was created

With the purpose to provide a dataset that contains real traffic and up-to-date attacks, the author of this dataset set up a set of Netflow v9 collectors sensors strategically located in the network of a Tier 3 ISP. The ISP in this experiment is a cloud service provider so that many of the services implemented in the network are virtualized. Apart from the normal client of the ISP, they included 25 additional VMs for the data collection purpose, 5 of which is the attacker, 5 victim machine in the core network which is not protected by the firewall, and 15 victim machines in the inner network which were protected by the firewall. The dataset combined the real monitored background traffic from the cloud services and synthetic attack traffic.

### What is in the dataset?

The dataset provided the traffic flow data which IP addresses have been anonymized for privacy purposes. The capture process spans a period of four months, after the collection period, they have successfully captured up to 16,900 million unidirectional flows. The dataset provided with 3 labels: normal, background, or attack. While the normal and attack labeled data are represented for normal user behaviour and attacker behaviour, the background labeled data is represented for the noisy real- world network data which could be normal or an attack. The main advantage of this dataset over others is that the background traffic is very representative of the Internet traffic, as it is captured from sensors in an ISP network where many different profiles of clients are located.

### What type of security problems it focuses on?

The author injected network-related attack scenarios into this dataset including Low-rate DoS, Port Scanning, and Botnet traffic.

### Who has been using it?
[31] use several supervised machine learning algorithms such as Random Forest (RF), Support Vector Machine (SVM) and Logistic Regression (LR) to detect the attack traffic and shown that RF algorithm outperformed others with an average F1 of 0.888 and an average AUC score of 0.868. [32][ used](#_page23_x85.04_y694.25) this dataset for the evaluation of several unsupervised learning algorithms for the detection of intrusions. They obtained the best F1 of 0.37 with ISOS algorithm [33[\] (a](#_page24_x85.04_y56.69) neighbor and statistical-based clustering algorithm)

### Can it be used to train neural networks - such as GCN?

Since this dataset contains the This dataset could be potentially used for the training and evaluation of Neural Network models.

## CTU-13
### When it was created

The CTU-13 is a dataset with botnet traffic that was captured in CTU University, Czech Republic, in 2011. The goal of the dataset was to have a large capture of real botnet traffic mixed with normal traffic and background traffic.

### How it was created

The network used for the simulation and capturing consists of 2 network: Infected Network, Background and normal network. Each host in the network is a virtualized computer running the Microsoft Windows XP SP2 operating system on top of a Linux Debian host. These networks were bridged into one of the CTU University routes where all traffic will be captured these routers and on each host. For the generation of Botnet scenarios, the author designed thirteen scenarios, each with different set of attack techniques.

### What is in the dataset?

In this dataset, raw packet data was captured from the bridging university router and in each individual host using tcpdump tool. After that, Argus, a network analyser tool, was used to convert the raw data into bidirectional NetFlow data. These final NetFlow files were composed of the following fields: Start Time, End Time, Duration, Source IP address, Source Port, Direction, Destination IP address, Destination Port, State, SToS, Total Packets and Total Bytes.

### What type of security problems it focuses on?

This dataset focuses on network-related and malware attack. The dataset contains 13 attack scenarios, each with different set of characteristic including IRC, P2P or HTTP protocols, sent SPAM, did Click-Fraud (CF), port scanning (PS) and DDoS attacks, used Fast-Flux(FF) techniques or were custom compiled (CC).

### Who has been using it?

Bansal et al. [[34\] ](#_page24_x85.04_y96.21)introduce CTU-13 data to compare and evaluate the performance of 3 learning models including RNN, LSTM-based NN and RNN for the detection of malicious traffic. Their LSTM achieved the best F1 score up to 0.8897.

### Can it be used to train neural networks - such as GCN?

Since this dataset provided dataset which simulated various of attack techniques with well-labeled samples. This dataset could be used for the training and evaluation of Neural Networks.

## USB-IDS Datasets
### When it was created 
This dataset was newly introduced a public synthetic intrusion dataset developed at the University of Sannio at Benevento (USB), Italy. This dataset aims to provide the instance of a DoS attack within the network.

### How it was created

To generate the test-bed for the simulation, the author use 3 Linux-based machines to represent 3 entities in the network: an attacker who tries to execute the attack a web server, victim server hosting a Apache web server and a client represent for a normal user access to the web page. The novelty of this dataset is that this dataset monitors the traffic data under several realistic scenarios where in each scenario, the attacker have to face with difference defense modules (given by Apache Software Foundation) of the victim server : Reqtimeout module, Evasive module, Security2, and no defense module. The probing of the simulation produces the raw packet data (pcap)

### What is in the dataset?

The dataset is recorded in the form of traffic flow. Firstly, raw packet data (pcap) is captured. After that, the CICFlowMeter tool is used to generate network traffic flow data from raw format (pcap) and generate up 83 feature for each flow. The flow data was labeled and stored in .csv format.

### What type of security problems it focuses on

This dataset contains malicious instances of 4 different iterations of Dos attack: Hulk (HTTP flood, TCPFlood, Slowloris (slow Dos), and Slowhttptest.

### Who has been using it?

Since this dataset is newly introduced, by the time of the review, none of the recent research has used this dataset.

### What it be used for to train neural networks - such as GCN?

The feature-rich flow data sample makes it applicable to train GCN. The limitation of this dataset is that the simulation only conducts on a very small size of the network (3 hosts). Furthermore, This dataset is focused on Dos network-level attacks, which is not applicable for lateral movements as well as active directory research.

## BETH Dataset
### When it was created 
This dataset is newly introduced in [35[\] for](#_page24_x85.04_y139.50) the anomaly detection and out-of-distribution analysis research.

### How it was created

To generate the dataset, the author keeps track of 23 Linux-based hosts (honeypots) over 5 hours on cloud service. BETH dataset includes both kernel-process logs and network logs (DNS logs). With real “anomalies” collected using a novel tracking system, The dataset contains over eight million data points tracking 23 hosts

### What is in the dataset?

BETH dataset monitors the system in both kernel-process logs and network logs (DNS logs). In total, the dataset produced over 8 million kernel-level process logs. The process call consists of 14 raw features as shown on Figure 1 where the DNS log included 12 raw features as shown on Figure 2. Each record in the dataset is manually labeled. Each record will have 2 labels: suspicious (out- of-distribution activities) and evil (ground true benign/malicious, indicated by a malicious external presence not inherent to the system). The dataset contains the botnet related attack where they observe an attempt to set up a botnet. Each exploited host only contain a single staged attack.

![](Aspose.Words.91fd896a-5dd5-4ed9-9698-3f8fc222ecaf.004.png)

Figure 3: BETH dataset process called feature

### What type of security problems it focuses on

Currently, the publicly available dataset is monitored from the honeypot which only contains Botnet attacks. However, the author mentioned in their paper [35] [that](#_page24_x85.04_y139.50) the full dataset included cryptomining and lateral movement activities (between servers).

### Who has been using it?

Since this dataset is newly introduced, by the time of the review, none of the recent research has used this dataset.

### What it be used for to train neural networks - such as GCN?

The heterogeneously-structured of the logs data could potentially be used to train neural networks where they contain several types of entities (host, user, event) which could be represented as a node in the network.

## DARPA/KDDCup/NSL-KDD
### When it was created 
As KDDCup and NSL-KDD datasets are both generated from DARPA, we will group these datasets as a set of data. Since it was published in 1999, there has been many research projects used this dataset to evaluate their network-based anomaly detection methods and systems. KDDCup is one of the most popular dataset for intrusion detection which was originally based on DARPA 1998/99  [36]. Another enhancement lead to the generation of NSL-KDD. NSL-KDD dataset when it solved the redundant of data sample of the original dataset and rearranging the attack datasample training and testing dataset.


![](Aspose.Words.91fd896a-5dd5-4ed9-9698-3f8fc222ecaf.005.png)

Figure 4: BETH dataset DNS logs feature



### How it was created

KDD Cup dataset built based on the DARPA’98 IDS evaluation program which monitored 7 weeks of network traffic. DARPA’98 is about 4 gigabytes of compressed raw (binary) tcpdump. KDD Cup process the DARPA’98 raw packet into about 4,900,000 connection records and adds more than 20 different types of attacks (e.g. DoS or buffer overflow) to the dataset. NSL-KDD dataset removed duplicates record in the KDD Cup dataset and introduce a more sophisticated testing and training set.

### What is in the dataset?

KDD Cup data provide a hands-on dataset which has been split into training and testing sets. KDD training set contains upto 4,900,000 single connection vectors which each contain 41 feature and labeled as either normal or an attack. Features of KDD can be categorized into 3 group: Basic feature, Traffic Features and Content Features. In the KSL-KDD dataset, the number of data records reduce to about 150,000 data instances.

### what type of security problems it focuses on

There is 24 types of attack involved in the training set and 14 attack type if the testing set. However, the attack technique could be classified into 4 groups: Denial of Service Attack (DoS), User to Root Attack (U2R), Remote to Local Attack (R2L), and Probing Attack. A main drawback of this dataset is that it used outdated technique for the simulation of the attack since this dataset have been released for more than 2 decades.

### Who has been using it?
[37] applied BLSTM model along with the employment of the attention mechanism and the convolutional layers to the NSL-KDD dataset. They achieved a detection rate of up to 84.25 % accuracy. [38] used the J48 decision tree model on the NSL-KDD dataset and achieved the accuracy of 93.82 %, achieved an accuracy more than 90 % and an f1-score 92.26 % when employing the 5-layer AE-based anomaly detection model.

### What it be used for to train neural networks - such as GCN?

With numerousfeatures, this dataset could be applicable to GCN. It could be hard to apply directly KDD cup dataset since it contains many duplicate records in both the training and testing sets. However, we could use NSL-KDD, a dataset based on the original KDD cup but have solved several problems of the original dataset including redundant records in training and testing set, re-arranging the both set and the dataset difficulty level.

## SUEE
### When it was created 
This dataset is released in 2017, this dataset comes with 2 iterations: SUEE1 and SUEE8.

### How it was created

The data sets contain traffic in and out of the web server of the Student Union for Electrical Engineering (Fachbereichsvertretung Elektrotechnik) at Ulm University. Internal hosts are hosts from within the university network, some of them are cable-bound, others connect through one of two wifi services on campus (eduroam and welcome).

### What is in the dataset?

This is a public-domain dataset that contains both benign and malicious traffic relative to the web server of the Student Union for Electrical Engineering at Ulm University. This dataset comes with 2 iteration, SUEE1 monitor 24 hour of traffic and SUEE8 monitor up to 8 days. Data is provided in pcap file which is not labeled but the attacker IP ranges are disclosed. The dataset captured the monitored traffic data in the packet level (.pcap).

### What type of security problems it focuses on?

In the dataset, there are up to 150 IP (spoofed) addresses involved in the attack which runs several iterations of Slow-Dos attack.

### Who has been using it?
[40] developed several concepts based on light-weight flow-based analysis of network traffic that can

identify attacker. They consider six attacker identification schemes in their analysis including Long Connections (LC), Low Packet Rate (LPR), Packet Distance Uniformity (PDU), Combination of LPR and PDU (LPR-PDU), Low Mean Packet Rate (MPR), Low Packet Rate Variance (PRV).

### Can it be used for to train neural networks - such as GCN?

Providing data in the packet level with a concise indication of attacker IP ranges, this dataset could be used for the training of the Neural Network

## CSE-CIC-IDS-2018
### When it was created

CSE-CIC-IDS-2018 is the latest cyber dataset by the Canadian Establishment for Cybersecurity

(CIC) in 2018. The traffic flow data are stored in CSV file with six columns labeled for each flow, namely FlowID, SourceIP, DestinationIP, SourcePort, DestinationPort, and Protocol with more than 80 network traffic features.

### How it was created

To generate the platform for the simulation of adversary scenarios, they construct an infrastructure consisting of two networks, namely Victim-Network and Attack-Network. The adversary network included 50 machines, whereas the victim network included 5 departments, 30 servers and 420 machines. To capture the traffic data interface information, they collect the raw traffic packet data (.pcap) and then use the CICFlowMeter [6[\], ](#_page22_x85.04_y350.51)a flow feature extractor also introduced by CIC, to extract traffic features.

### What is in the dataset?

CSE-CIC-IDS2018 contains about 16,233,002 observations of traffic flow which is collected for over 10 days of the simulation. Each record contains 80 features of the traffic flow along with several labels: SourceIP, SourcePort, DestinationIP, DestinationPort and Protocol.

### What type of security problems it focuses on?

This dataset contains 7 network-related adversary scenarios which include Botnet, Heartbleed, Brute-force, Denial of Service and Distributed Denial of Service, inside network infiltration, and Web attacks.

### Who has been using it?

This dataset contains a wide range of attack technique that could be used for intrusion detection research. Huancayo et al. [?] achieved the accuracy, precision and recall for the Botnet attack detection of 99%, 100% and 99% respectively using Random Forest [?] and Decision Tree [?]. Long short-term memory (LSTM) model with an Attention mechanism of [?] achieved an accuracy of 96.2%, precision, and recall of 96% for detecting web and infiltration attacks.

### Can it be used for to train neural networks - such as GCN?

This dataset is suitable for the training of Neural Network since this dataset contain a large amount of feature (up to 80 feature) on flow level, a number of data sample in both classes and well- labeled.

## CICDDoS2019
### When it was created 
The CICDDoS2019 dataset published in 2019 with the purpose to remedies the shortcomings of the current DDoS dataset.

### How it was created

To construct the testbed for the simulation, they have designed and implemented two networks, namely Attack-Network and Victim-Network. While the Victim-Network is a highly security infrastructure with a firewall, router, switches, and several common operating systems along with an agent that provides the benign behaviors on each PC, the Attack-Network is a completely separated third-party infrastructure that executes differently.

### What is in the dataset?

The dataset capture the traffic flow information which included 80 features extracted from the raw pcap dataset using CICFlowMeter. Each record contains 80 feature of the traffic flow along with several labels: SourceIP, SourcePort, DestinationIP, DestinationPort, and Protocol.

### What type of security problems it focuses on?

This dataset contains many types of the DDoS attack. The training set contains 12 DDoS attacks including NTP, DNS, LDAP, MSSQL, NetBIOS, SNMP, SSDP, UDP, UDP-Lag, WebDDoS, SYN and TFTP. On the testing set, they execute 7 attacks including PortScan, NetBIOS, LDAP, MSSQL, UDP, UDPLag and SYN.

### Who has been using it?

DDoSNet [[41\],](#_page24_x85.04_y363.34) is a leanring model based on autoencoder and RNN deep neural. The learning process of this model contains two stages: pre-training stage (unsupervised) and fine-tuning stage (supervised). DDoSNet produced the average F1 score of 0.99 with an accuracy of 99 percent. AE-MLP [42] is a multi-class classification model which consists of Autoencoder (AE) to extract the compressed and reduced feature sets and an Multi-layer Perceptron Network (MLP) use the extracted features to classify attack into different DDoS attack types. This technique obtained the average of 98.34 % accuracy while the precision, recall, and F1-score all remain at 97.91 %, 98.48 %, and 98.18 % respectively.

### Can it be used for to train neural networks - such as GCN?

Same with the CSE-CIC-IDS-2018 dataset.

Others
======
## ISP data
### When it was created 
The dataset was established in 2019 along with the research on analyzing the internet trend, migration of services to new protocols, and impact of popular services on user behaviour by monitoring the traffic information from tier-2 network in 5 years (from 2013 to 2017).

### How it was created

M. Trevisan et al [[43\] ](#_page24_x85.04_y447.98)build on data collected by the passive monitoring infrastructure of a nationwide ISP in Italy - real data. It operates a backbone tier-2 network, connected to hundreds of customer and peering ASes and a large number of provider ASes. The dataset contains the real-time traffic data that are monitored passively from vantage points located at the edge of the ISP network. The traffic data is then processed by Tstat [[44\], ](#_page24_x85.04_y493.20)a custom-made passive traffic analyzer, and stored in different log files.

### What is in the dataset?

The dataset contained up to 31.9 TB of compressed and anonymized flow logs (around 247 billion         flow records). The Tstat generate 9 difference log files such as log~~ udp~~ complete, log~~ tcp~~ complete, log~~ skype~~ nocomplete, log~~ video~~ complete, log~~ http~~ complete, log~~ skype~~ complete, log~~ mn~~ complete, log~~ chat~~ complete and log~~ chat~~ nocomplete. These logs capture and produce the statistical measurements of the network where each row in the log files corresponds to a different flow and each column is associated with a specific measure. Each record contains classical fields on flow monitoring [\[45](#_page24_x85.04_y536.48)], such as IP addresses, port numbers, packet- and byte-wise counters.

### What type of security problems it focuses on?

The main purpose of this dataset is to analyse the statistical change of traffic networks imposed by the changes of users behaviours and services. The data is labeled based on the application which instantiates the flow. This dataset might contain malicious behaviour in their nature, these samples, however, might not be labeled.

### Who has been using it?

The author of the dataset used it to analyse the influence of the user behaviour, connection duration, operational network and services popularity in recent year to the Internet [44].

### Can it be used for to train neural networks - such as GCN?

Since the purpose of this dataset is to analysis on broadband characterization, service usage, and longitudinal traffic analysis of user trends, hence it is only labeled in terms of application, malicious activities are not classified from normal. Hence no potential for lateral movement/active directory research. With the sheer volume of application-labeled data samples, this dataset is a candidate for the training and evaluation of application classification learning model. [46] [hav](#_page24_x85.04_y579.77)e used this data to evaluate network traffic classification using ML algorithms and statistical techniques.

## MAWI
### When it was created 
This dataset was contributed since 2010 as a labeled version of the MAWI (Measurement and Analysis on the WIDE Internet) archive sample for network points B and F. This dataset contains daily traces of traffic in the form of packet captures, which is captured from a trans-Pacific link between Japan and the United States

### How it was created

The MAWI traffic repository archives traffic data collected from the WIDE backbone networks. The WIDE network (AS2500) is a Japanese academic network connecting universities and research institutes.

### What is in the dataset?

The archive contains tcpdump daily traces of 15 minutes captured in a link between Japan and the United States. The data monitored the data since 2001, however, only data from 2007 are labeled by using a combination of several anomaly detection classifiers. This dataset is really extensive and allows the analysis for a very long period. It is noteworthy that this data does not contain true labels.

### What type of security problems it focuses on?

This data might contain malicious activities as a nature when monitoring modern network captures. However, this dataset does not contain ground true labels in term of normal traffic or malicious traffic. The MAWI dataset can be used to study anomaly detectors, internet traffic characteristics, and traffic classifiers.

### Who has been using it?

The author of this dataset employs an anomaly detection model [47] [with](#_page24_x85.04_y623.61) the aim to provide a labels version of this dataset for future research. As this dataset is not ground-true, Cordero et al [\[48](#_page24_x85.04_y666.34)] injected synthetic attacks (e.g., SYN DDoS, SYN port scan) into MAWI dataset to evaluate their replicator neural networks for the anomalies detection.

### Can it be used for to train neural networks - such as GCN?

Although this data also provided a labeled version by using the anomaly detection model, the labeling is dependent on the classifiers that have been used in the process and their generation of false positives. As there is not ground true labels, this dataset is suitable for evaluating unsupervised anomaly detection system. Containing a large volume of realistic network data, this dataset could be also used as the background data sample for the training of supervised Neural Network when integrating with other attack data samples.

## Shell Command Logs
### When it was created

Released in 2021, This dataset contain Educational data mining and learning analytic are emerging research fields that analyze data from educational contexts. This dataset is , contain the log from the educational cyber training.

### How it was created

This dataset records the command used by the trainee in the cybersecurity training. During each training session, trainees control a virtual machine that run Kali Linux to complete sequences of assignments that mostly involve attacking one or more vulnerable networked hosts. Commands with their arguments were captured using Syslog protocol.

### What is in the dataset?

The dataset contains 13446 shell commands obtained from 175 participants who attended cyber- security training and solved assignments in the Linux terminal. This data capture the command activities by recording the command, their arguments and metadata such as timestamp, working direc- tory, and host identification in the emulated training infrastructure. The commands were captured in Bash, ZSH, Metasploit shells and stored as JSON records.

### what type of security problems it focuses on

This dataset captures various type of malicious log commands conducted by trainees during the cyber security section.

### Who has been using it?

By the time of this review, there has not been any research using this dataset.

### What it be used for to train neural networks - such as GCN?

As it is obtained from the cybersecurity assignments, most of the command in the dataset is malicious hence the dataset (solely) is not applicable for GCN.

## Hornet 40 (Honeypots data)
### When it was created 
The Honeypot was released in 2021, the data was captured from difference honeypot servers in difference periods of 2021

### How it was created

The Hornet datasets contain a collection of datasets designed to help understand how geography may impact the inflow of network attacks. The data was collected from the eight identical configured honey servers which placed in 8 different geographic locationw across North America, Europe, and Asia throughout April and May 2021.

### What is in the dataset?

The dataset captures the network traffic on honeypots. Eight cloud servers were created and configured simultaneously, following identical instructions. The network capture was performed using the Argus network monitoring tool in each cloud server. The data provide the bidirectional NetFlow files in either Argus binary file or CSV format. There is 3 subset of this data which monitor the traffic of the honeynet on 40, 15, 7 days periods.

### What type of security problems it focuses on

The dataset does not specify the labels of the traffic data, however, activities monitored on honeypot are naturally malicious.

### Who has been using it?

By the time of this review, there has not been any research use this dataset.

### What it be used for to train neural networks - such as GCN?

The lack of proper labels and the traffic of the normal user make this dataset (solely) inapplicable for the learning task. Since this dataset contains mostly malicious activity traffic, we could combine this dataset to other network traffic dataset (which also capture network traffic using the Netflow) such as CTU-13, UNSW NB15, etc, to enrich the malicious sample.



References
======

1. T.<a name="_page22_x85.04_y153.30"></a> Bai, H. Bian, A. Abou Daya, M. A. Salahuddin, N. Limam, and R. Boutaba, “A machine learning approach for rdp-based lateral movement detection,” in 2019 IEEE 44th Conference on Local Computer Networks (LCN). IEEE, 2019, pp. 242–245.
2. B.<a name="_page22_x85.04_y199.63"></a> Bowman, C. Laprade, Y. Ji, and H. H. Huang, “Detecting lateral movement in enterprise computer networks with unsupervised graph {AI},” in 23rd International Symposium on Research in Attacks, Intrusions and Defenses ({RAID} 2020), 2020, pp. 257–268.
3. C.<a name="_page22_x85.04_y243.47"></a> Laprade, B. Bowman, and H. H. Huang. PicoDomain. Accessed Nov. 29, 2021. [Online]. Available: <https://github.com/iHeartGraph/PicoDomain>
4. T.<a name="_page22_x85.04_y275.35"></a> Cochrane, P. Foster, V. Chhabra, M. Lemercier, C. Salvi, and T. Lyons, “Sk-tree: a systematic malware detection algorithm on streaming trees via the signature kernel,” arXiv preprint arXiv:2102.07904, 2021.
5. A.<a name="_page22_x85.04_y318.63"></a> Golczynski and J. A. Emanuello, “End-to-end anomaly detection for identifying malicious cyber behavior through nlp-based log embeddings,” arXiv preprint arXiv:2108.12276, 2021.
5. A.<a name="_page22_x85.04_y350.51"></a> H. Lashkari, G. Draper-Gil, M. S. I. Mamun, and A. A. Ghorbani, “Characterization of tor traffic using time based features.” in ICISSp, 2017, pp. 253–262.
5. S.<a name="_page22_x85.04_y382.39"></a> Lei, C. Xia, and T. Wang, “Lchi: Low-order correlation and high-order interaction integrated model oriented to network intrusion detection,” Wireless Communications and Mobile Computing, vol. 2021, 2021.
5. The<a name="_page22_x85.04_y426.22"></a> HELK: open source hunt platforms. Accessed Nov. 29, 2021. [Online]. Available: <https://thehelk.com/intro.html>
5. E.<a name="_page22_x85.04_y458.66"></a> Masabo, K. S. Kaawaase, and J. Sansa-Otim, “Big data: deep learning for detecting malware,” in 2018 IEEE/ACM Symposium on Software Engineering in Africa (SEiA). IEEE, 2018, pp. 20–26.
5. E.<a name="_page22_x85.04_y500.00"></a> Masabo, K. S. Kaawaase, J. Sansa-Otim, J. Ngubiri, and D. Hanyurwimfura, “Improvement of malware classification using hybrid feature engineering,” SN Computer Science, vol. 1, no. 1, pp. 1–14, 2020.
5. H.<a name="_page22_x85.04_y545.78"></a> S. Anderson and P. Roth. Github: Elastic Malware Benchmark for Empowering Researchers. Accessed Nov. 29, 2021. [Online]. Available: h[ttps://github.com/elastic/ember](https://github.com/elastic/ember)
5. H.-D.<a name="_page22_x85.04_y578.21"></a> Pham, T. D. Le, and T. N. Vu, “Static pe malware detection using gradient boosting decision trees algorithm,” in International Conference on Future Data and Security Engineering. Springer, 2018, pp. 228–236.
5. X.<a name="_page22_x85.04_y621.49"></a> Huang, G. C. Fox, S. Serebryakov, A. Mohan, P. Morkisz, and D. Dutta, “Benchmarking deep learning for time series: Challenges and directions,” in 2019 IEEE International Conference on Big Data (Big Data). IEEE, 2019, pp. 5679–5682.
5. H.<a name="_page22_x85.04_y665.88"></a> Li, X. Liu, and Q. Mei, “Predicting smartphone battery life based on comprehensive and real-time usage data,” arXiv preprint arXiv:1801.04069, 2018.
5. Y.<a name="_page22_x85.04_y697.21"></a> Lu, Y. Shu, X. Tan, Y. Liu, M. Zhou, Q. Chen, and D. Pei, “Collaborative learning between cloud and end devices: an empirical study on location prediction,” in Proceedings of the 4th ACM/IEEE Symposium on Edge Computing, 2019, pp. 139–151.
16. S.<a name="_page23_x85.04_y56.69"></a> Wassermann and P. Casas, “Bigmomal: big data analytics for mobile malware detection,” in Proceedings of the 2018 Workshop on Traffic Measurements for Cybersecurity, 2018, pp. 33–39.
16. L.<a name="_page23_x85.04_y84.53"></a> U. Memon, N. Z. Bawany, and J. A. Shamsi, “A comparison of machine learning techniques for android malware detection using apache spark,” Journal of Engineering Science and Technology, vol. 14, no. 3, pp. 1572–1586, 2019.
16. A.<a name="_page23_x85.04_y128.37"></a> K. Sahu, S. Sharma, M. Tanveer, and R. Raja, “Internet of things attack detection using hybrid deep learning model,” Computer Communications, 2021.
16. V.<a name="_page23_x85.04_y160.25"></a> Dutta, M. Chora´s, M. Pawlicki, and R. Kozik, “A deep learning ensemble for network anomaly and cyber-attack detection,” Sensors, vol. 20, no. 16, p. 4583, 2020.
16. G.<a name="_page23_x85.04_y192.13"></a> Guo, “A machine learning framework for intrusion detection system in iot networks using an en- semble feature selection method,” in 2021 IEEE 12th Annual Information Technology, Electronics and Mobile Communication Conference (IEMCON). IEEE, 2021, pp. 0593–0599.
16. M.<a name="_page23_x85.04_y236.52"></a> Ge, X. Fu, N. Syed, Z. Baig, G. Teo, and A. Robles-Kelly, “Deep learning-based intrusion de- tection for iot networks,” in 2019 IEEE 24th Pacific Rim International Symposium on Dependable Computing (PRDC). IEEE, 2019, pp. 256–25609.
16. A.<a name="_page23_x85.04_y280.35"></a> Harilal, F. Toffalini, J. Castellanos, J. Guarnizo, I. Homoliak, and M. Ochoa, “Twos: A dataset of malicious insider threat behavior based on a gamified competition,” in Proceedings of the 2017 International Workshop on Managing Insider Security Threats, 2017, pp. 45–56.

23. D.<a name="_page23_x85.04_y323.64"></a> C. Le and N. Zincir-Heywood, “Anomaly detection for insider threats using unsupervised ensembles,” IEEE Transactions on Network and Service Management, vol. 18, no. 2, pp. 1152– 1164, 2021.
23. J.<a name="_page23_x85.04_y367.47"></a> Glasser and B. Lindauer, “Bridging the gap: A pragmatic approach to generating insider threat data,” in 2013 IEEE Security and Privacy Workshops. IEEE, 2013, pp. 98–104.
23. J.<a name="_page23_x85.04_y399.35"></a> Jiang, J. Chen, T. Gu, K.-K. R. Choo, C. Liu, M. Yu, W. Huang, and P. Mohapatra, “Anomaly detection with graph convolutional networks for insider threat and fraud detection,” in MILCOM 2019-2019 IEEE Military Communications Conference (MILCOM). IEEE, 2019, pp. 109–114.
23. T.<a name="_page23_x85.04_y443.74"></a> N. Kipf and M. Welling, “Semi-supervised classification with graph convolutional networks,” arXiv preprint arXiv:1609.02907, 2016.
23. Z.<a name="_page23_x85.04_y475.07"></a> Chkirbene, S. Eltanbouly, M. Bashendy, N. AlNaimi, and A. Erbad, “Hybrid machine learning for network anomaly intrusion detection,” in 2020 IEEE International Conference on Informatics, IoT, and Enabling Technologies (ICIoT). IEEE, 2020, pp. 163–170.
23. I.<a name="_page23_x85.04_y519.46"></a> Alrashdi, A. Alqazzaz, E. Aloufi, R. Alharthi, M. Zohdy, and H. Ming, “Ad-iot: Anomaly detection of iot cyberattacks in smart city using machine learning,” in 2019 IEEE 9th Annual Computing and Communication Workshop and Conference (CCWC). IEEE, 2019, pp. 0305– 0310.
23. B.<a name="_page23_x85.04_y572.76"></a> A. Tama and K.-H. Rhee, “Attack classification analysis of iot network via deep learning approach,” Res. Briefs Inf. Commun. Technol. Evol.(ReBICTE), vol. 3, pp. 1–9, 2017.
23. M.<a name="_page23_x85.04_y607.13"></a> H. Bhuyan, D. Bhattacharyya, and J. K. Kalita, “An empirical evaluation of information metrics for low-rate and high-rate ddos attack detection,” Pattern Recognition Letters, vol. 51, pp. 1–7, 2015.
23. R.<a name="_page23_x85.04_y650.41"></a> Mag´an-Carri´on, D. Urda, I. D´ıaz-Cano, and B. Dorronsoro, “Towards a reliable comparison and evaluation of network intrusion detection systems based on machine learning approaches,” Applied Sciences, vol. 10, no. 5, p. 1775, 2020.
23. T.<a name="_page23_x85.04_y694.25"></a> Zoppi, A. Ceccarelli, T. Capecchi, and A. Bondavalli, “Unsupervised anomaly detectors to detect intrusions in the current threat landscape,” ACM/IMS Transactions on Data Science, vol. 2, no. 2, pp. 1–26, 2021.
33. E.<a name="_page24_x85.04_y56.69"></a> Schubert and M. Gertz, “Intrinsic t-stochastic neighbor embedding for visualization and outlier detection,” in International Conference on Similarity Search and Applications. Springer, 2017, pp. 188–203.
33. A.<a name="_page24_x85.04_y96.21"></a> Bansal and S. Mahapatra, “A comparative analysis of machine learning techniques for botnet detection,” in Proceedings of the 10th International Conference on Security of Information and Networks, 2017, pp. 91–98.
33. K.<a name="_page24_x85.04_y139.50"></a> Highnam, K. Arulkumaran, Z. Hanif, and N. R. Jennings, “Beth dataset: Real cybersecurity data for anomaly detection research,” TRAINING, vol. 763, no. 66.88, p. 8.
33. R.<a name="_page24_x85.04_y170.83"></a> Lippmann, J. W. Haines, D. J. Fried, J. Korba, and K. Das, “The 1999 darpa off-line intrusion detection evaluation,” Computer networks, vol. 34, no. 4, pp. 579–595, 2000.
33. T.<a name="_page24_x85.04_y202.16"></a> Su, H. Sun, J. Zhu, S. Wang, and Y. Li, “Bat: Deep learning methods on network intrusion detection using nsl-kdd dataset,” IEEE Access, vol. 8, pp. 29575–29585, 2020.
33. L.<a name="_page24_x85.04_y233.49"></a> Dhanabal and S. Shantharajah, “A study on nsl-kdd dataset for intrusion detection system based on classification algorithms,” International journal of advanced research in computer and communication engineering, vol. 4, no. 6, pp. 446–452, 2015.
33. W.<a name="_page24_x85.04_y276.77"></a> Xu, J. Jang-Jaccard, A. Singh, Y. Wei, and F. Sabrina, “Improving performance of autoencoder-based network anomaly detection on nsl-kdd dataset,” IEEE Access, vol. 9, pp. 140136–140146, 2021.
33. T.<a name="_page24_x85.04_y320.06"></a> Lukaseder, L. Maile, B. Erb, and F. Kargl, “Sdn-assisted network-based mitigation of slow ddos attacks,” in International Conference on Security and Privacy in Communication Systems. Springer, 2018, pp. 102–121.
33. M.<a name="_page24_x85.04_y363.34"></a> S. Elsayed, N.-A. Le-Khac, S. Dev, and A. D. Jurcut, “Ddosnet: A deep-learning model for detecting network attacks,” in 2020 IEEE 21st International Symposium on” A World of Wireless, Mobile and Multimedia Networks”(WoWMoM). IEEE, 2020, pp. 391–396.
33. Y.<a name="_page24_x85.04_y407.18"></a> Wei, J. Jang-Jaccard, F. Sabrina, A. Singh, W. Xu, and S. Camtepe, “Ae-mlp: A hybrid deep learning approach for ddos detection and classification,” IEEE Access, vol. 9, pp. 146810–146821, 2021.
33. M.<a name="_page24_x85.04_y447.98"></a> Trevisan, D. Giordano, I. Drago, M. M. Munaf`o, and M. Mellia, “Five years at the edge: Watching internet from the isp network,” IEEE/ACM Transactions on Networking, vol. 28, no. 2, pp. 561–574, 2020.
33. M.<a name="_page24_x85.04_y493.20"></a> Trevisan, A. Finamore, M. Mellia, M. Munafo, and D. Rossi, “Traffic analysis with off-the-shelf hardware: Challenges and lessons learned,” IEEE Communications Magazine, vol. 55, no. 3, pp. 163–169, 2017.
33. R.<a name="_page24_x85.04_y536.48"></a> Hofstede, P. Celeda,ˇ B. Trammell, I. Drago, R. Sadre, A. Sperotto, and A. Pras, “Flow monitoring explained: From packet capture to data analysis with netflow and ipfix,” IEEE Com- munications Surveys & Tutorials, vol. 16, no. 4, pp. 2037–2064, 2014.
33. A.<a name="_page24_x85.04_y579.77"></a> S. Khatouni and N. Zincir-Heywood, “Integrating machine learning with off-the-shelf traffic flow features for http/https traffic classification,” in 2019 IEEE Symposium on Computers and Communications (ISCC). IEEE, 2019, pp. 1–7.
33. R.<a name="_page24_x85.04_y623.61"></a> Fontugne, P. Borgnat, P. Abry, and K. Fukuda, “Mawilab: combining diverse anomaly detec- tors for automated anomaly labeling and performance benchmarking,” in Proceedings of the 6th International COnference, 2010, pp. 1–12.
33. C.<a name="_page24_x85.04_y666.34"></a> G. Cordero, S. Hauke, M. Muhlh¨¨ auser, and M. Fischer, “Analyzing flow-based anomaly in- trusion detection using replicator neural networks,” in 2016 14th Annual Conference on Privacy, Security and Trust (PST). IEEE, 2016, pp. 317–324.
33. D.<a name="_page24_x85.04_y710.18"></a> Giordano. Five Years at the Edge: Watching Internet from the ISP Network. Accessed Nov. 29, 2021. [Online]. Available: <https://smartdata.polito.it/five-years-at-the-edge/>
50. N.<a name="_page25_x85.04_y56.69"></a> Moustafa and J. Slay. The UNSW-NB15 Dataset. Accessed Nov. 29, 2021. [Online]. Available: <https://research.unsw.edu.au/projects/unsw-nb15-dataset>
50. MAWILab.<a name="_page25_x85.04_y85.09"></a> MAWI Working Group Traffic Archive. Accessed Nov. 29, 2021. [Online] h[ttp://mawi. wide.ad.jp/mawi/ and](http://mawi.wide.ad.jp/mawi/) h[ttp://www.fukuda-lab.org/mawilab/data.html.](http://www.fukuda-lab.org/mawilab/data.html)
50. The<a name="_page25_x85.04_y116.97"></a> UCSD Network Telescope. Center for Applied Internet Data Analysis at the University of California’s San Diego Supercomputer Center. Accessed Nov. 29, 2021. [Online]. Available: [https://www.caida.org/projects/network~~ telescope/](https://www.caida.org/projects/network_telescope/)
50. ARCS<a name="_page25_x85.04_y160.80"></a> Data Sets. Advanced Research in Cyber Systems (ARCS). Accessed Nov. 29, 2021. [Online]. Available: <https://csr.lanl.gov/data/>
50. I.<a name="_page25_x85.04_y192.68"></a> Homoliak. Github: TWOS (The Wolf of SUTD) Dataset. Advanced Research in Cyber Systems (ARCS). Accessed Nov. 29, 2021. [Online]. Available: h[ttps://github.com/ivan-homoliak-sutd/ twos](https://github.com/ivan-homoliak-sutd/twos)
50. H.<a name="_page25_x85.04_y234.03"></a> Ivan and G. Joshua. Insider Threat Test Dataset by Carnegie Mellon University. Accessed Nov. 29, 2021. [Online]. Available: h[ttps://kilthub.cmu.edu/articles/dataset/ Insider~~ Threat~~ Test~~ Dataset/12841247/1](https://kilthub.cmu.edu/articles/dataset/Insider_Threat_Test_Dataset/12841247/1)
50. S.<a name="_page25_x85.04_y280.35"></a> Myneni, A. Chowdhary, A. Sabur, S. Sengupta, G. Agrawal, D. Huang, and

    1000. Kang. Gitlab: DAPT-2020 Dataset. Accessed Nov. 29, 2021. [Online]. Available: <https://gitlab.thothlab.org/Advanced-Persistent-Threat/apt-2020/>
50. Github:<a name="_page25_x85.04_y324.19"></a> Operationally Transparent Cyber (OpTC) Data Release. Five Directions. Accessed Nov. 29, 2021. [Online]. Available: <https://github.com/FiveDirections/OpTC-data>
50. G.<a name="_page25_x85.04_y356.07"></a> Maci´a-Fern´andez, J. Camacho, R. Mag´an-Carri´on, P. Garc´ıa-Teodoro, and R. Ther´on. UGR’16: A New Dataset for the Evaluation of Cyclostationarity-Based Network IDSs. Accessed Nov. 29, 2021. [Online]. Available: <https://nesg.ugr.es/nesg-ugr16/index.php#CAL>
50. M.<a name="_page25_x85.04_y399.91"></a> Ramilli. Malware Training Sets: A machine learning dataset for everyone. Accessed Nov. 29, 2021. [Online]. Available: h[ttps://marcoramilli.com/2016/12/16/ malware-training-sets-a-machine-learning-dataset-for-everyone/](https://marcoramilli.com/2016/12/16/malware-training-sets-a-machine-learning-dataset-for-everyone/)
50. S.<a name="_page25_x85.04_y443.74"></a> Garcia, M. Grill, J. Stiborek, and A. Zunino. The CTU-13 Dataset. A Labeled Dataset with Botnet, Normal and Background traffic. Accessed Nov. 29, 2021. [Online]. Available: <https://www.stratosphereips.org/datasets-ctu13>
50. K.<a name="_page25_x85.04_y487.58"></a> Nickolaos, M. Nour, and S. Elena. The BoT-IoT dataset. Accessed Nov. 29, 2021. [Online]. Available: <https://cloudstor.aarnet.edu.au/plus/s/umT99TnxvbpkkoE>
50. N.<a name="_page25_x85.04_y519.46"></a> Moustafa, “A new distributed architecture for evaluating ai-based security systems at the edge: Network ton~~ iot datasets,” Sustainable Cities and Society, vol. 72, p. 102994, 2021.
50. A.<a name="_page25_x85.04_y550.79"></a> Parmisano, S. Garcia, and M. Erquiaga. Aposemat IoT-23: A labeled dataset with malicious and benign IoT network traffic . Accessed Nov. 29, 2021. [Online]. Available: <https://www.stratosphereips.org/datasets-iot23>
50. Github:<a name="_page25_x85.04_y595.17"></a> 2017-SUEE-data-set. Accessed Nov. 29, 2021. [Online]. Available: h[ttps://github.com/ vs-uulm/2017-SUEE-data-set](https://github.com/vs-uulm/2017-SUEE-data-set)
50. I.<a name="_page25_x85.04_y627.05"></a> Sharafaldin, A. H. Lashkari, and A. A. Ghorbani, “Toward generating a new intrusion detection dataset and intrusion traffic characterization.” ICISSp, vol. 1, pp. 108–116, 2018.
50. I.<a name="_page25_x85.04_y658.38"></a> Sharafaldin, A. H. Lashkari, S. Hakak, and A. A. Ghorbani, “Developing realistic distributed denial of service (ddos) attack dataset and taxonomy,” in 2019 International Carnahan Conference on Security Technology (ICCST). IEEE, 2019, pp. 1–8.
50. M.<a name="_page25_x85.04_y702.77"></a> Catillo, A. Del Vecchio, L. Ocone, A. Pecchia, and U. Villano. USB-IDS Datasets. Accessed Nov. 29, 2021. [Online]. Available: <http://idsdata.ding.unisannio.it/>
68. K.<a name="_page26_x85.04_y56.69"></a> Highnam, K. Arulkumaran, Z. Hanif, and N. R. Jennings. BETH Dataset: Real Cybersecurity Data for Anomaly Detection Research. Accessed Nov. 29, 2021. [Online] h[ttps://www.kaggle.com/ katehighnam/beth-dataset and](https://www.kaggle.com/katehighnam/beth-dataset) h[ttps://github.com/jinxmirror13/BETH~~ Dataset~~ Analysis.](https://github.com/jinxmirror13/BETH_Dataset_Analysis)
68. Y.<a name="_page26_x85.04_y97.04"></a> Mirsky, T. Doitshman, Y. Elovici, and N. R. Shabtai, Asaf. Kitsune Network Attack Dataset. Accessed Nov. 29, 2021. [Online]. Available: h[ttps://www.kaggle.com/ymirsky/ network-attack-dataset-kitsune](https://www.kaggle.com/ymirsky/network-attack-dataset-kitsune)
68. KDD<a name="_page26_x85.04_y139.88"></a> Cup 1999 Data. Accessed Nov. 29, 2021. [Online]. Available: h[ttp://kdd.ics.uci.edu/ databases/kddcup99/kddcup99.html](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)
68. Y.<a name="_page26_x85.04_y172.76"></a> Mirsky, A. Shabtai, L. Rokach, B. Shapira, and Y. Elovici. Sherlock - smartphone malware dataset. Accessed Nov. 29, 2021. [Online]. Available: h[ttps://www.kaggle.com/BGU-CSRC/ sherlock](https://www.kaggle.com/BGU-CSRC/sherlock)
68. H.<a name="_page26_x85.04_y214.10"></a> Martin, Martin, B. V´aclav, and S. Pavol. Dataset of intrusion detection alerts from a sharing platform. Accessed Nov. 29, 2021. [Online]. Available: h[ttps://data.mendeley.com/datasets/ p6tym3fghz/1](https://data.mendeley.com/datasets/p6tym3fghz/1)
68. V.<a name="_page26_x85.04_y260.43"></a> Sv´ˇ abensky,´ J. Vykopal, P. Seda, and P. Celeda.ˇ Dataset: Shell Commands Used by Participants of Hands-on Cybersecurity Training. Accessed Nov. 29, 2021. [Online]. Available: <https://zenodo.org/record/5137355#.YaRYoJFBxhF>
68. V.<a name="_page26_x85.04_y304.27"></a> Valeros. Hornet: Network Dataset of Geographically Placed Honeypots. Accessed Nov. 29, 2021. [Online]. Available: h[ttps://www.stratosphereips.org/ hornet-network-dataset-of-geographically-placed-honeypots](https://www.stratosphereips.org/hornet-network-dataset-of-geographically-placed-honeypots)
68. R.<a name="_page26_x85.04_y347.55"></a> Roberto and L. R. Jose. Security Datasets (Mordor). Accessed Nov. 29, 2021. [Online]. Available: <https://github.com/OTRF/Security-Datasets>
26

[ref1]: Aspose.Words.91fd896a-5dd5-4ed9-9698-3f8fc222ecaf.001.png

