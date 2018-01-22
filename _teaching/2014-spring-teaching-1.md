---
title: "Growing Tree Structured Cascade"
collection: teaching
permalink: /projects/2014-spring-teaching-1
startdate: 2017-June-01
startmonth: March
enddate: 2017-September-01
endmonth: September
mathjax: true
---

In this project we describe a way to determine the optimal tree structured cascade configuration.

## Cascading Architecture

In a general machine learning model, all the data points
are treated in the same way i.e. computationally every data point is the same with respect to the model. But for cascading architecture based upon the complexity of the data point its computation cost changes. This is achieved by using classifiers sequentially whose capacity increases gradually. ( 1< 2..< L)
{% include image.html url="/images/linearcascade.png" width=450 align="right" %}
An example $x$ is passed to next stage only if the current stage declared it as positive, if any stage declares $x$ as negative in the process it is outputted as negative. So, sample $x$ is declared as positive only if everystage in the cascade declares it as positive. Cascading architecture is mainly used for problems involving imbalanced datasets as most of the samples are classified in the early stages of the cascade and only the samples which are hard to classify are passed to final stages which take up most of the computational time. As  this percentage of hard samples is very less, overall run time is better with cascading architecture for these datasets. 

{% include image.html url="/images/probability_linearcascade.png" width=450 height=100 align="right" %}	
Here $P_{*}(y|\textbf{x})$ refers to the final output probability and $p_{l}$ represents probability of $l^{th}$ stage. $L$ being total number of stages. Informally, if a datapoint reaches $i^{th}$ stage that means all the stages from 1.. $i-1$ has classified it as 1, and suppose $i^{th}$ stage classified it as '0'. The final probability (apprx) is gonna be $p_{i}$

## Tree Structured Cascades
{% include image.html url="/images/treecascade.png" width=650 align="right" %}
 Tree structured architecture finds its usefulness in the field of mobile heath or mHealth. Wearable on-body sensing technologys have low computational power comparative to mobile devices, which makes it hard to run complex classifiers on wearable technologys. So, the information from these wearable devices is fed into mobile devices for computing. Recent work by [2] used tree structured architecture on health data, here they propose a way to jointly learn all the parameters by assuming some fixed configuration of the network. 
{% include image.html url="/images/treecascade_prob.png" width=450 height=100 align="right" %}	
 There are $D+1$ devices, with $D+1$ being the central node. $p_{*}^{d}$  the final output probability of $d^{th}$ device, $p_{l}^{D+1}$ is output probability of $l^{th}$ stage in central node. In this project I addressed this drawback by proposing a greedy stratergy in finding the optimal configuration of the network. The intuition behind this is whenever a stage is being added to the existing network it is added in such a way that the output remains unaltered i.e. newly added stage acts as neutral between old and new architecture. Due to the nature of the objective function the newly added stage parameters are same as previous stage parameters. Intuitively, if new stages intial parameters are same as previous last stage its going to pass test casses which are passed by previous last and its not going to reject any as the cases to be rejected are done by previous last stage. As the objective function of newly structure is different from old, after few iterations predictor function of newly added and previous last are going to change. If we had 'D+1' devices and planning to add 'M' stages without our method we had to try $(D+1)^{M}$ combinations and had  to pick the best configuration but with our greedy stratergy it will take $M$ $(D+1)$ try's. As number of devices is going to be constant ,we brought down the time complexity of the problem to linear.



## Results
The optimal tree structured configuration with respect to human activity recongnistion dataset  is  5 stages at Device 1, 5 stages at Device 2, 1 stage at Smartphone. Accuracy and F1 score correponding to this configuration are 0.9728 and 0.911.  The optimal term here refers to best accuracy. Optimal configuration with respect to smoking dataset  is 1 stages at Device 1, 1 stages at Device 2, 2 stage at Smartphone. Accuracy and F1 score correponding to this configuration are 0.984 and 0.881. For the baseline model we grow the network by randomly intializing the newly added stage parameters. For human activity recongnistion we get best  accuracy of 0.970 , corresponding F1 score 0.90. For smoking dataset we get best  accuracy   of 0.984, corresponding F1 score 0.881 on baseline model. 

## References
[1] Paul Viola and Michael Jones. Rapid object detection using a boosted cascade of simple features. In Computer Vision and Pattern Recognition, 2001. CVPR 2001. Proceedings of the 2001 IEEE Computer Society Conference on, volume 1, pages I–I. IEEE, 2001.

[2] Hamid Dadkhahi and Benjamin M Marlin.   Learning tree-structured detection cascades for heterogeneous networks of embedded devices.   InProceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pages 1773–1781. ACM,2017.

