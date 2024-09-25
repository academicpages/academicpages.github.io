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

<span style="font-size:18px; color:red"> Downloaded file</span>  contains two main folders: 
1. ```data```
2. ```detrital_ui```.

# Overview of the Bayesian erosion model
## Input files

1. Create a folder with a sample name (for example <span style="font-size:18px; color:green"> ANIDT4</span>)
2. In <span style="font-size:18px; color:green"> ANIDT4</span> create another two folder with name ```data``` and ```detrital_ui```.
3. Upload two input data files in ```data``` folder of <span style="font-size:18px; color:green"> ANIDT4</span>
     1. Age file ```.csv``` in the following formate (detrital cooling age distribution of sample <span style="font-size:18px; color:green"> ANIDT4</span>)
      ```bash
          27.0
          13.7
          11.7
          14.2
          9.4
          6.9
           .
           .  
      ```
      2. DEM file ```.xyz``` in the following format (latitude-x, longitude-y, elevation of catchment-z <span style="font-size:18px; color:green"> ANIDT4</span>).
      ```bash
           x y z 
          217623.033 3251932.988 5165
          217653.033 3251932.988 5167
          217683.033 3251932.988 5168
           . . .
           . . .
      ```
4. Copy code files from the ```detrital_ui``` folder of <span style="font-size:18px; color:red"> Downloaded file</span> , and then paste these in <span style="font-size:18px; color:green"> ANIDT4</span>'s ```detrital_ui``` folder. Specifically following files:
     1.  <span style="font-size:18px; color:blue"> Python files</span> (```.py```): ``` common.py```, ```data_type.py```, ```model_setup.py```, ```plot.py```, and ```run.py```


## Set up used

1. Ubuntu 20.04.6 LTS, 64 bits.
2. Conda environment was created (for example ```py2```) and activated.
3. In ```py2``` environment following packages and libraries are installed
   1. Python 2.7 (specifically version python=2.7.18) installed
   2. numpy (version 1.16.6), matplotlib (1.5.0) installed along with required libraries. Other libraries detail can be found in file called ``` Bayesian_detrital_env.yml ```, [link is here](https://github.com/birajborgohain/Detrital-Thermochron-Avdeev-et-al.-2019/tree/main)
   3. *Pymc* (version - 2.3.8) installed, a link for details is [here](https://pymcmc.readthedocs.io/en/latest/INSTALL.html)
      1. ``` conda install pymc::kabuki ``` code was used to install *PyMc*
      2. Check for installation of ```pymc```
         ```bash
         $ python
        >>> import pymc
        >>>
         ```


## Running a model

1. Open a terminal in the folder (```detrital_ui```) of <span style="font-size:18px; color:green"> ANIDT4</span> containing code files (i.e., <span style="font-size:18px; color:blue"> Python files</span>) of the Bayesian erosion model and activate the environment ```py2``` 
2. Run the *Bayesian erosion model* by typing ```python run.py``` and then click ```enter```
  

## Output files
 
 1. Done, model output contains:
    1. Simulated age-elevation plot, a ```.png ``` file (summary.png)
    2. Goodness of fit test plot, a ```.png``` file (KS_test.png)
    3. A ```.csv``` file (statistics.csv) containing: 
       1. Erosion rates (mm/yr) ```e1```, ```e2```, ```e3```,...
       2. Age of erosion rate change  (Ma) ```abr1```, ```abr2```,...
          
# Configuring a model

<span style="font-size:18px; color:red"> Download file</span>'s ```model_setup.py``` file is used primarily to configure the model for a sample for various erosion history scenarios (here example sample is <span style="font-size:18px; color:green"> ANIDT4</span>). 
1. To model **uniform erosion history scenario**, which refers to constant erosion rate through time, the following changes are required in ```model_setup.py```, this can be done by editing class and variables in the ```model_setup.py``` :
   1. Assign DEM file location and file name, for example, DEM file name is ```ANIDT4.xyz```
      ```bash
      catchment_1 = Catchment(hypsometry_file = "../data/ANIDT4.xyz", elevation_column = 'z')
      ```
   2. Assign age file location, sample name, catchment data (```catchement_1```), thermochronometric type (```AFT```), for example, the age file name is ```ANIDT4.csv```
      ```bash
      sample_1 = DetritalSample(age_file = "../data/ANIDT4.csv", sample_name = 'ANIDT4', catchment = catchment_1, tc_type = 'AFT')

      ```
   3. Assign the range of the erosion rate that the sample would have experienced, for example, from ```0 to 3``` mm/yr for <span style="font-size:18px; color:green"> ANIDT4</span> sample. This is based on previous studies around the sample location, or it can be a guess. The minimum and maximum values are required. In ```model_setup.py``` file this is coded as ```erate_prior = (0,3)```.
   4. Assign a range of the timing of a change in erosion rate that would have experienced, for example, from ```0 to 60``` Ma for <span style="font-size:18px; color:green"> ANIDT4</span> sample. This is the second prior that we can assign minimum and maximum ages from the measured age distribution of <span style="font-size:18px; color:green"> ANIDT4</span>.  In ```model_setup.py``` file this is coded as ```abr_prior = (0,60)```.
   5. Assign a number of breaks in the exhumation model; in this uniform erosion history scenario, the break will be zero. In ```model_setup.py``` file this is coded as ```break = 0```.
     
2. To model **non-uniform erosion rate scenario**, which refers to variation in erosion rates through time, only the number of break parameters needed to be changed, other parameters are kept the same as described in **uniform erosion rate scenarios**. Thus, the only line of code that is required to change is the value in ```break=  ```. Here, ```break= 1``` for the one-break scenario refers to one discrete change in erosion rates through time, and ```break= 2``` for the two-break refers to two discrete changes in erosion rate through time.
3. The best model scenario (whether zero-break, one-break, or two-break) is evaluated by comparing the cumulative probability distribution of modeled ages and measured ages using a goodness-of-fit plot that displays the results of Kolmogorov-Smirnov test. An overlap of these two data suites indicates an acceptable model fit. For example, the below plot (which will be uploaded soon) displays a degree of overlap between these two; it is shown using the cumulative probability plots of measured AFT (orange dots) and swaths of modeled AFT (blue) ages. Here, the p-value is used to select the best model; it refers to the probability of getting model results close to observed results and the acceptable fitting criteria considered in this example is p >0.05. 
   
# References

- *Avdeev, B., Niemi, N. A., & Clark, M. K.* (2011). **Doing more with less: Bayesian estimation of erosion models with detrital thermochronometric data.** Earth and Planetary Science Letters, 305(3–4), 385–395. https://doi.org/10.1016/j.epsl.2011.03.020


- *Borgohain, B., Mathew, G., Salvi, D., Harbola, D., Rai, P.,* (2024). **Spatial and Temporal Variation of Erosion Rate of the Lohit Bomi-Chayu Batholith around Eastern Himalayan Syntaxis (Southeast of Namche Barwa massif),** (Under Review in Tectonics)





