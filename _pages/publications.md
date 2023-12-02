---
layout: archive
title: "Publications"
permalink: /publications/
excerpt: "<sup class='hash'>#</sup>co-first author; <sup class='asterisk'>*</sup>corresponding author"
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  <div id="article-container-{{ post.title }}" class="article-container"></div>
  <script>
      document.addEventListener('DOMContentLoaded', (event) => {
          fetchAndParseBibtex('{{ post.title }}-paper.bib').then(parsedData => {
              let htmlContent = generateArticleHtml(parsedData);
              document.getElementById("article-container-{{ post.title  }}").innerHTML = htmlContent;
          });
      });
  </script>
{% endfor %}

