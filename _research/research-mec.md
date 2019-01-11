---
title: "An Alexa-based restaurant recommendation system"
collection: research
type: "EE 596 Conversational Artificial Intelligence"
permalink: /research/research-mec
venue: "University of Washington"
date: 2018-03-21
location: "City, Country"
---

[[Code]](https://github.com/AlexXiao95/AlexaBots), 
[[Slides]](https://hao-fang.github.io/ee596_spr2018/slides/showcase/MosEisleyCantina_slides.pdf),
[[Poster]](https://hao-fang.github.io/ee596_spr2018/slides/showcase/MosEisleyCantina_poster.pdf)

## Introduction

The increased prevalence and sophistication of home-based virtual assistants such as Amazon’s Alexa has given rise to a wide variety of tailored applications employing these technologies. Virtual assistant applications can play music, manage calendars, set reminders and alarms, as well as search the web. However, some gaps in functionality are yet to be filled and user friendly recommendation systems are oftentimes lacking if not entirely absent. Thus, the motivation for this project is to fill this perceived gap by building an application that allows Alexa-users to search for restaurants that fit a variety of qualifications via their Alexa devices. Our aim is to develop a conversational restaurant recommendation system using data from the Yelp & Google Places APIs to assist people in searching for and choosing restaurants from their Alexa device.

Our target users are primarily people in urban areas with access to Alexa at home, who are looking for a restaurant to eat at now, to get takeout from, or are planning a future trip.

This application will converse with the user in a social manner by engaging them in a conversation wherein it will use both the current dialog and its memory of previous ones to set a series of constraints which will narrow the search space and provide the best recommendation.

## Finite State Dialog Manager
<div style="text-align: center">
<img src="https://alexxiao95.github.io/research/mec/dialogManager.png" width = "600">
</div>

The dialog manager, deployed as an AWS Lambda function, governs the interaction between the user and the system by guiding the dialog and petitioning the various interface modules for the necessary information such that requests by the user are satisfied. This figure contains a schematic overview of the dialog management system. After an analysis of possible user behaviours, we have defined several basic states so that our chatbot can respond to the user in a useful manner.

1. **Launch state**:​ The Launch state is the initial state of the Finite State dialog manager and the entry point to the model. It welcomes the user and asks questions while considering known information about the user. Given an appropriate user response, which is sent to the dialog manager via Alexa Language Understanding from the Interaction model, it will switch to the Add Constraint state. If the user is a first time user, we will ask them to provide their home address and work address to create their user profile. If the account has used our system before, we will first ask their feedback about our previous recommendation. If they are satisfied with the previous recommendation, we can directly recommend a similar restaurant without asking them for more information.

2. **Add Constraint state**: ​This state is to keep track of the user’s preferences to constrain the recommendations that Mos Eisley Cantina will make. The user can specify preferences as constraints like the desired location, hours (open now or not), and cuisine. When the constraints for the restaurant recommendation search are sufficient to make a good recommendation (location and cuisine type are required, unless a recommendation is being made based on a previous successful recommendation), the dialog manager will change to the Offer Recommendation state. If the provided information is insufficient, it will remain in the AddConstraint state and continue to ask the user for more information.

3. **Offer Recommendation state**:​ This state calls the Yelp API and passes user constraints, using the return values to generate restaurant recommendations. There are the following different cases:
 * If the user gives negative feedback or asks for another or a different restaurant, the dialog manager remains in this current state and offers another recommendation.
 * If the user gives positive feedback, it switches to the End state.
 * If the user wants to change constraints (if they have changed their mind and want to overwrite previous constraints) or add additional constraints like price level, the dialog manager updates the constraints and stays in this state.
 * If the user wants information about the offered recommendation, it switches to the Offer Data state.

4. **Offer Data state**: ​This state is called when the user wants Mos Eisley Cantina to provide more information about a specific restaurant. It provides restaurant information (phone number, address, opening hour, reviews and duration to get there, etc.) via the Yelp API and Google Maps API. It remains in this state, continuing to offer more data, as long as the user requests more information. If the user is satisfied with the recommendation and does not want more information, the dialog manager switches to End state. If the user wants another, different recommendation or to revisit a previous recommendation, it switches to the Offer Recommendation state.

5. **End state**:​ This state ends the session, thanks the user, and saves both the user profile and data about the recommendations made.

## Demo
<div style="text-align: center">
<img src="https://alexxiao95.github.io/research/mec/demo1.png" width = "300">
</div>
<div style="text-align: center">
<img src="https://alexxiao95.github.io/research/mec/demo2.png" width = "300">
</div>
<div style="text-align: center">
<img src="https://alexxiao95.github.io/research/mec/demo3.png" width = "300">
</div>
<div style="text-align: center">
<img src="https://alexxiao95.github.io/research/mec/demo4.png" width = "300">
</div>