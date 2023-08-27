---
title: 'Week one (May 29, 2023 - Jun 5, 2023)'
collection: gsoc
---

This is the first week of my GSoC journey.

GSoC project
=================
*  [GSoC project URL](https://summerofcode.withgoogle.com/programs/2023/projects/HKW6ydaI)
*  [Work Repository](https://github.com/Mustardburger/CellBox)

Tasks
=================
1. Set up CellBox for easy development and debugging
I have several choices of setting up CellBox:
* Google Colab: CellBox's official repo has a demo Colab Notebook of how to run the model. I was able to run the notebook successfully. However, Colab Notebook is not suitable for development and prototyping: every time I make changes to the **.py** files in the cloned repo, I need to restart the notebook for the changes to take effect. This is very time-consuming.
* Binder: CellBox's repo also has a Binder to run code, although it suffers from the same cons as Colab. Also, version control of my changes to CellBox repo with Git on Colab and Binder is also very inconvenient.
* Personal computer: I can `git clone` the whole CellBox repo to my PC, run my code there, and `git push` my local changes to my fork. Everything will work great, except on my PC I will have to install Anaconda, then all the Python packages needed for CellBox. Tensorflow and Pytorch are very heavy.
* Computer cluster: I'm a university student, so I have access to my school's computer cluster. This resource is not available for everyone, but for me it is the best option: I can `git clone` the repo and make changes and push it back to remote just like with my PC, but now the cluster offers much more memory to install packages.

Relevant issues:
================
* CellBox apparently requires Python 3.8, not Python 3.6 as specified in the repo. Check my Google Doc notebook for more details.

Notes
=================
Check out my [personal GSoC notebook](https://docs.google.com/document/d/1fYkUNYuRcPHByWUYay6yUeTKtBuiwTGKJoztT0LajiA/edit?usp=sharing), where I keep my observations and comments in one place.
