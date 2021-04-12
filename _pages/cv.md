---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

## Educación

* Doctor en Ciencias Ambientales. Universidad de Granada, 2017. Programa en Ingeniería Civil y Arquitectura.    
* Diploma de Estudios Avanzados. Universidad de Granada, 2010. Programa en Urbanística, Ordenación del Territorio y Medio Ambiente.  
* Máster en Gestión de Sistemas de Información Geográfica. Universidad de Girona, 2010.  
* Licenciatura en Ciencias Ambientales. Universidad de Granada, 2008.  

## Publicaciones

  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

## Docencia

  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

## Ponencias y cursos

  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
