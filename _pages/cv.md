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
<!-- TODO(Ayush): replace the placeholder below with your real degrees, newest first -->
* Degree in Field, University Name, Year

Work & research experience
======
<!-- TODO(Ayush): replace the placeholder below with your positions, newest first -->
* Role, Institution/Company, Period
  * Brief description of what you did or achieved.

Skills
======
* **Machine learning:** linear/ridge/lasso & polynomial regression, decision trees, random forest, gradient boosting (XGBoost, GBR), AdaBoost, KNN, SVM
* **Data science:** PCA & dimensionality reduction, feature engineering, model evaluation (R², MSE, RMSE, MAE)
* **Programming & tools:** Python, Jupyter notebooks, pandas, scikit-learn
<!-- TODO(Ayush): add anything else, e.g. C/C++, MATLAB, SQL, AutoCAD, LaTeX -->

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
