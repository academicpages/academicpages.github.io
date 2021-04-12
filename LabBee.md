---
title: "LabBee: General-purpose microscopy automation assistant"
excerpt: "LabBee: General-purpose microscopy automation assistant"
sitemap: false
permalink: /LabBee/
author_profile: false
---

### Control your microscope with a voice assistant!

## About
- General-purpose lab automation assistant powered by **Amazon Alexa**
- Enables **voice control of scientific equipment and software**
- Integrates with other Alexa devices and features (smart sockets, timers, calendars, etc)

## Preview

*In these demonstrations, Amazon Alexa calls the LabBee custom skill. LabBee is being used to control an Olympus microscope via open-source [Micro-Manager](https://micro-manager.org/) software.*

<br />
<iframe width="560" height="315" src="https://www.youtube.com/embed/q7ksrQ13pbM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<br />

<iframe width="560" height="315" src="https://www.youtube.com/embed/MtSdDXN6GyI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Current features

Currently, LabBee can be used to control microscopes by interfacing with the open-source [Micro-Manager](https://micro-manager.org/) software. The following features are implemented.

| Voice command  | Description |
|     ---        |    ---      |
| "Microscope"      | Opens microscope interface or says that it is already open       |
| "Snap" / "Snap image"   | Snaps image with current acquisition settings        |
| "Live mode {**ON**/**OFF**}"   | Turns live mode on or off        |
| "Move stage {**DIRECTION**} {**DISTANCE**} microns"   | Moves the stage in the specified direction (up/down/left/right)        |
| "Again / Repeat"   | Repeat the previous move (stage or objective) |
| "Set exposure to {**X**} milliseconds"   | Sets camera exposure. |
| "Increase/decrease exposure by {**X**} {percent/milliseconds}"   | Adjusts camera exposure. |
| "Move objective {**UP**/**DOWN**} by {**X**} microns"   | Moves the objective. |
| "What is the exposure?"   | Returns the exposure value. |
| "Set up acquisition"   | Sets up acquisition series. Define time interval between images and the number of images|
| "Start the acquisition" / "Acquire"   | Starts acquisition if it is already set up.|


## Contact

Contact [Ilya Kolb](mailto:koljr2005@gmail.com)