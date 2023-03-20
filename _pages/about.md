---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---


My research interests encompass healthcare machine learning systems and general artificial intelligence🧠🤖. I envision creating a learning system as efficient and effective as, or surpassing, human capabilities. During my PhD, I conducted extensive research on radiologists' eye-tracking, believing that incorporating the information found in a human expert's reasoning process is crucial for training neural networks.

I am also fascinated by neuroscience, computer graphics, hardware circuit design, and internal combustion engines, I have yet to become an expert in these fields😢.

I am curretnly a PhD candidate at Shanghai Jiao Tong University, supervised by [Prof. Dinggang Shen](http://idea.bme.shanghaitech.edu.cn) and [Prof. Qian Wang](https://qianwang.space). 
Prior to this, I completed my BS degree from Northeastern University (Shenyang, China) and Chinese Academy of Sciences (Shenzhen Institute of Advanced Technology) in 2015. In my free time, I enjoy programming⌨️ (Currently ![Github stars](https://img.shields.io/github/stars/jamesqfreeman?style=social) stars🌟), running🏃, swimming🏊, weightlifting🏋️, and motorsports🏁.


Computer Aided Diagnosis with Eye-tracking
======
Our motivation is straightforward: leveraging the eye movements of radiologists to improve computer-aided diagnosis. The collection of this data is a passive and unobtrusive process that captures informative supervision related to the radiologists' diagnostic procedures. 

First, let me show some cases we collected:
![This red circle will not show up in the normal collecting, just here for demo.](demo-2.gif)

1. To make sure the collected gaze are informative, we first use it as a network supervision during training. It is a pilot study that use gaze to improve deep-learning-based CAD sytem and is published at IEEE Trans on Medical Imaging at 2022. [[Paper](https://arxiv.org/abs/2204.02976)][[GitHub pages](https://jamesqfreeman.github.io/MicEye/)]. 
<img src="images/Follow_my_eye.png" alt="Gaze supervision" style="width:50%;">
Cite: Follow my eye: using gaze to supervise computer-aided diagnosis. 

**S Wang**, X Ouyang, T Liu, Q Wang, D Shen

2. After this worked, we apply this to a more complex task (mammography) and architecture (Vision Transformer). This work is submitted in IEEE Trans on Medical Imaging and is currently under major revision. [[Paper ] (https://arxiv.org/abs/2205.12466)].
![On vision transformer](vitGaze.png)
Cite: Eye-gaze-guided Vision Transformer for Rectifying Shortcut Learning. 

C Ma, L Zhao, Y Chen, L Zhang, Z Xiao, H Dai, D Liu, Z Wu, Z Liu, **S Wang**, ...

3. We extent gaze in the very foundamental part in computer vision, data augmentation. Our brains naturally and constantly augment images (e.g., by slightly shifting our gaze to view the same object from different angles). In our research, we investigated how we could improve current image augmentation techniques by mimicking the way humans use gaze. This work is submitted to IEEE Trans on Neural Networks and Learning Systems (2022.10). [[code ](https://jamesqfreeman.github.io/MicEye/contrastive_learning_example/)]
![Gaze in augmentation](focus_contrast.png)
Learning Better Contrastive View from Radiologist’s Gaze. 

**S Wang**, Z Zhuang, X Ouyang, L Zhang, Z Li, C Ma, T Liu, D Shen, Q Wang

4. We propose the idea of training a neural network solely on gaze information, as we believe gaze provides valuable insights for diagnostic tasks. Through our gaze collection process, we have observed that similar lesions often elicit similar gaze patterns. Therefore, we propose constructing a self-supervised system based on gaze similarity. This work is submitted to ICCV 2023.
![Self-supervision with Gaze](McGIP.png)
Mining Gaze for Contrastive Learning toward Computer-Assisted Diagnosis.

Z Zhao\*, **S Wang\*,** Q Wang, D Shen

New age with Foundation Model
======
I do think we are at the second research golden age for AI with LARGE transformers and webscale unsupervised pretraining. The first golden age are lead by ImageNet supervised pretrain and CNNs. As a 
1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
2. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
3. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
4. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
5. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
6. Check status by going to the repository settings, in the "GitHub pages" section

Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. You will need to replace the default variables with ones about yourself and your site's github repository. The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml). For example, if you don't have a portfolio or blog posts, you can remove those items from that navigation.yml file to remove them from the header. 

Create content & metadata
------
For site content, there is one markdown file for each type of content, which are stored in directories like _publications, _talks, _posts, _teaching, or _pages. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured data about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

**Markdown generator**

I have also created [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the academicpages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring academicpages can be found in [the guide](https://academicpages.github.io/markdown/). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful.
