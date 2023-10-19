---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}


* **Su, Z.**, Tavolara, T. E., Carreno-Galeano, G., Lee, S. J., Gurcan, M. N., & Niazi, M. K. K. (2022). Attention2majority: Weak multiple instance learning for regenerative kidney grading on whole slide images. Medical Image Analysis.
* **Su, Z.**, Niazi, M. K. K., Tavolara, T. E., Niu, S., Tozbikian, G. H., Wesolowski, R., & Gurcan, M. N. (2023). BCR-Net: A deep learning framework to predict breast cancer recurrence from histopathology images. Plos one.
* **Su, Z.**, Kumar, S., Tavolara, T. E., Gurcan, M. N., Segal, S., & Niazi, M. K. K. (2023). Predicting obstructive sleep apnea severity from craniofacial images using ensemble machine learning models. In Medical Imaging 2023: Computer-Aided Diagnosis. SPIE.
*	**Su, Z.**, Rezapour, M., Sajjad, U., Gurcan, M. N., & Niazi, M. K. K. (2023). Attention2Minority: A salient instance inference-based multiple instance learning for classifying small lesions in whole slide images. Computers in Biology and Medicine.
* Tavolara, T. E., **Su, Z.**, Gurcan, M. N., & Niazi, M. K. K. (2023). One label is all you need: Interpretable AI-enhanced histopathology for oncology. Seminars in Cancer Biology.
* Sajjad, U., Rezapour, M., **Su, Z.**, Tozbikian, G. H., Gurcan, M. N., & Niazi, M. K. K. (2023). NRK-ABMIL: Subtle Metastatic Deposits Detection for Predicting Lymph Node Metastasis in Breast Cancer Whole-Slide Images. Cancers.

Papers under review
======
* **Su, Z.**, Rezapour, M., Sajjad, U., Niu, S., Gurcan, M. N., & Niazi, M. K. K. (2023). Cross-attention-based multiple instance learning with saliency inference for predicting cancer metastasis on whole slide images. arXiv preprint arXiv:2309.09412.