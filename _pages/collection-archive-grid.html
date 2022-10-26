---
layout: archive
title: "Posts by Collection (grid view)"
permalink: /collection-archive-grid/
entries_layout: grid
author_profile: true
---

{% assign entries_layout = page.entries_layout | default: 'list' %}
{% capture written_label %}'None'{% endcapture %}

{% for collection in site.collections %}
  {% unless collection.output == false or collection.label == "posts" %}
    <section class="taxonomy__section">
      {% capture label %}{{ collection.label }}{% endcapture %}
      {% if label != written_label %}
        <h2 id="{{ label | slugify }}" class="archive__subtitle">{{ label }}</h2>
        {% capture written_label %}{{ label }}{% endcapture %}
      {% endif %}
      <div class="entries-{{ entries_layout }}">
        {% for post in collection.docs %}
          {% include archive-single.html type=entries_layout %}
        {% endfor %}
      </div>
      <a href="#page-title" class="back-to-top">{{ site.data.ui-text[site.locale].back_to_top | default: 'Back to Top' }} &uarr;</a>
    </section>
  {% endunless %}
{% endfor %}
