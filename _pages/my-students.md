---
layout: archive
title: "Students and research"
permalink: /my-students/
author_profile: true
header:
  og_image: "research/ecdf.png"
---
<!DOCTYPE html>
<html>
<head>
<style>
.grid-container {
  display: grid;
  column-gap: 50px;
  grid-template-columns: auto auto;
  background-color: #2196F3;
  padding: 10px;
}

.grid-item {
  background-color: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(0, 0, 0, 0.8);
  padding: 20px;
  font-size: 30px;
  text-align: center;
}
</style>
</head>
<body>

<h1>The column-gap Property</h1>

<p>Use the <em>column-gap</em> property to adjust the space between the columns:</p>

<div class="grid-container">
  <div class="grid-item">1</div>
  <div class="grid-item">2</div>
  <div class="grid-item">3</div>  
  <div class="grid-item">4</div>
  <div class="grid-item">5</div>
  <div class="grid-item">6</div>  
  <div class="grid-item">7</div>
  <div class="grid-item">8</div>
  <div class="grid-item">9</div>  
</div>

</body>
</html>
<h2>Parinaz Barakhshan</h2>
<div>
  <div>
    <p style="float:left">
      <img  src="../images/my-students/Parinaz/parinaz.jpg" width="200"  height="200" alt="parinaz">
    </p>
    <p float= "right" align="right">
      <p align="left" style="padding:10px" >
        I am a third-year Ph.D. candidate and Research Assistant at the University of Delaware, Department of Electrical and Computer Engineering.

        I have always loved learning, growing, developing, and challenging myself to contribute to something significant. The whole point of learning more is to be able to make a difference in the world. My purpose is to help the world run better.
      </p>
    </p>
  </div>

  <div >
      My research interests include:

              optimizing compilers,
              programming methodologies,
              source-to-source Translators,
              performance evaluation for HPC,
              best practices and tools in computational and data-intensive research,
              using ML, deep learning, and NLP to solve problems that cannot be solved in traditional ways.

      For more information, see the <a href="https://sites.udel.edu/parinazb/">Personal Web Site</a>
  </div>
<b>Research Topic: iCetus, An Interactive Parallelizing Compiler</b>
<br>
<img src="../images/my-students/Parinaz/pimage.png" width="200" height="200" alt="">

<b>Project Description: </b> Today’s computers are all multicore. In a modern shared-memory architecture, parallelization techniques enable us to utilize multiple processors simultaneously and improve the performance of an application by converting sequential code into multi-threaded and/or vectorized code. 

Our goal is to develop a tool that allows users with varying skill sets to apply parallelization techniques interactively. While the tool can parallelize the code/ parts of the code in a fully automatic format for Non-expert users,  Power users can finely steer the optimization process through the tool menus to obtain an optimized version of the code.



---------------------------------------------------------------------------------------------------
<h2>Akshay Bhosale</h2>
<img src="../images/my-students/Akshay/Akshay.png" width="200" 
     height="200" alt="Akshay">

I am currently working towards my PhD at the University of Delaware in Newark,DE . My major is Computer Engineering.My Undergrad major was Electronics Engineering. I have completed coursework in a variety of areas ranging from web application security, computer architecture, secure software design to parallel programming, compilers , ML and cryptography. This page will give you a comprehensive overview of all my work.
Principal Research Interests

    Automatic Parallelization
    Multi-Level Intermediate Representation (MLIR)
    Source to Source Translators
    Parallel programming paradigms
    Compile-time analysis and transformation techniques

Other subjects/research areas of interest

    Machine Learning
    Computer Systems Architecture


For more information, see the <a href="https://subscripted-subscript.akshayud.me/">Personal Web Site</a>
<br>
<b>Research Topic: Subscripted subscript patterns</b>
<br>
<img src="../images/my-students/Akshay/pakshay.png" width="400" height="400" alt="Akshay">
<br>
<b>Project Description: </b> A number of scientific applications comprise of loops wherein an array is subscripted by another array - a[b[i]]. With write references to the host array (array ‘a’) within a loop, current compile-time techniques are incapable of detecting such loops as parallelizable. If left unparallelized, these loops can in-turn prevent the performance obtained through automatic parallelization, matching that of the hand parallelized version. Hence, Subscripted subscript analysis is the next big challenge in Automatic Parallelization.



---------------------------------------------------------------------------------------------------
<h2>Miguel Rosas</h2>
<img src="../images/my-students/MiguelR/MiguelR.png" width="200" 
     height="200" alt="MiguelR">

I am a 24 years old P.hd student from the department of Computer Engineering at the University of Delaware. I am  from Cali-Colombia  and am an alumni from the Community College Initiative program  2017-2018 at Houston Community College. Also, I am a community leader with a solid professional and academic background in human rights and Software Engineering. Throughout my work at the Universidad ICESI in COlombia, I have contributed to original concepts for  software engineering, and machine learning methodologies. Right now, I am part of the National Science Foundation-supported project designed to expand access to artificial intelligence, led by The Ohio State University. Last but not least, I have  been awarded with several scholarships by the national and international industry, such as One Young World 2021 sponsored by Pfizer company, the summer internship program 2021, Global Rights Connection2021 sponsored by EQUITAS in Canada, where I obtained the social award for my  project called "I have a Dream 2021", The Youth Ambassador Program 2020 sponsored by the Department of State and among others."

<b>Principal Research Interests</b>

    Automatic Parallelization
    Software Development
    Artificial Intelligence
    Parallel programming paradigms
    Compile-time analysis and transformation techniques

<b>Other subjects/research areas of interest</b>

    Human Rights
    Diplomacy



<b>Research Topic: Artificial Intelligence in Compilers</b>
<br>
<img src="../images/my-students/MiguelR/pimage.jpeg" width="400" height="400" alt="AI">

<b>Project Description: </b>

</div>
<nbsp>

<!-- {% include base_path %}

{% assign ordered_pages = site.research | sort:"order_number" %}

{% for post in ordered_pages %}
  {% include archive-single.html type="grid" %}
{% endfor %} -->
