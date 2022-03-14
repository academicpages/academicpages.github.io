---
permalink: /
title: "MotionSC"
excerpt: "About me"
author_profile: true
redirect_from: /sitemap/
---

<p>A Data Set and Network for Real-Time Semantic Mapping in Dynamic Environments</p>
<div>
    <video autoplay="autoplay" src="./images/MotionSCHomeVideo.mp4" controls="controls" width="100%" />
</div>

<div class="page__lead">
    <div class="page__content">
        <div class="HOME-feature-block">
            <div>
                Trace Free Scenes
                <p>
                    <img src="./images/TraceFree.png" alt="Trace Free">
                </p>
                <p>
                    MotionSC scenes are sampled from multiple viewpoints, ensuring minimal occlusions and no traces left by dynamic objects. The image above showcases MotionSC lack of traces for dynamic objects compared to SemanticKITTI, another well known vision benchmark.
                </p>
            </div>
            <div>
                Sequential Labels
                <p>
                    <img src="./images/SemanticLabel.png" alt="SemanticLabel">
                </p>
                <p>
                    Data is captured at 10Hz and semantic labels along with scene flow data ground truth data is provided for each frame. This provides more information for scene understanding over multiple scans.
                </p>
            </div>
            <div>
                Synthetic Data
                <p>
                    <img src="./images/Carla.png" alt="Carla">
                </p>
                <p>
                    MotionSC is generated using CARLA, an open source simulator for autonomous driving research. This enables high customizability, from the number of dynamic objects to the position and number of sensors.
                </p>
            </div>
            <!-- <p class="small">
                Additional Information here.
            </p> -->
    </div>
    <div class="page__content">
        <p>
        Comparison with Other Semantic Mapping Datasets
        </p>
        <table class="table">
            <tr>
                <th>Metric</th>
                <th>Our Dataset (MotionSC)</th> 
                <th>SemanticKitti</th>
            </tr>
            <tr>
                <td>Scan Speed (Hz)</td> 
                <td>10</td> 
                <td>10</td>
            </tr>
            <tr>
                <td>Total Scene Count</td>
                <td>24</td> 
                <td>20</td>
            </tr>
            <tr>
                <td>Total Class Count</td>
                <td>23</td> 
                <td>28</td>
            </tr>
        </table>
    </div>
</div>

<div class="page__content">
    Getting started
    <p class="small">
        A description of the dataset and its properties can be found in the Dataset page on this website. To download it, please visit the Download page to download the Cartesian or Cylindrical dataset version. An example of how to use the dataset can be found on the MotionSC Github repository linked in the Download page as well. This repository contains the CarlaSC dataloader used in the MotionSC paper as well as python visualization scripts.
    </p>
</div>  


<div class="page__content">
    <div>
        Paper
    </div>
    <p class="small">
        See our paper below for more information and our network baseline results: 
        <div>
            <img src="./images/MotionSCPaperAll.png" alt="MotionSC Paper Here" background-size="cover">
        </div>
        <p class="small">
            If you plan to use our dataset and tools in your work, we would appreciate it if you could cite our paper.
            (<a href="https://github.com/UMich-CURLY/3DMapping">PDF</a>)
        </p>
    </p>
</div>  

