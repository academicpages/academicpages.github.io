---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---
## Professional Projects

### ⛰️ Cervest - Global Digital Terrain Model ⛰️
  * Implemented end-to-end ML workflow to build a global Digital Elevation Model that has allowed to correct under- prediction of flood risk in several urban areas and to derive valuable auxiliary information to other work streams.
  * Built modeling framework for quick refinement and prototyping, using Pytorch Lightning, Ray Tune, and Mlflow. Carried out parameter tunning of models in parallel using multiple GPU and multi-CPUs in-house servers.
  * Architected bespoke attention based UNet model to produce high-quality terrain reconstructions.
  * Coordinated the development of scalable data pipelines, including geospatial ML data processing workflows and those focused on the inference stage. Pipelines were designed to comply with computational requirements and scalability performance, using Argo CD and Kubernetes.

### 🌾 GMV - BIGMIG DEMO - Use of Space Based Big Data to Prevent Forced Migration 🌾
  * Development of a hybrid bespoke spatio-temporal Convolutional LSTM deep neural architecture for semantic segmentation of a time series of multispectral satellite imagery. Nowcasting of agriculture, land use identification, and geospatial feature extraction in remote areas of Mozambique.
  * Work accepted for presentation and delivered at the 2019 ESA Phi Week, and the [1st AI for Copernicus workshop](https://climate.copernicus.eu/1st-artificial-intelligence-copernicus-workshop-presentations) at ECMWF, (Reading).
  * [ESA Project website](https://business.esa.int/projects/bigmig-demo)

### 🚂 GMV - Smart Railway 🚂
  * Development of a commercial system to be used by the rail industry capable of 3D semantic segmentation of LIDAR point cloud data using geometric deep neural networks. Generation of a pseudo-real-time 3D geospatial model of the envelope surrounding the UK rail network for surveying applications, asset monitoring, and change over time pre-emptive alerts.
  * Development of a new end-to-end system for the rail industry which makes use of bespoke Geometric Deep Neural Networks to perform highly accurate automated railway surveying and gauging given point clouds captured using train mounted LIDAR
  * Automatic real-time generation of a 3D digital twin of the UK rail network
  * Relationship development with Network Rail and Transport for London

### 🌧️ GMV - HYMS - Precipitation Nowcasting with STFC/RAL 🌧️
  * With the UK Space Agency funding, STFC’s RAL Space will develop a pre-prototype of this new kind of sensor the Hyperspectral Microwave Sounder ([HYMS](https://www.youtube.com/watch?v=IP7QMPeXLrM), small enough to fly onboard a nano-satellite, set to transform the future of weather forecasting. It has achieved four times greater sensitivity than sounder technology onboard the current generation of meteorological satellites, and a hardware footprint 50-fold smaller. HYMS its capacity to record measurements at a higher revisit rate than existing weather satellite (Having a constellation of satellites that can offer radiance measurements along with microwave hyperspectral spectrum at a high-rate opens the door to new advances in the weather short-range forecasting and nowcasting field)
  * To exploit that capability and contribute to the accurate prediction of extreme short-range weather events, GMV has reviewed state-of-the-art and prototyped a deep neural architecture precipitation nowcasting algorithm. Combining multiple-source input data (i.e., radar, infrared, and microwave) the prototyped model successfully forecasted precipitation values for the next hour.
    
  * Key achievements:
    * Conducted research study entitled to show potential benefit on the use of microwave satellite data for precipitation nowcasting applications. Gained knowledge about cutting-edge developed ML models for nowcasting applications (ConvLSTM, Unet, Self-attention-based architectures, Conditional GANs (cGAN))
    * Identification of meteorological datasets suitable for nowcasting machine learning applications.
    * Implemented Unet Network using research datasets that combined spatio-temporal data coming from multiple sensors (radar, satellite data (visible, infrared, microwave).

### 🍫 GMV - MRV4C 🍫 
  * Development of system reliant on geospatial EO big data ML processing chains to provide remote monitoring reporting and verification services. Development of deep neural networks to extract information from a synergy of radar and multispectral satellite imagery data streams.
  * Contribution to the development of interactive web app to showcase generated products to end-users. Functionalities spans over statistical reports to interactive geospatial visualizations using Streamlit and Kepler.gl.


### 🛰️ GMV - GNSS Ionopshere Modelling  - HARMONY 🛰️
  * Machine Learning to Model GNSS Systems focuses on the development of a Machine Learning GNSS demonstrator capable of showcasing the benefit of ML for the GNSS sector. Use cases to be considered include the use of Deep Learning for Ionospheric Delay Modeling and IGS Products forecasting.
