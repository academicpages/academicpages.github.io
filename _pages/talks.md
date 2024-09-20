---
permalink: /talks
title: "Talks"
---

# Talks

<ul>
{% assign talks = site.data.talks | sort: "date" | reverse %}
{% for talk in talks %}
<li>
<b>{{ talk.title }} @ {{ talk.venue }}{{ talk.date | date: "%Y" }}
{% if talk.url %}
    <a href="{{ talk.url }}" target="_blank">[Video]</a>
{% endif %}
</b>
</li>
{% endfor %}
</ul>