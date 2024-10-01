---
title: "Bayesian Erosion Modeling for inversion of detrital Low-Temperature Thermochronometric ages"
excerpt: "From detrital age to erosion history: A user guide to run Bayesian Erosion Model  <br/><img src='/images/web_bayes_3.png'> "
collection: 
---



Results of **Bayesian erosion modeling** for inversion of detrital fission-track thermochronometric ages are demonstrated in Borgohain et al. (2024, under review in Tectonics) that utilized a Bayesian erosion model developed by Avdeev et al. (2011). 

The following documentation describes: 
- Overview of running the **Bayesian erosion model** of Avdeev et al. (2011)
- Configuring a model 
- Details about code options (Will be uploaded soon). 



# Overview of the Bayesian erosion modeling in Python

## Installation and computer setup
1. Original Avdeev et al. (2011) can be downloaded from a link [click here](https://code.google.com/archive/p/thermochron/downloads). <span style="font-size:18px; color:red"> Downloaded file</span>  contains two main folders: 
   - ```data```
   - ```detrital_ui```.
2. The simulation is carried out in Ubuntu 20.04.6 LTS, 64 bits.
3. Conda environment was created (for example ```py2```) and activated.
4. In ```py2``` environment following packages and libraries are required to run Avdeev et al. (2011) Bayesian erosion model 
   - Python 2.7 (specifically version python=2.7.18) installed
   - numpy (version 1.16.6), matplotlib (1.5.0) installed along with required libraries. Other libraries detail can be found in file called ``` Bayesian_detrital_env.yml ```, [link is here](https://github.com/birajborgohain/Detrital-Thermochron-Avdeev-et-al.-2019/tree/main)
   - *Pymc* (version - 2.3.8) installed, a link for details is [here](https://pymcmc.readthedocs.io/en/latest/INSTALL.html)
      - ``` conda install pymc::kabuki ``` code was used to install *PyMc*
      - Check for installation of ```pymc```
         ```
         $ python
        >>> import pymc
        >>>
         ```
___

*Start*

## Input files

1. Create a folder with a sample name (for example <span style="font-size:18px; color:green"> ANIDT4</span>)
2. In <span style="font-size:18px; color:green"> ANIDT4</span> create another two folder with name ```data``` and ```detrital_ui```.
3. Upload two input data files in ```data``` folder of <span style="font-size:18px; color:green"> ANIDT4</span>
     - Age file ```.csv``` in the following formate (detrital cooling age distribution of sample <span style="font-size:18px; color:green"> ANIDT4</span>)
      ```
          27.0
          13.7
          11.7
          14.2
          9.4
          6.9
           .
           .  
      ```
      - DEM file ```.xyz``` in the following format (latitude-x, longitude-y, elevation of catchment-z <span style="font-size:18px; color:green"> ANIDT4</span>).
      ```
           x y z 
          217623.033 3251932.988 5165
          217653.033 3251932.988 5167
          217683.033 3251932.988 5168
           . . .
           . . .
      ```
4. Copy code files from the ```detrital_ui``` folder of <span style="font-size:18px; color:red"> downloaded file</span> , and then paste these in <span style="font-size:18px; color:green"> ANIDT4</span>'s ```detrital_ui``` folder. Specifically, the following files:
     -  <span style="font-size:18px; color:blue"> Python files</span> (```.py```): ``` common.py```, ```data_type.py```, ```model_setup.py```, ```plot.py```, and ```run.py```



## Running a model

1. Open a terminal in the folder (```detrital_ui```) of <span style="font-size:18px; color:green"> ANIDT4</span> containing code files (i.e., <span style="font-size:18px; color:blue"> Python files</span>) and activate the environment ```py2``` 
2. Run the *Bayesian erosion model* by typing ```python run.py``` and then click ```enter```
  

## Output files
 
Done, the model output contains:
- Simulated age-elevation plot, a ```.png ``` file (summary.png)
- Goodness of fit test plot, a ```.png``` file (KS_test.png)
- A ```.csv``` file (statistics.csv) containing: 
  - Erosion rates (mm/yr) ```e1```, ```e2```, ```e3```,...
  - Age of erosion rate change  (Ma) ```abr1```, ```abr2```,...

*End*

___

# Configuring a model

```model_setup.py``` file (in ```detrital_ui```folder of <span style="font-size:18px; color:red"> downloaded file</span>) is used primarily to configure the model for a sample for various erosion history scenarios (here example sample is <span style="font-size:18px; color:green"> ANIDT4</span>). 
The following changes are required in ```model_setup.py```, this can be done by editing class and variables in the ```model_setup.py``` :
1. Assign paths of input data files
   - Assign DEM file location and file name, for example, DEM file name is ```ANIDT4.xyz```
      ```
      catchment_1 = Catchment(hypsometry_file = "../data/ANIDT4.xyz", elevation_column = 'z')
      ```
   - Assign age file location, sample name, catchment data (```catchement_1```), thermochronometric type (```AFT```), for example, the age file name is ```ANIDT4.csv```
      ```
      sample_1 = DetritalSample(age_file = "../data/ANIDT4.csv", sample_name = 'ANIDT4', catchment = catchment_1, tc_type = 'AFT')
      ```
2. Priors (In Bayesian statistics, a prior is the initial beliefs and assumptions about a model's parameters. Priors are based on existing knowledge or expert opinion, and are usually specified using probability distributions)
   - First prior is the range of the erosion rate that the sample would have experienced, for example, from ```0``` to ```3``` mm/yr for <span style="font-size:18px; color:green"> ANIDT4</span> catchment sample, here 0 is a minimum and 3 is a maximum erosion rate that a catchment (<span style="font-size:18px; color:green"> ANIDT4</span>) would have experienced. This is based on previous studies around the sample location, or it can be a guess. In ```model_setup.py``` file, this is coded as ```erate_prior = (0,3)```.
   - Second prior is a range of the timing of change (or changes) in erosion rates that a catchment would have experienced, for example, from ```0 to 60``` Ma for <span style="font-size:18px; color:green"> ANIDT4</span> sample. This prior can be assigned from minimum and maximum ages of the measured age distribution of <span style="font-size:18px; color:green"> ANIDT4</span> sample.  In ```model_setup.py``` file, this is coded as ```abr_prior = (0,60)```.

3. Model scenarios: such as uniform and non-uniform erosion history scenarios. This is modeled by assigning number of breaks in the model. In ```model_setup.py``` file, this is coded as ```break =...```.
   - **Uniform erosion rate scenarios**: In the uniform erosion history scenario, the break will be zero, i.e., ```break = 0```, which refers to uniform erosion rates through time or no change in erosion rates throughout the time.
   - **Non-uniform erosion rate scenario** (```break=1,2```), which refers to variation in erosion rates through time. Here, ```break=1``` for the one-break scenario refers to one discrete change in erosion rates through time, and ```break=2``` for the two-break refers to two discrete changes in erosion rate through time. *Note the change can happen any time (```break=1```) or any number of times (```break=2```) between the assigned time range of change in erosion rates, here, for example between ```0 to 60```Ma*
     
4. The best model scenario (whether  ```break=0```[zero-break], ```break=1```[one-break], or ```break=2```[two-break]) is evaluated by comparing the cumulative probability distribution of modeled ages and measured ages using a goodness-of-fit (**GOF**) plot that displays the results of Kolmogorov-Smirnov (**KS**) test. An overlap of these two data suites indicates an acceptable model fit. For example, the below plot (which will be uploaded soon) displays a degree of overlap between these two; it is shown using the cumulative probability plots of measured AFT (orange dots) and swaths of modeled AFT (blue) ages. Here, the p-value is used to select the best model; it refers to the probability of getting model results close to observed results and the acceptable fitting criteria considered in this example is p >0.05. 


**Three model scenario: ```zero-break```, ```one-break```, and ```two-break``` for a detrital AFT age distribution from a catchment** <br/><img src='/images/break models.png'>*Example displaying modeled cooling history using Bayesian erosion model.*  

     
<br>

# References

- *Avdeev, B., Niemi, N. A., & Clark, M. K.* (2011). **Doing more with less: Bayesian estimation of erosion models with detrital thermochronometric data.** Earth and Planetary Science Letters, 305(3–4), 385–395. https://doi.org/10.1016/j.epsl.2011.03.020


- *Borgohain, B., Mathew, G., Salvi, D., Harbola, D., Rai, P.,* (2024). **Spatial-Temporal Variation in Erosion Rate of Lohit Bomi-Chayu Batholith around Eastern Himalayan Syntaxis (SE of Namche Barwa massif),** (Under Review in Tectonics)





