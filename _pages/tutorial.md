---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/
title: "Tutorial"
permalink: /tutorial/
author_profile: true
title: "Tutorial at SIGIR 2023: Explainable Information Retrieval"
event: SIGIR 2023
event_url: "https://sigir.org/sigir2023/"
location: "Taipei(SIGIR)"
address:
  street:
  city:
  region:
  postcode:
  country:
summary: "Explainable Information Retrieval"
abstract: "This tutorial presents explainable information retrieval (ExIR), an emerging area focused on fostering responsible and trustworthy deployment of machine learning systems in the context of information retrieval. As the field has rapidly evolved in the past 4-5 years, numerous approaches have been proposed that focus on different access modes, stakeholders, and model development stages. This tutorial aims to introduce IR-centric notions, classification, and evaluation styles in ExIR, while focusing on IR-specific tasks such as ranking, text classification, and learning-to-rank systems. We will delve into method families and their adaptations to IR, extensively covering post-hoc methods, axiomatic and probing approaches, and recent advances in interpretability-by-design approaches. We will also discuss ExIR applications for different stakeholders, such as researchers, practitioners, and end-users, in contexts like web search, patent and legal search, and high-stakes decision-making tasks. To facilitate practical understanding, we will provide a hands-on session on applying ExIR methods, reducing the entry barrier for students, researchers, and practitioners alike.
"

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2023-07-22T9:00:22+02:00
date_end: 2023-07-22T12:30:22+02:00
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: 2020-07-19T14:47:22+02:00

authors: [Avishek Anand]
tags: []

# Is this a featured talk? (true/false)
featured: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

# Optional filename of your slides within your talk's folder or a URL.
url_slides: "https://arxiv.org/pdf/2211.02405.pdf"

url_code:
url_pdf: "https://arxiv.org/pdf/2211.02405.pdf"
url_video: ""

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---
This half-day tutorial is divided into two parts of 90 minutes each -- In the first part we explore the notions of explainable IR, probing neural models and explainable-by-design approaches. In the second half, we delve deeper into axiomatic IR and its connection to interpretability and some of the popular posthoc approaches. 

<br>

## Contents

 1. **[Full Slides](https://shorturl.at/fhrDH)**. 
 2. **[Notions of Explainable IR](https://shorturl.at/apHJ8)** by [Avishek Anand](http://www.avishekanand.com). 
 3. **[Intrinsic Methods for ExIR](https://shorturl.at/dnrGW)** by [Avishek Anand](http://www.avishekanand.com). 
 4. **[Probing transformer models](https://shorturl.at/dnrGW)** by [Avishek Anand](http://www.avishekanand.com).
 
 <br>    

 5. **[Posthoc approaches in ExIR](https://shorturl.at/pyBM1)** by [Procheta Sen](https://procheta.github.io/sprocheta/).
 6. **[Axiomatic IR for Interpretability](https://shorturl.at/hzKR8)** by [Sourav Saha](https://souravsaha.github.io).
 7. **[Outlook and Conclusion](https://shorturl.at/biK03)** by [Avishek Anand](https://www.avishekanand.com).

<br>

## Notebooks

1. [Intent rerank](https://www.dropbox.com/scl/fi/58i4p3q39yr4l1z5xrds1/demo_1_intent_rerank.html?rlkey=i4q2103pvvcqr2yinjs8lb863&dl=0)
2. [Exs rerank](https://www.dropbox.com/scl/fi/wyvea8721ns6ag64k4s10/demo_2_exs_rerank.html?rlkey=mhlrq0rwnsh8y9v7g733voni3&dl=0)
3. [Axiomatic](https://www.dropbox.com/scl/fi/lyb9l4ufnvlq9pfuhc6fk/demo_3_axiomatic.html?rlkey=qbaooi04fgyg1dd3ixx6ax4hv&dl=0)

---
## References

<br>

[1] "Sanity Checks for Saliency Maps", Adebayo et al., NeurIPS 2018. 

[2] "LIRME: Locally Interpretable Ranking Model Explanation", Verma and Ganguly, SIGIR 2019.

[3] "The Curious Case of IR Explainability: Explaining Document Scores
within and across Ranking Models", Sen et al., SIGIR 2020.

[4] "Model agnostic interpretability of rankers via intent modelling", Singh and Anand, FAT 2020.

[5] "Listwise Explanations for Ranking Models Using Multiple Explainers", Lyu et al., ECIR 2023.

[6] "Query Understanding via Intent Description Generation", Zhang et al., CIKM 2020.

[7] "A formal study of information retrieval heuristics", Fang et al., SIGIR 2004.

[8] "Axiomatic Result Re-Ranking", Hagen et al., CIKM 2016.

[9] "Aggregating inconsistent information: Ranking and clustering", Ailon et al., JACM 2008.

[10] "Explainable k-Means and k-Medians Clustering", Dasgupta et al., ICML 2020.

[11] "Towards Axiomatic Explanations for Neural Ranking Models", Volske et al., ICTIR 2021.

[12] "An Axiomatic Approach to Diagnosing Neural IR Models", Rennings et al., ECIR 2019.

[13] "Diagnosing BERT with Retrieval Heuristics", Camara and Hauff, ECIR 2020.








