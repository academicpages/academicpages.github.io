---
title: "Research"
permalink: /research/
author_profile: true
---

## Single-sided subduction (SSS): High trench retreat rate & back-arc extension

Models can self-consistently generate a variety of trench retreat rate and induce different extent of extension within a homogeneous and mobile overriding plate. This is achieved by verying merely the age/thickness of the subducting slab and overriding plate under a well-tested rheology setup.

<!DOCTYPE html>
<html>
<head>
<style>
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

.mySlides {
  display: none;
  width: 100%;
  height: auto;
}

.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  margin-top: -22px;
  padding: 16px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}

.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.8);
}

.fade {
  -webkit-animation-name: fade;
  -webkit-animation-duration: 1.5s;
  animation-name: fade;
  animation-duration: 1.5s;
}

@-webkit-keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}
</style>
</head>
<body>

<div class="slideshow-container">

<div class="mySlides fade">
  <img src="/images/zhibinlei-SSS-thermal_state.png" style="width:100%">
</div>

<div class="mySlides fade">
  <img src="/images/zhibinlei-SSS-velocity_filter.png" style="width:100%">
</div>

<div class="mySlides fade">
  <img src="/images/zhibinlei-SSS-contribution.png" style="width:100%">
</div>

<a class="prev" onclick="plusSlides(-1)">&#10094;</a>
<a class="next" onclick="plusSlides(1)">&#10095;</a>

</div>

<script>
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
}
</script>

</body>
</html>

## Dual inward dipping subduction (DIDS) & progressive weakening within the overriding plate

Relative to SSS, DIDS can generate:  1) fixed boundary condition for the middle overriding plate 2) a stronger united upwelling mantle flow. Both effects
contribute to the progressive weakening, exbited as viscosity reduction, within the overriding plate.

![zhibinlei-dualsp-model_setup.png](/images/zhibinlei-dualsp-model_setup.png)
Model setup

![zhibinlei-dualsp-fixed trench + single sp.png](/images/zhibinlei-dualsp-fixed trench + single sp.png)
Temporal evolution of horizontal velocity component for DIDS and  SSS.

![zhibinlei-adaptive_mesh-example.gif](/images/zhibinlei-adaptive_mesh-example.gif)
Animation of plate weakening (viscosity reduction) in a DIDS model.

![dualsp-dominant deformation_mechanism.png](/images/zhibinlei-dualsp-dominant deformation_mechanism.png)
Dominant deformation analysis for a DIDS model that pull apart the overriding plate, indicating that dislocation and yielding plays the dominant role to weaken the overriding plate.

## Inherited lateral lithospheric heterogeneities & localisation of plate weakening
