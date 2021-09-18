---
title: 'Image Refiner'
date: 2020-09-18
permalink: /posts/2012/08/2021-09-18-CodeGen/
tags:
  - MATLAB
  - Image Refinement
  - Medical Engineering
---

Getting Started
===============

The ImageRefiner is a tool written to analyse nephrological images in the `.tiff`-format. 
There are a lot of different parameters that can be adjusted in order to optimize the image analysis process. The settings used for an analysis can be adjusted in the file :file:`Settings.m`.


First steps with the ImageRefiner
---------------------------------

Make sure the data you want to analyze fits the scheme shown here! If the folder structure is different the analysis will not work as intended. 
In case this folder structure is not supplied the ImageRefiner will throw a logical error exception.

```json

  data
  |----191_19
  |       |----Cortex
  |       |       |----191-19_GF01
  |       |       |       |-----<Name>_CH1.tif
  |       |       |       |-----<Name>_CH2.tif
  |       |       |       |-----<Name>_CH3.tif
  |       |       |       |-----<Name>_CH4.tif
  |       |       |----191-19_GF02
  |       |       |       |-----<Name>_CH1.tif
  |       |       |       |-----<Name>_CH2.tif
  |       |       |       |-----<Name>_CH3.tif
  |       |       |       |-----<Name>_CH4.tif
  |       |----Medulla
  |       |       |----191-19_GF01
  |       |       |       |-----<Name>_CH1.tif
  |       |       |       |-----<Name>_CH2.tif
  |       |       |       |-----<Name>_CH3.tif
  |       |       |       |-----<Name>_CH4.tif
  ...
```

The ImageRefiner was programmed to provide tasks as a singular way of interaction for the user.
The usage of explicit functions is only advised if you are a developer and know what you are doing. Generally please stick to using the tasks.


Normal work flow
~~~~~~~~~~~~~~~~

You can run this code from the MATLAB Command Window.

```matlab
  imageRefinerTask = Tasks.ImageRefinerTask('C:\\path\to\folder\with\data', 'ExportDirectory', 'C:\\path\to\export\folder', 'excel') 
  imageRefinerTask.execute()
```

Please verify the settings inside :file:`Settings.m` to make sure that the imageAnalyzer works as intended: 
  #. SCALE_PIXEL_TO_MICRONS
  #. COLOR_CHANEL_ENUM


If you want to access the Verification mode you may run this code in the MATLAB Command Window:

```matlab
  imageVerificationTask = Tasks.ImageVerificationTask('C:\\path\to\folder\with\data', 'C:\\path\to\export\folder', 'excel') 
  imageVerificationTask.execute()
```

During the verification process you can view all areas in an image that were detected by the ImageAnalyzer. 
If you want to adapt the boundaries for areas please change the following settings inside :file:`Settings.m`: 
  #. CAPPILARY_MIN_AREA
  #. CAPPILARY_MAX_AREA


Debugging
---------

Should you encounter any problems during the programm execution please read the error message first! 
The error message will be displayed in the MATLAB window in red. Go to the first error message and try to fix the error. 
In case you do not understand the error please contact the developer (robert.goellinger@rwth-aachen.de). You may additionally attach the .log-File found inside the target directory. 