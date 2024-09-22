---
title: "Bayesian Erosion Model with Low-Temperature Thermochronology"
excerpt: "From detrital age to erosion history: A user guide to run Bayesian Erosion Model  <br/><img src='/images/web_bayes_3.png'> "
collection: 
---



Results of **Bayesian erosion modeling** of detrital fission-track thermochronometric ages are demonstrated in Borgohain et al. (2024, under review in Tectonics) that utilized a Bayesian erosion model developed by Avdeev et al. (2011). 

The following documentation describes: 
1. Overview of running the **Bayesian erosion model** of Avdeev et al. (2011)
2. Configuring a model (Will be uploaded soon)
3. Details about code options (Will be uploaded soon). 

Original Avdeev et al. (2011) can be downloaded from a link [click here](https://code.google.com/archive/p/thermochron/downloads). 

It contains two main folders: 
1. ```data```
2. ```detrital_ui```.

# Overview of the Bayesian erosion model
## Input files

1. Code files (Included in ```detrital_ui``` folder)
     1.  <span style="font-size:18px; color:green"> Python files</span> (```.py```): ``` common.py```, ```data_type.py```, ```model_setup.py```, ```plot.py```, and ```run.py```
 
2. Input data file (Included in ```data``` folder)
   1. Age file ```.csv``` in the following formate (only age)
      ```python
          27.0
          13.7
          11.7
          14.2
          9.4
          6.9
           .
           .  
      ```
   3. DEM file ```.xyz``` in the following format (latitude, longitude, elevation).
      ```python
           x y z 
          217623.033 3251932.988 5165
          217653.033 3251932.988 5167
          217683.033 3251932.988 5168
           . . .
           . . .
      ```

## Set up used

1. Ubuntu 20.04.6 LTS, 64 bits
2. Conda environment was created (for example # ```py2```) and activated 
3. Python 2.7 (specifically version python=2.7.18) installed
4. numpy (version 1.16.6), matplotlib (1.5.0) installed along with required libraries. Other libraries detail can be found in file called ``` Bayesian_detrital_env.yml ```, [link is here](https://github.com/birajborgohain/Detrital-Thermochron-Avdeev-et-al.-2019/tree/main)
5. Pymc (version - 2.3.8) installed, link for details is [here](https://pymcmc.readthedocs.io/en/latest/INSTALL.html)
    1. ``` conda install pymc::kabuki ``` was used to install in a anaconda environment
    2. Check for installation of ```pymc```
         ```python
         $ python
        >>> import pymc
        >>>
         ```


## Running a model

1. Open a terminal in a folder containing code files of the Bayesian erosion model and activate the environment ```py2``` 
2. Run the code by typing ```python run.py``` and then click ```enter```
  

## Output files
 
 1. Done, model output contains:
    1. Simulated age-elevation plot, a ```.png ``` file (summary.png)
    2. Goodness of fit test plot, a ```.png``` file (KS_test.png)
    3. A ```.csv``` file (statistics.csv) containing: 
       1. Erosion rates (mm/yr) ```e1```, ```e2```, ```e3```,...
       2. Age of erosion rate change  (Ma) ```abr1```, ```abr2```,...

# References

Avdeev, B., Niemi, N. A., & Clark, M. K. (2011). Doing more with less: Bayesian estimation of erosion models < with detrital thermochronometric data. Earth and Planetary Science Letters, 305(3–4), 385–395. < https://doi.org/10.1016/j.epsl.2011.03.020

Borgohain, B., Mathew, G., Salvi, D., Harbola, D., Rai, P., (2024). Spatial and Temporal Variation of Erosion Rate      of the Lohit Bomi-Chayu Batholith around Eastern Himalayan Syntaxis (Southeast of Namche Barwa massif), (Under      Review in Tectonics)



