---
layout: archive
title: "Project"
permalink: /projects/
author_profile: true
redirect_from:
  - /projects
  - /projects.html
---

{% include base_path %}

DGEMM on Cori KNL Node (C++, AVX2, AVX512)
------
[Link to github repo](https://github.com/lix19937/dgemm-knl)
* Implement DGEMM on Intel Cori Node. Achieve average of 75% MKL performance on single core.
* Use AVX512 inline assembly for embedded broadcast, increase theoratical peak from 22.4 to 44.8 GFLOPs.
* Mix use of AVX2 & AVX512 for 8x8 matrix transpose, reduce the pressure on load port. Incr 0.4% peak perf.




Search Engine from Scratch (C++)
------
* Mainly responsible for search engine back-end: webpage crawler and HTML parser.
* Implement our STL string, vector, map, priority queue.
* Use pthread, OpenSSL, and socket to implement multi-machine multi-thread crawler that supports download prioritized web pages, remove duplicated web pages, handling URL redirection, and support IPv4 & IPv6 download at the same time.
* Implement HTML parser to extract URL links, anchor text, title, and body from HTML. Our parser can handle more corner cases than Python 3 html.parser.



PicassoXS: IOS Photo Editing APP that Change Photo to Painting (Python, Tensorflow)
------
[Link to github repo](https://github.com/lix19937/PicassoXS)
* Mainly responsible for the back-end CNN model building and deployment, backend server, algorithm research and implementation.
* Algorithm: compared various style transfer algorithms. Combined ideas from multiple algorithms to deal with the trade-offs between algorithm visual effect, computing time, and hardware consumption. The final model can process 512^2 image on 8 CPU instance within 4s. 
* Back end: Use tensorflow to build CNN model, train the model, and deploy the model service to Google Cloud through TF server, Docker and K8S. Use Python, Flash to implement RESTful API to receive IOS requests, call corresponding model services, and return processed photos to IOS.




