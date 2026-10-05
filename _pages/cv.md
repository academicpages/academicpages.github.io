---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* **Ph.D. (ongoing)** — Centre of Studies in Resources Engineering (CSRE), IIT Bombay
<!-- Earlier degrees: add verified B.Tech/M.Tech degree, institution, and year when provided. -->

Work & research experience
======
* **Doctoral Researcher**, CSRE, IIT Bombay
  * Research interests: deep learning for remote sensing, quantum machine learning, computer vision, and foundation models.

Skills
======
* **Deep learning:** PyTorch, transformers, computer vision
* **Research applications:** remote sensing, foundation models
* **Machine learning:** linear/ridge/lasso & polynomial regression, decision trees, random forest, gradient boosting (XGBoost, GBR), AdaBoost, KNN, SVM
* **Data science:** PCA & dimensionality reduction, feature engineering, model evaluation (R², MSE, RMSE, MAE)
* **Programming & tools:** Python, Jupyter notebooks, pandas, scikit-learn
<!-- TODO(Ayush): add anything else, e.g. C/C++, MATLAB, SQL, AutoCAD, LaTeX -->

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
