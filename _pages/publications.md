---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

* **A General Framework for Account Risk Rating on Ethereum: Toward Safer Blockchain Technology**  
**Qishuang Fu**, Dan Lin, Jiajing Wu, and Zibin Zheng  
IEEE Transactions on Computational Social Systems (TCSS),2023  
[ [<font color="red">Paper</font>](https://ieeexplore.ieee.org/abstract/document/10097741) ]  [ [<font color="red">Code</font>](https://github.com/fuqishuang228/Risk-Rating_Framework) ] [ [<font color="red">Data</font>](https://www.dropbox.com/scl/fo/naxj68ft8zbl0ssry6128/h?dl=0&rlkey=53tqxfjfs6mtc1cwxnty7okv5) ]
  
  <img src="https://raw.githubusercontent.com/fuqishuang228/fuqishuang228.github.io/master/images/Fig_framework.png" width="80%" align="center">

* **Does Money Laundering on Ethereum Have Traditional Traits?**  
**Qishuang Fu**, Dan Lin, Yiyue Cao, and Jiajing Wu  
IEEE International Symposium on Circuits and Systems (ISCAS),2023  
[ [<font color="red">Paper</font>](https://arxiv.org/abs/2303.15841) ] [ [<font color="red">Code</font>](https://github.com/fuqishuang228/ETH_ML_Traits_Analysis/tree/main) ] [ [<font color="red">Data</font>](https://www.dropbox.com/scl/fo/t2ynpos4l2grq383cexnc/h?dl=0&rlkey=wuj0kvzgdu9objp9lvsf66jml) ]

  <img src="http://fuqishuang228.github.io/images/ML.png" width="80%" align="center">
{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
