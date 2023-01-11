---
layout: archive
title: "Students and research"
permalink: /my-students/
author_profile: true
header:
  og_image: "research/ecdf.png"
---
<h2>Parinaz Barakhshan</h2>
<img src="../images/Parinaz/parinaz.jpg" width="200" 
     height="200" alt="DARWIN">

I am a third-year Ph.D. candidate and Research Assistant at the University of Delaware, Department of Electrical and Computer Engineering.

I have always loved learning, growing, developing, and challenging myself to contribute to something significant. The whole point of learning more is to be able to make a difference in the world. My purpose is to help the world run better.

My research interests include:

        optimizing compilers,
        programming methodologies,
        source-to-source Translators,
        performance evaluation for HPC,
        best practices and tools in computational and data-intensive research,
        using ML, deep learning, and NLP to solve problems that cannot be solved in traditional ways.

For more information, see the <a href="https://sites.udel.edu/parinazb/">Personal Web Site</a>
<b>Research Topic: iCetus, An Interactive Parallelizing Compiler</b>
<img src="../images/Parinaz/pimage.jpg" width="200" height="200" alt="DARWIN">

<b>Project Description: </b> Today’s computers are all multicore. In a modern shared-memory architecture, parallelization techniques enable us to utilize multiple processors simultaneously and improve the performance of an application by converting sequential code into multi-threaded and/or vectorized code. 

Our goal is to develop a tool that allows users with varying skill sets to apply parallelization techniques interactively. While the tool can parallelize the code/ parts of the code in a fully automatic format for Non-expert users,  Power users can finely steer the optimization process through the tool menus to obtain an optimized version of the code.



---------------------------------------------------------------------------------------------------
<h2>Akshay Bhosale</h2>
<img src="../images/Akshay/Akshay.jpg" width="200" 
     height="200" alt="DARWIN">

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


For more information, see the <a href="https://subscripted-subscript.akshayud.me/>Personal Web Site</a>
<b>Research Topic: Subscripted subscript patterns</b>
<img src="../images/Akshay/pakshay.jpg" width="200" height="200" alt="DARWIN">

<b>Project Description: </b> A number of scientific applications comprise of loops wherein an array is subscripted by another array - a[b[i]]. With write references to the host array (array ‘a’) within a loop, current compile-time techniques are incapable of detecting such loops as parallelizable. If left unparallelized, these loops can in-turn prevent the performance obtained through automatic parallelization, matching that of the hand parallelized version. Hence, Subscripted subscript analysis is the next big challenge in Automatic Parallelization.
----------------------------------------------------------------------------------------------------
<h3>Real-Application Benchmarks for High-Performance Computing</h3>

<img src="../images/research/spec30logo.jpg" width="300" 
     height="300" alt="spec30">

We are creating HPC benchmarks that are representative of real-world applications. This is a collaboration with the Standard Performance Evaluation Corporation, <a href="http://spec.org">SPEC</a> and Indiana University. <a href="https://www.nsf.gov/awardsearch/showAward?AWD_ID=1842623">NSF award page</a>. <a href="https://www.udel.edu/udaily/2020/june/sunita-chandrasekaran-rudi-eigenmann-supercomputer-benchmarks/">News release</a>

<b>Collaborators: </b> <a href="https://www.eecis.udel.edu/~schandra/">Sunita Chandrasekaran</a>, <a href="https://itnews.iu.edu/people/henschel.php">Robert Henschel</a>


<h3>Cetus Source-to-Source Compiler Infrastructure</h3>
<img src="../images/research/cetus.png" width="300" 
     height="300" alt="cetus">
 
 Cetus is a compiler and transformation infrastructure for transforming C source code. The original purpose of Cetus was for automatic parallelization - translation of C code into C code annotated with OpenMP directives. Many other uses of the translator have emerged, such as the translation of OpenMP programs into CUDA and MPI. Cetus is being maintained as a community infrastructure and has been used for many projects worldwide (see the list of publications on the Cetus web page).
The Cetus project is a collaboration with Purdue University. NSF awards:
<a href="https://www.nsf.gov/awardsearch/showAward?AWD_ID=0707931">0707931</a>
<a href="https://www.nsf.gov/awardsearch/showAward?AWD_ID=1405954">1405954</a>

<a href="https://sites.udel.edu/cetus-cid/">Cetus Website</a>

<b>Research Staff: </b> <a href="https://akshayud.me">Akshay Bhosale</a>, Parinaz Barakhshan, Jan Sher Khan, Hao Wang  
<b>Collaborators: </b> <a href="https://engineering.purdue.edu/~smidkiff/">Samuel Midkiff</a>, Milind Kulkarni.



<nbsp>

<!-- {% include base_path %}

{% assign ordered_pages = site.research | sort:"order_number" %}

{% for post in ordered_pages %}
  {% include archive-single.html type="grid" %}
{% endfor %} -->
