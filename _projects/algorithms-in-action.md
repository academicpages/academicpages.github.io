---
title: "🔧 Algorithms in Action"
collection: projects
permalink: /project/algorithms-in-action
excerpt: 'Algorithms in Action (AiA) is an online algorithm visualizer tool for CS students.'
date: 2020-10-01
---

<div>
  <img src="/images/aia/aia.png" alt="AiA_logo" style="width: 300px"> 
</div>

<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->

- [Project Timeline](#project-timeline)
- [Project Description](#project-description)
- [Tech Stack](#tech-stack)
- [Main Features](#main-features)
  - [Layouts](#layouts)
  - [Stepwise Refinement](#stepwise-refinement)
  - [Parameter Configurations](#parameter-configurations)
  - [Visualization Controller](#visualization-controller)
- [My Contribution](#my-contribution)

<!-- TOC end -->

<!-- TOC --><a name="project-timeline"></a>

# Project Timeline

March 2020 - October 2020

> **Try AiA demo here: [https://algorithms-in-action.github.io/](https://algorithms-in-action.github.io/){:target="_blank"}** \
> **Github: [https://github.com/algorithms-in-action/algorithms-in-action.github.io](https://github.com/algorithms-in-action/algorithms-in-action.github.io){:target="_blank"}{:target="_blank"}**

# Project Description

[Algorithms in Action (AiA)](https://algorithms-in-action.github.io/about) is an algorithm visualizer tool originally proposed by [Prof. Harald Sondergaard](https://findanexpert.unimelb.edu.au/profile/13416-harald-sondergaard), [Dr Linda Stern](https://findanexpert.unimelb.edu.au/profile/14535-linda-stern), and [Dr Lee Naish](https://people.eng.unimelb.edu.au/lee/) from the University of Melbourne in the 2000s. It was a pioneering pedagogy technology for students to learn and visualise algorithms. However, the old application was outdated and fell out of use.

To bring this pioneering pedagogy back to the light, my team and I re-designed and re-developed this application from the ground up in a modern way. We used the popular web library [React](https://reactjs.org/) and tried to make AiA open source.

Our team has implemented five different algorithms under different categories. However, our aim is not only implementing 5 algorithms but implementing them in a way that it is easy for future people to add new algorithms.

# Tech Stack

<div>
  <img src="/images/aia/aia-tech-stack.png" alt="AiA_tech"> 
</div>

- [React](https://reactjs.org/) as the main JavaScript UI library
- [Material-UI](https://material-ui.com/) as the React UI framework
- [tracer.js](https://github.com/algorithm-visualizer/tracers.js) as the visualization library for JavaScript
- [Jest](https://jestjs.io/) as the JavaScript testing framework
- [ESLint](https://eslint.org/) as the JavaScript linter

# Main Features

## Layouts

AiA has a simple three-column layout: algorithm categories on the left, visualization and controller panel in the middle, and the information display panel on the right.

<div>
  <img src="/images/aia/aia-homepage.png" alt="AiA_homepage"> 
</div>

User can select an algorithm under a category on the left, the particular information of the selected algorithm will display correspondingly. The visualization will display in the middle. The background information of the algorithm, as well as the pseudocode, will appear on the right.

## Stepwise Refinement

One of the biggest differences between AiA and other algorithm visualizer tools in the market is that AiA uses `pseudocode` instead of the actual code. Furthermore, AiA allows **stepwise refinement**, which is the pioneering pedagogy proposed by our three teachers.

The idea of the stepwise refinement is to give students a sense of how to run the algorithm from general to detail. Taking heapsort as an example, in general, we need to `BuildHeap` and then `SortHeap`. If students are wondering how to `BuildHeap`, they can click the expand button and more detailed code will display. To make the heap stable, we perform `DownHeap`. Again, to figure out how to perform `DownHeap`, we click the expand button and know that we need to compare the parent node and its two children and swap if necessary.

<div>
  <img src="/images/aia/aia-hs-stepwise-refinement.png" alt="AiA_stepwise_refine"> 
</div> 

<br>

It also features inline explanations. If students do not understand a line of the pseudocode, they can click the little 'file' icon to display the inline explanation.

<div>
  <img src="/images/aia/aia-hs-inline-explanation.png" alt="AiA_inline_explanation"> 
</div>

## Parameter Configurations

Students can set their own parameters so that they can explore any edge cases of the algorithm. Different algorithms have different parameter panels: Binary Search Tree, HeapSort, and QuickSort take an array of numbers as input, while graph algorithms like Prim's algorithm and Transitive Closure take an adjacency matrix as input.

<div>
  <img src="/images/aia/aia-parameters.png" alt="AiA_parameters"> 
</div>

## Visualization Controller

The algorithm visualization automatically plays when the 'play' button is clicked. By adjusting the speed slider, AiA also allows users to control the speed of the visualization. Moreover, if the users want to manually step through the algorithm instead of auto-playing, they can click the two buttons to step forward and backward. The visualization will change correspondingly.

<div>
  <img src="/images/aia/aia-qs-visualization.png" alt="AiA_qs_vis"> 
</div>

<div>
  <img src="/images/aia/aia-prims-visualization.png" alt="AiA_prime_vis"> 
</div>

<br>

# My Contribution

As part of the team, I highly engaged with the team not only through Zoom meetings but also through Slack due to the Covid-19 situation. I set up the project environment and created a CI/CD pipeline so that the project can be deployed automatically. My teammate and I explored a way of how to systematically add new algorithms and how to step the animation forwards and backward, which was one of the most difficult parts of the project. I implemented and refactored the Binary Search Tree algorithms (including searching and inserting), which made the rest of the algorithms easy to implement. I implemented many features/requirements, such as the play/pause functions, different parameter panels including matrix parameters, the about page, and so on. I also fixed many bugs and refactor some existing code to align with the client's feedback.