---
title: "Bayesian Erosion Model with Low-Temperature Thermochronology"
excerpt: "User Guide to Run the Code "
collection: 
---



Simulation presented in Borgohain et al., (2024) uses Bayesian erosion model of Avdeev et al., (2011) (EPSL) has been. 
Folllowing documentation describes: (1) Procedure to run the model and (2) modification to include ZFT simulation, and to extract model output for ploting in Jupyter. Original Avdeev et al., (2011) can be downloaded from a link [click here](https://code.google.com/archive/p/thermochron/downloads). 

# Over view of Bayesian erosion model
# Input files

1. Code file
     1. ``` <span style="font-size:38px; color:green"> This is some text </span> ```
     2. $ \begin{pmatrix} a & b \\ c & d \end{pmatrix} $
2. Input data dile
   1. Age file ```.csv```
      ```python
           <span style="font-size:18px; color:green">This is some text</span>
      ```
   3. DEM file ```.xyz```

# Set up used

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


# Start simulating

1. Open a terminal in a folder containing code file of Bayesian erosion model and activate the environment ```py2``` 
2. Run the code by typing and then click ```enter```
    ```python
        python run.py
    ```

 
 # Output files
 
 1. Done, model out contains
    1. Simulated age-elevation plot
    2. Goodness of fit test plot
    3. ```.csv``` file conating
       1. Erosion rates (mm/yr) ```e1```, ```e2```, ```e3```,...
       2. Age of erosion rate change  (Ma) ```abr1```, ```abr2```,...
 
         


