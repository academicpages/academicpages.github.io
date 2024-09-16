---
permalink: /software
title: "Software"
---

# Software

{% assign types = site.data.software | group_by: "type" %}
{% for soft_group in types %}
<h3>{{ soft_group.name | title }}</h3>
<ul>
{% assign software_group = soft_group.items | sort: "title" %}
{% for software in software_group %}
<li>
<a href="{{ software.url }}" target="_blank"><b>{{ software.title }}</b></a>
<p> {{ software.description }}</p>
</li>
{% endfor %}
</ul>
{% endfor %}