---
title: "Bayesian Erosion Model with Low-Temperature Thermochronology"
excerpt: "User Guide to Run the Code "
collection: 
---



Simulation presented in Borgohain et al., (2024) uses Bayesian erosion model of Avdeev et al., (2011) (EPSL) has been. 
Following documentation describes: (1) over view of running Bayesian erosion model and (2) modification to include ZFT simulation, and to extract model output for ploting in Jupyter. Original Avdeev et al., (2011) can be downloaded from a link [click here](https://code.google.com/archive/p/thermochron/downloads). It contains two main folders: 1. ```data```, 2. ```detrital_ui```.

# Over view of Bayesian erosion model
## Input files

1. Code files (Included in ```detrital_ui``` folder)
     1.  <span style="font-size:18px; color:green"> Four python ```.py``` files: </span> ``` common.py```, ```data_type.py```, ```model_setup.py```, ```plot.py```, and ```run.py```
 
2. Input data file (Included in ```data``` folder)
   1. Age file ```.csv``` in the following formate (only age)
      ```python
           27
          13.7
          11.7
          14.2
          9.4
          6.9
           .
           .  
      ```
   3. DEM file ```.xyz``` in the following formate (latitude, longitude, elevation).
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
    1. ``` conda install pymc::kabuki ``` was used to install in a anconda environment
    2. Check for proper installation of pymc
         ```python
         $ python
        >>> import pymc
        >>>
         ```


## Start simulating

1. Open a terminal in a folder containing code file of Bayesian erosion model and activate the environment ```py2``` 
2. Run the code by typing ```python run.py``` and then click ```enter```
  

## Output files
 
 1. Done, model output contain
    1. Simulated age-elevation plot, a .png file (summary.png)
    2. Goodness of fit test plot, a .png file (KS_test.png)
    3. ```.csv``` file contaning (statistics.csv)
       1. Erosion rates (mm/yr) ```e1```, ```e2```, ```e3```,...
       2. Age of erosion rate change  (Ma) ```abr1```, ```abr2```,...
 
         


