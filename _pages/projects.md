---
layout: archive
title: "Projects"
permalink: /Projects/
author_profile: true
---

<style>
/* CSS for tabbed navigation */
.tab {
  overflow: hidden;
  border: 1px solid #ccc;
  background-color: #f1f1f1;
}

/* Style the buttons inside the tab */
.tab button {
  background-color: inherit;
  float: left;
  border: none;
  outline: none;
  cursor: pointer;
  padding: 14px 16px;
  transition: 0.3s;
  font-size: 17px;
}

/* Change background color of buttons on hover */
.tab button:hover {
  background-color: #ddd;
}

/* Create an active/current tablink class */
.tab button.active {
  background-color: #ccc;
}

/* Style the tab content */
.tabcontent {
  display: none;
  padding: 6px 12px;
  border: 1px solid #ccc;
  border-top: none;
}
</style>

<div class="tab">
  <button class="tablinks" onclick="openProject(event, 'CourseCompanion')">Course Companion</button>
  <button class="tablinks" onclick="openProject(event, 'UrbanAnalysis')">Walkability and Well-Being</button>
  <button class="tablinks" onclick="openProject(event, 'CPUScheduling')">CPU Scheduling & Process Synchronization</button>
</div>

<div id="CourseCompanion" class="tabcontent">
  ## [Course Companion](https://github.com/ethanlanders/Course-Companion)
</div>

<div id="UrbanAnalysis" class="tabcontent">
  ## [Walkability and Well-Being - An Urban Analysis](https://github.com/ethanlanders/Walkability-And-Well-Being-Analysis-CS620-Data-Project)

  ### **Old Dominion University, Fall 2023**

  <video width="100%" height="400" controls allowfullscreen>
    <source src="../files/Walkability&WellBeing_CS620.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>

  Collaborated with classmates on a project exploring the intricate relationship between community walkability and various facets of well-being in urban environments, focusing on New York City neighborhoods.

  ## **Objective:**
  Investigate correlations between walkability and well-being indicators, such as concentrated poverty rates and student obesity rates.

  ## **Methodology:**
  Collected data on New York City walkability, poverty, and obesity. Utilized Python, Pandas, Matplotlib, and Seaborn for preprocessing and visualization. Merged datasets for comprehensive analysis.

  ## **Results:**
  No significant correlation between walkability and poverty. Identified higher obesity rates in less walkable New York City neighborhoods.
  <img src="../files/Poverty-Walkability.png" alt="Visualization displaying the correlation between Poverty and Walkability in New York City neighborhoods.">
  <img src="../files/Obesity-Walkability.png" alt="Visualization displaying the correlation between Obesity and Walkability in New York City neighborhoods.">
</div>

<div id="CPUScheduling" class="tabcontent">
  ## [CPU Scheduling & Process Synchronization](https://github.com/ethanlanders/CPUScheduling-ProcessSynchronization-CS471Project)

  ### **Old Dominion University, Fall 2023**

  <video width="100%" height="400" controls allowfullscreen>
    <source src="../files/CS471CourseProject.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>

  Collaborated with a classmate on a comprehensive project addressing CPU scheduling algorithms and process synchronization.

  ## CPU Scheduling Problem:
  * Developed a CPU scheduler simulation with FIFO, SJF, and Priority algorithms.
  * Utilized C++ to handle 541 simulated processes, addressing arrival time, CPU burst length, and priority.
  * The problem incorporates well-documented code and sample input data files and produces detailed statistics for each scheduling algorithm.

  ## Process Synchronization Problem:
  * Classmate led the development of the Producer-Consumer problem using Pthreads, with comprehensive testing and performance measurement.
  * The solution is implemented in C++ and covers various scenarios, providing insights into overall turnaround time.

  This project allowed us to delve into the intricacies of operating systems, applying theoretical concepts to practical problem-solving.
</div>

<script>
function openProject(evt, projectName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(projectName).style.display = "block";
  evt.currentTarget.className += " active";
}
</script>
