---
permalink: /students/
title: ""
excerpt: "Students"
redirect_from: 
  - /students.html
---
{% include base_path %}

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
<li> <div>{% if person.photo %}<a href="{{ person.photo | replace: 'BASE', base_path}}"><img class="alumnus" src="{{ person.photo | replace: 'BASE', base_path }}" alt="{{ person.name }}" /></a>{% endif %}
     {{ person.name }} (PhD {{ person.year }})<br />
     Thesis: <i><a href="{{ person.thesis_url }}">{{person.thesis}}</a></i><br />
     Current position: {{ person.position }}</div>
     <div style="clear:both;"></div></li>
{% endfor %}
</ul>
