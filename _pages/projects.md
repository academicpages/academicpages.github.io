---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---

{% include base_path %}

<!-- ## Selected Research Projects

<ul>
    {% for post in site.researchprojects reversed %}
        {% include archive-single-talk-cv.html %}

    {% endfor %}
<ul> -->


## Selected Software Application Projects

<ul>
    {% for post in site.projects reversed %}
        {% include archive-single-talk-cv.html %}
        <!-- <li><a href="{{ project.permalink }}" target="_blank">{{ project.title }}</a></li> -->
        <!-- [{{ project.title }}]({{ project.permalink }}){:target="_blank"} -->
        <!-- [{{ project.title }}](project.permalink) -->
    {% endfor %}
<ul>
