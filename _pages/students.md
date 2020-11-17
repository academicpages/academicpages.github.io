---
permalink: /students/
title: ""
excerpt: "Students"
redirect_from: 
  - /students.html
---

I'm fortunate to work with a fantastic research group. 

<h1>Postdocs</h1>
{% assign people = site.data.students | where: "type", "postdoc" | sort: "name" %}
<ul>
{% for person in people %}
<li> {{ person.name }} </li>
{% endfor %}
</ul>

<h1> PhD Students</h1>
{% assign people = site.data.students | where: "type", "phd" | sort: "name" %}
<ul>
{% for person in people %}
<li> {{ person.name }} </li>
{% endfor %}
</ul>

<h1>Master's Students</h1>
{% assign people = site.data.students | where: "type", "masters" | sort: "name" %}
<ul>
{% for person in people %}
<li> {{ person.name }} </li>
{% endfor %}
</ul>

<h1> Undergrad Students </h1>
{% assign people = site.data.students | where: "type", "ugrad"  | sort: "name" %}
<ul>
{% for person in people %}
<li> {{ person.name }} </li>
{% endfor %}
</ul>

<h1>Alumni</h1>
{% assign people = site.data.students | where: "type", "phd-alumni" | sort: "name" %}
<ul>
{% for person in people %}
<li> {{ person.name }} (PhD {{ person.year }})<br />
     Thesis: <i><a href="{{ person.thesis_url }}">{{person.thesis}}</a></i><br />
     Current position: {{ person.position }}
</li>
{% endfor %}
</ul>
