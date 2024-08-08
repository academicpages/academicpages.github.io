---
permalink: /publications
title: "Publications"
---

# Publications
\* Equal contribution

{% for collection in site.data.publications %}
<h3>{{ collection.type | capitalize }}</h3>
<ul>
{% assign publications = collection.publications | sort: "date" | reverse %}
{% for publication in publications %}
<li>
{% assign authors = publication.authors | split: ", " %}
{% for member in authors %}
    {% if member == "Sledzieski" or member == "Sledzieski*" %}
        <b>{{ member }}</b>,
    {% else %}
        {{ member }},
    {% endif %} 
{% endfor %}
"{{ publication.title }},"
<i>{{ publication.venue }}</i>{% if publication.extra %}, {{ publication.extra }}{% endif %}.
    {% if publication.pdf %} <a href="{{ publication.pdf }}" target="_blank"><b>[PDF]</b></a> {% endif %}
    {% if publication.code %} <a href="{{ publication.code }}" target="_blank"><b>[Code]</b></a> {% endif %}
    {% if publication.talk %} <a href="{{ publication.talk }}" target="_blank"><b>[Talk]</b></a> {% endif %}
</li>
{% endfor %}
</ul>
{% endfor %}

### PhD Thesis: [Learning the Language of Biomolecular Interactions]({{ baseurl }}/assets/files/Sledzieski_PhD_Thesis.pdf) ([Defense](https://www.youtube.com/watch?v=lJkTFrfQ510))