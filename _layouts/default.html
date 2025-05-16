<!DOCTYPE html>
<html lang="{{ site.lang | default: "en-US" }}">

  <head>
    <!-- General meta -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    {% if page.indexing == false %}
      <meta name="robots" content="noindex">
    {% endif %}

    {% if page.collectionpage %}
      {% seo title=false %}

      {% assign collectiondata = site.collections | where: "label", page.collectionpage | first %}
      <title>{{ collectiondata.title }} - {{ site.title }}</title>
      <meta property="og:title" content="{{ collectiondata.title }}">
      <meta name="description" content="{{ collectiondata.description }}">
      <meta property="og:description" content="{{ collectiondata.description }}">
    {% else %}
      {% seo %}
    {% endif %}
    {% if site.fonts.preconnect_urls %}
      {% for url in site.fonts.preconnect_urls %}
        <link rel="preconnect" href="{{ url }}" crossorigin />
      {% endfor %}
    {% endif %}

    <link rel="manifest" href="{{ "/manifest.json" | relative_url }}">
    <meta name="theme-color" content="{{ site.manifest.theme_color | default: '#242e2b' }}"/>

    {% if site.css_inline == true %}
      {% include site-styles.html %}
    {% else %}
      <link rel="stylesheet" href="{{ "/assets/styles.css" | relative_url }}">
    {% endif %}

    {% if site.favicons or site.avatarurl %}{% include site-favicons.html %}{% endif %}

    {% if site.google_analytics %}{% include site-analytics.html %}{% endif %}

    {% include site-fonts.html %}

    {% include site-before-start.html %}
  </head>

  <body class="layout-{{ page.layout }}{% if page.title %}  {{ page.title | slugify }}{% endif %}">
    {% include site-icons.svg %}

    {{ content }}

    {% if site.service_worker != false %}{% include site-sw.html %}{% endif %}

    {% include site-before-end.html %}
  </body>

</html>
