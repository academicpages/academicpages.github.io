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
  font-size: 16px;
  font-family: Helvetica, Arial, sans-serif;
  color: #444;
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

/* Style the GitHub button */
.github-button {
  display: inline-block;
  padding: 10px 20px;
  margin-top: 10px;
  font-size: 16px;
  background-color: #24292e;
  color: #ffffff;
  text-decoration: none;
  border-radius: 5px;
}

.github-button:hover {
  background-color: #3b4045;
}
</style>

<div class="tab">
  <button class="tablinks" onclick="openProject(event, 'NetflixFilmAnalysis')"><b>Netflix Film Analysis</b></button>
  <button class="tablinks" onclick="openProject(event, 'CourseCompanion')"><b>Course Companion</b></button>
  <button class="tablinks" onclick="openProject(event, 'UrbanAnalysis')"><b>Walkability & Well-Being</b></button>
  <button class="tablinks" onclick="openProject(event, 'CPUScheduling')"><b>CPU Management</b></button>
</div>

<div id="NetflixFilmAnalysis" class="tabcontent">
  <h2>Netflix Film Analysis</h2>
  <a href="https://github.com/ethanlanders/netflix-film-analysis" class="github-button">View on GitHub</a>
  <h3>Video Demo:</h3>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/GDShteNxp6c?si=8WDGTLSQgJd4Rcyd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  <span><a href="https://colab.research.google.com/drive/15Z0Y3_eYU-PMwSIJ4-XGYdNBDaoJ52hA?usp=sharing" target="_blank">Click here</a> to view the project report.</span>

</div>

<div id="CourseCompanion" class="tabcontent">
  <h2>Course Companion</h2>
  <a href="https://github.com/ethanlanders/Course-Companion" class="github-button">View on GitHub</a>
  <p><b>Old Dominion University, Fall 2023 & Spring 2024</b></p>
  <p>Worked with a team of eight on our senior year capstone project to develop Course Companion, a tool designed to help university instructors improve the accessibility and quality of their course materials. This software allows educators to upload course materials for in-depth analysis, providing valuable insights and suggestions for enhancement.</p>
  <h3>Key Features:</h3>
    <ul>
      <li>Navigable GUI for easy use</li>
      <li>Document analysis for course materials in various file types</li>
      <li>Accessibility suggestions for educators</li>
      <li>Detailed report generation for easy review and reference</li>
      <li>View and save previously generated reports</li>
    </ul>
    <h3>Technologies Used:</h3>
    <p>Python, PyQt5, Pandoc</p>
</div>

<div id="UrbanAnalysis" class="tabcontent">
  <h2>Walkability and Well-Being - An Urban Analysis</h2>
  <a href="https://github.com/ethanlanders/Walkability-And-Well-Being-Analysis-CS620-Data-Project" class="github-button">View on GitHub</a>
  <p><b>Old Dominion University, Fall 2023 & Spring 2024</b></p>
  <h3>Video Demo:</h3>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/W4uXdOSEJTo?si=CW39xMWMVd9xYa0k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

  <p>Collaborated with classmates on a project exploring the intricate relationship between community walkability and various facets of well-being in urban environments, focusing on New York City neighborhoods.</p>

  <h3>Objective:</h3>
  <p>Investigate correlations between walkability and well-being indicators, such as concentrated poverty rates and student obesity rates.</p>

  <h3>Methodology:</h3>
  <p>Collected data on New York City walkability, poverty, and obesity. Utilized Python, Pandas, Matplotlib, and Seaborn for preprocessing and visualization. Merged datasets for comprehensive analysis.</p>

  <h3>Results:</h3>
  <p>No significant correlation between walkability and poverty. Identified higher obesity rates in less walkable New York City neighborhoods.</p>
  <img src="../files/Poverty-Walkability.png" alt="Visualization displaying the correlation between Poverty and Walkability in New York City neighborhoods.">
  <img src="../files/Obesity-Walkability.png" alt="Visualization displaying the correlation between Obesity and Walkability in New York City neighborhoods.">
</div>

<div id="CPUScheduling" class="tabcontent">
  <h2>CPU Scheduling & Process Synchronization</h2>
  <a href="https://github.com/ethanlanders/CPUScheduling-ProcessSynchronization-CS471Project" class="github-button">View on GitHub</a>
  <p><b>Old Dominion University, Fall 2023 & Spring 2024</b></p>

  <h3>Video Demo:</h3>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/MF5aDcGZ3pQ?si=n0fAuwoORmq0cF2d" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

  <p>Collaborated with a classmate on a comprehensive project addressing CPU scheduling algorithms and process synchronization.</p>

  <h3>CPU Scheduling Problem:</h3>
  <ul>
    <li>Developed a CPU scheduler simulation with FIFO, SJF, and Priority algorithms.</li>
    <li>Utilized C++ to handle 541 simulated processes, addressing arrival time, CPU burst length, and priority.</li>
    <li>The problem incorporates well-documented code and sample input data files and produces detailed statistics for each scheduling algorithm.</li>
  </ul>

  <h3>Process Synchronization Problem:</h3>
  <ul>
    <li>Classmate led the development of the Producer-Consumer problem using Pthreads, with comprehensive testing and performance measurement.</li>
    <li>The solution is implemented in C++ and covers various scenarios, providing insights into overall turnaround time.</li>
  </ul>

  <p>This project allowed us to delve into the intricacies of operating systems, applying theoretical concepts to practical problem-solving.</p>
</div>

<script>
function openProject(evt, projectName) {
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(projectName).style.display = "block";
  evt.currentTarget.className += " active";
}
</script>
