---
permalink: /
title: "Ze Rong | AI for Medical Imaging, Sports Analytics, and Representation Learning"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---


Hi! I’m **Ze Rong (荣泽)**, an undergraduate researcher (BSc in Computer Science, *Nantong University*) focusing on **AI for biomedical data**, **representation learning across modalities and scales**, and **soccer analytics**. My work blends solid engineering with method design, emphasizing **frequency-aware modeling**, **reconstruction-aided training**, and **multimodal alignment** for robust generalization.

- **Email:** <ZeRong7777@gmail.com>  
- **GitHub:** <https://github.com/ZeRong7777>  
- **CV:** [PDF (latest)](/files/CV_rz.pdf)

---

## Research interests
- **Medical imaging:** frequency-domain segmentation, reconstruction-aided learning, small-sample/low-SNR regimes  
- **Cross-modal & cross-scale representation:** token-level alignment, curriculum/adaptation, reliability-aware fusion  
- **Sports analytics (soccer):** team affect & tactics, spatio-temporal graph models, broadcast audio/commentary fusion

---

## News & highlights
- **Oct 2025** — *FaRMamba* accepted to **ICONIP 2025** (frequency-based learning + reconstruction-aided Vision-Mamba for medical segmentation).  
- **2025** — *FIRM* accepted to **ACML 2025** (token-level alignment for unsupervised VI-ReID with prompt fusion + evolving memory).  
- **Apr 2025** — **CN119762378A** invention patent published: unsupervised blind super-resolution & denoising for low-quality medical images.  
- **2024** — *JMIR* systematic review on AI for acute stroke diagnosis published.

> See more in [Publications](/publications/) and [Talks](/talks/).

---

## Selected publications
**FaRMamba: Frequency-based Learning and Reconstruction-Aided Mamba for Medical Segmentation** (ICONIP 2025)  
**FIRM: Fusion-Injected Residual Memory Brings Token-Level Alignment to Unsupervised VI-ReID** (ACML 2025)  
*Plus a JMIR 2024 systematic review and additional works; full list on the* [Publications](/publications/) *page.*

> Tip: Add each paper as a Markdown item in `_publications/` to enable the automatic publication list, per-paper pages, and BibTeX.

---

## Projects (engineering)
- **3D Medical Image Interactive Analysis Platform**  
  nnU-Net + axial PS attention; VTK.js/ITK.js visualization (3D tools, measurement, interaction).
- **Ophthalmic Disease Diagnosis Platform**  
  EfficientNet-V2 with vessel topology cues, HSV enhancement, CSRA; Vue + ElementUI full-stack web app.

---

## Awards
- China Robot and Artificial Intelligence Competition (CRAIC) **2025 National Second Prize**  
- CRAIC **2024 National First Prize**  
- Chinese Collegiate Computing Competition **2024 National Second Prize**

---

## Get started / site notes
This site is built with the **Academic Pages** template (Jekyll + GitHub Pages).  
- Update global settings in [`_config.yml`](/_config.yml) and menu in [`_data/navigation.yml`](/_data/navigation.yml).  
- Add publications to `_publications/`, talks to `_talks/`, posts to `_posts/`, and custom pages to `_pages/`.  
- Put files (e.g., PDFs) in `/files/` and link as `/files/your_file.pdf`.

*Last updated: {{ "now" | date: "%b %d, %Y" }}*

Getting started
======
1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this template](https://github.com/academicpages/academicpages.github.io) by clicking the "Use this template" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](https://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section

Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. You will need to replace the default variables with ones about yourself and your site's github repository. The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml). For example, if you don't have a portfolio or blog posts, you can remove those items from that navigation.yml file to remove them from the header. 

Create content & metadata
------
For site content, there is one Markdown file for each type of content, which are stored in directories like _publications, _talks, _posts, _teaching, or _pages. For example, each talk is a Markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each Markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured data about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

**Markdown generator**

The repository includes [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual Markdown files that will be properly formatted for the Academic Pages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the Markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and Markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a Markdown file for a talk
![Editing a Markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring Academic Pages can be found in [the guide](https://academicpages.github.io/markdown/), the [growing wiki](https://github.com/academicpages/academicpages.github.io/wiki), and you can always [ask a question on GitHub](https://github.com/academicpages/academicpages.github.io/discussions). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful.
