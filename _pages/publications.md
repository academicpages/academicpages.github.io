<!-- <!-- ---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %} -->


<!-- ---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<div class="publication-list">
  {% for post in site.publications reversed %}
    <div class="publication-item">
      <div class="publication-year">{{ post.year }}</div>
      <div class="publication-content">
        <div class="publication-image">
          {% if post.image %}
            <img src="{{ post.image }}" alt="Publication Image">
          {% endif %}
        </div>
        <div class="publication-details">
          <h3 class="publication-title">{{ post.title }}</h3>
          <p class="publication-authors">{{ post.authors }}</p>
          <p class="publication-venue">{{ post.venue }}</p>
          <div class="publication-links">
            {% if post.pdf %}
              <a href="{{ post.pdf }}" class="btn">PDF</a>
            {% endif %}
            {% if post.github %}
              <a href="{{ post.github }}" class="btn">GitHub</a>
            {% endif %}
            {% if post.poster %}
              <a href="{{ post.poster }}" class="btn">Poster</a>
            {% endif %}
            {% if post.youtube %}
              <a href="{{ post.youtube }}" class="btn">YouTube</a>
            {% endif %}
            {% if post.news %}
              <a href="{{ post.news }}" class="btn">News Coverage</a>
            {% endif %}
            {% if post.medium %}
              <a href="{{ post.medium }}" class="btn">Medium Article</a>
            {% endif %}
          </div>
        </div>
      </div>
    </div>
  {% endfor %}
</div> --> -->

