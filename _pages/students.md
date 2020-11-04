---
permalink: /students/
title: ""
excerpt: "Students"
redirect_from: 
  - /students.html
---

I'm fortunate to work with a fantastic research group. 

# Postdocs
{% assign people = site.data.students | where: "type", "postdoc" | sort: "name" %}
<ul>
{% for person in people %}
<li> {{ person.name }} </li>
{% endfor %}
</ul>


# PhD Students
{% assign people = site.data.students | where: "type", "phd" | sort: "name" %}
<ul>
{% for person in people %}
<li> {{ person.name }} </li>
{% endfor %}
</ul>

# MS / MEng Students
{% assign people = site.data.students | where: "type", "masters" | sort: "name" %}
<ul>
{% for person in people %}
<li> {{ person.name }} </li>
{% endfor %}
</ul>

# Undergrad Students
{% assign people = site.data.students | where: "type", "ugrad"  | sort: "name" %}
<ul>
{% for person in people %}
<li> {{ person.name }} </li>
{% endfor %}
</ul>
