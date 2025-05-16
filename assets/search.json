---
layout: null
sitemap: false
---

{% capture json %}
[
  {% assign collections = site.collections | where_exp:'collection','collection.output != false' %}
  {% for collection in collections %}
    {% assign docs = collection.docs | where_exp:'doc','doc.sitemap != false' %}
    {% for doc in docs %}
      {
        "title": {{ doc.title | jsonify }},
        "excerpt": {{ doc.excerpt | markdownify | strip_html | jsonify }},
        "content": {{ doc.content | markdownify | strip_html | jsonify }},
        "url": {{ site.baseurl | append: doc.url | jsonify }}
      },
    {% endfor %}
  {% endfor %}
  {% assign pages = site.html_pages | where_exp:'doc','doc.sitemap != false' | where_exp:'doc','doc.title != null' %}
  {% for page in pages %}
  {
    "title": {{ page.title | jsonify }},
    "excerpt": {{ page.excerpt | markdownify | strip_html | jsonify }},
    "content": {{ page.content | markdownify | strip_html | jsonify }},
    "url": {{ site.baseurl | append: page.url | jsonify }}
  }{% unless forloop.last %},{% endunless %}
  {% endfor %}
]
{% endcapture %}

{{ json | lstrip }}
