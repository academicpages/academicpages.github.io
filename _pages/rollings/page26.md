---
index: 26
layout: archive
permalink: /rolling-archive/page26/index.html
title: Personal daily events
author_profile: true
redirect_from:
  - /wordpress/rolling-posts/
---

{% include base_path %}
{% capture written_year %}'None'{% endcapture %}
{% assign sortedposts = site.rollings | sort: 'date' | reverse %}

{% assign is_last_partial = 0 %}
{% assign have_previus_page = 0 %}
{% assign have_next_page = 0 %}
{% assign have_valid_page = 0 %}


{% assign posts_count = sortedposts | size %}


{% assign internal_mod_pag = 1000 %}
{% if site.paginate > 0 %}
      {% assign internal_mod_pag = site.paginate %}
{% endif %}


{% assign mod_pag = posts_count | modulo:internal_mod_pag %}
{% if mod_pag > 0 %}
      {% assign is_last_partial = 1 %}
{% endif %}
{% assign pages_count = posts_count | divided_by:internal_mod_pag | plus:is_last_partial %}


{% assign next_pag = page.index | plus:1 %}


{% assign previus_pag = page.index | minus:1 %}

{% if next_pag <= pages_count %}
      {% assign have_next_page = 1 %}
{% endif %}

{% if previus_pag >= 0 %}
      {% assign have_previus_page = 1 %}
{% endif %}



{% assign OFFSET = internal_mod_pag | times:page.index %}

{% if page.index <= pages_count %}
      {% assign have_valid_page = 1 %}
{% endif %}



{% if have_valid_page > 0 %}
      {% for post in sortedposts limit:internal_mod_pag offset:OFFSET %}
        {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
        {% if year != written_year %}
          <h2 id="{{ year | slugify }}" class="archive__subtitle">{{ year }}</h2>
          {% capture written_year %}{{ year }}{% endcapture %}
        {% endif %}
        {% include archive-single.html %}
      {% endfor %}
{% endif %}



{% if pages_count > 1 %}
<nav class="pagination">
  <ul>
    {% comment %} Link for previous page {% endcomment %}
    {% if have_previus_page > 0 %}
      {% if previus_pag == 1 %}
        <li><a href="{{ base_path }}/rolling-archive/">{{ site.data.ui-text[site.locale].pagination_previous | default: "Previous" }}</a></li>
      {% else %}
        <li><a href="{{ base_path }}/rolling-archive/page{{ previus_pag }}/">{{ site.data.ui-text[site.locale].pagination_previous | default: "Previous" }}</a></li>
      {% endif %}
    {% else %}
      <li><a href="#" class="disabled"><span aria-hidden="true">{{ site.data.ui-text[site.locale].pagination_previous | default: "Previous" }}</span></a></li>
    {% endif %}
    {% comment %} First page {% endcomment %}
    {% if page.index == 1 %}
      <li><a href="#" class="disabled current">1</a></li>
    {% else %}
      <li><a href="{{ base_path }}/rolling-archive/">1</a></li>
    {% endif %}
    {% assign page_start = 2 %}
    {% if page.index > 4 %}
      {% assign page_start = page.index | minus: 2 %}
      {% comment %} Ellipsis for truncated links {% endcomment %}
      <li><a href="#" class="disabled">&hellip;</a></li>
    {% endif %}

    {% assign page_end = pages_count | minus: 1 %}
    {% assign pages_to_end = pages_count | minus: page.index %}
    {% if pages_to_end > 4 %}
      {% assign page_end = page.index | plus: 2 %}
    {% endif %}

    {% for index in (page_start..page_end) %}
      {% if index == page.index %}
        <li><a href="{{ base_path }}/rolling-archive/page{{ index }}/" class="disabled current">{{ index }}</a></li>
      {% else %}
        {% comment %} Distance from current page and this link {% endcomment %}
        {% assign dist = page.index | minus: index %}
        {% if dist < 0 %}
          {% comment %} Distance must be a positive value {% endcomment %}
          {% assign dist = 0 | minus: dist %}
        {% endif %}
        <li><a href="{{ base_path }}/rolling-archive/page{{ index }}/">{{ index }}</a></li>
      {% endif %}
    {% endfor %}
    {% comment %} Ellipsis for truncated links {% endcomment %}
    {% if pages_to_end > 3 %}
      <li><a href="#" class="disabled">&hellip;</a></li>
    {% endif %}
    {% if page.index == pages_count %}
      <li><a href="#" class="disabled current">{{ page.index }}</a></li>
    {% else %}
      <li><a href="{{ base_path }}/rolling-archive/page{{ pages_count }}/">{{ pages_count }}</a></li>
    {% endif %}


    {% comment %} Link next page {% endcomment %}
    {% if have_next_page > 0 %}
      <li><a href="{{ base_path }}/rolling-archive/page{{ next_pag }}/">{{ site.data.ui-text[site.locale].pagination_next | default: "Next" }}</a></li>
    {% else %}
      <li><a href="#" class="disabled"><span aria-hidden="true">{{ site.data.ui-text[site.locale].pagination_next | default: "Next" }}</span></a></li>
    {% endif %}
  </ul>
</nav>
{% endif %}
