---
title: "Bayesian Erosion Model with Low-Temperature Thermochronology"
excerpt: "User Guide to Run the Code<br/><img src='/images/My_DP_Prayoga.JPG'>"
collection: 
---

# Installation
(May 2024) by Biraj and Divydeep 

Bayesian erosion model Avdeev et al., (2011) (EPSL) has been modified for generating data presented in Borgohain et al., (2024). 
Folllwing documentation describes: (1) Procedure to run the code and (2) Modification to include ZFT simulation, extract results to ploting output graph in python. 
Original Avdeev et al., (2011) can be downloaded from link 

               https://code.google.com/archive/p/thermochron/downloads

# Procedure to run the code: 

     For Ubuntu 20.04.6 LTS, 64 bits steps followed
1. Creat an environment using (example py2)


         Bayesian_detrital_env.yml
2. Note python environment has to be in

        python 2.7 (specifically version python=2.7.18)
3. Install 

        pymc (specifically version pymc==2.3.8)
         
4. To install pymc visit the website

        https://pymcmc.readthedocs.io/en/latest/INSTALL.html
5. Installing from Anaconda

        https://anaconda.org/pymc
6. In terminal inside the envrionment (py2)

        $ conda install pymc::kabuki
7. To check for installation of pymc

        $ python
        >>> import pymc
        >>>
8. Go to detrital_ui folder

        Open terminal
9. Activate the conda environment (for example py2)

      
        $ conda activate py2   
10. Then

        python run.py
11. Done


# Input files
# Input parameter
