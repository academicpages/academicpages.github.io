---
layout: archive
title: "Cats & Codes"
permalink: //cats-and-codes/
author_profile: false
--- 
<!-- Displaying categories -->
{% include base_path %}
<p class="category__taxonomy">
  <strong><i class="fa fa-fw fa-folder-open" aria-hidden="true"></i> {{ site.data.ui-text[site.locale].categories_label | default: "Categories:" }} </strong>
  <span itemprop="keywords">
  {% for category in site.categories %}
    {% assign keyValue = category | split: '#' %}
    {% capture category_word %}{{ category | first }}{% endcapture %}
    <a href="/categories/#{{ category | first | slugify}}" class="category__taxonomy-item" rel="tag">{{ category_word }}</a>{% unless forloop.last %}<span class="sep"></span>{% endunless %}
  {% endfor %}
  </span>
</p>

<style>
    .category__taxonomy-item {
      color: black;
      font-size: 16px;
      text-align: center;
      border: solid;   
      background: AliceBlue; 
      border-radius:10px;
      border-color: AliceBlue;
      padding: 0.3em;
      margin-bottom: 0.5em;
      text-decoration: none!important;
    }  
    .category__taxonomy-item:hover{
      background-color: SlateBlue;
    }
</style>
<style>
    .tag__taxonomy-item{
      color: black;
      font-size: 14px;
      text-align: center;
      text-decoration: none;
      border: solid;   
      background: MistyRose; 
      border-radius:10px;
      border-color: MistyRose;
      text-decoration: none!important;
      padding: 0.3em;
      margin-bottom: 0.5em;
      cursor: pointer;
    }
    .tag__taxonomy-item:hover{
      background-color: crimson;
    }
</style> 

<!-- Post -->
<ul class="post-list">
<!-- Looping over the posts -->
    {% for post in site.posts %}
          <h2>
            <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
          </h2>
          <style>
            .post-link{
              text-decoration: none!important;
            }
          </style>
          <!-- Author -->
          {% assign author = site.data.authors[post.author] %}
          <div class="teaser-container">
          {% if author.avatar %}
          <img class = "author-logo" src="/images/{{author.avatar}}"/>
          {% endif %}
          {% if post.date %}
          <p class="page__date"><strong><i class="fa fa-fw fa-calendar" aria-hidden="true"></i> {{ site.data.ui-text[site.locale].date_label | default: "Published:" }}</strong> <time datetime="{{ post.date | default: "1900-01-01" | date_to_xmlschema }}">{{ post.date | default: "1900-01-01" | date: "%B %d, %Y" }}</time>, by <u>{{author.name}}</u></p>
          {% endif %}
          <!--  -->
          </div>
          <style>
          .author-logo{
            margin: 6px;
            border-radius: 50%;
            float: left;
            width: 50px;
            height: 50px;
            border: 2px solid {{post.bcolor}};       
          }
          </style>
          <style>
          .teaser-container {
            display: flex;
            align-items: center;
            flex-direction: row;
            font-size: 15px;
          }
          </style>
          <style>
          <!-- Zoom Hovering effect -->
          .zteaser-thumbnail{
            transition: transform .2s; /* Animation */
          }
          .teaser-thumbnail:hover {
            transform: scale(1.15); /* (150% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
          }
          </style>
          {% if post.image %}
          <img class="teaser-thumbnail" style="border-top:20px solid {{ post.bcolor }};border-right:20px solid {{ post.bcolor }};border-left:20px solid {{ post.bcolor }};border-bottom:1px solid {{ post.bcolor }};"
          src="{{ site.baseurl }}/blog_images/{{ post.image}} " width="440px" height="240px"> 
          {% endif %}
          {{ post.excerpt }}
          <div class = "btn-tag">
          <a class="btn btn-default" href="{{ post.url | prepend: site.baseurl }}"> Read more </a>
          <p class="tag__taxonomy">
          <i class="fa fa-fw fa-tags" aria-hidden="true"></i>
            <span itemprop="keywords">
            {% for hash in post.tags %}
              {% assign keyValue = hash | split: '#' %}
              {% capture tag_word %}{{ keyValue[1] | strip_newlines }}{% endcapture %}
              <a href="/tags/#{{hash | slugify}}"  class="tag__taxonomy-item" rel="tag">{{ hash }}</a>{% unless forloop.last %}<span class="sep"></span>{% endunless %}
            {% endfor %}
            </span>
          </p>
          </div>
          <style>
          .btn-tag {
            display: flex;
            align-items: center;
            flex-direction: row;
            gap: 5%;
            <!-- font-size: 15px; -->
          }
          </style>
          <hr/>
    {% endfor %}  
</ul>

**_More blog posts will be updated soonish. Happy to host more, therefore feel free to write to me if you are interested. Also the website development is in progress, so don't hesistate to report any bug [here](https://github.com/academicpages/academicpages.github.io/pull/915)_**

**_Find more data science and web-development related videos on my [youtube channel](https://www.youtube.com/c/Avra_b/videos)_**
<section class="page__share">
  {% if site.data.ui-text[site.locale].share_on_label %}
    <h4 class="page__share-title">{{ site.data.ui-text[site.locale].share_on_label | default: "Share on" }}</h4>
  {% endif %}

  <a href="https://twitter.com/intent/tweet?text={{ base_path }}{{ page.url }}" class="btn btn--twitter" title="{{ site.data.ui-text[site.locale].share_on_label | default: 'Share on' }} Twitter"><i class="fab fa-twitter" aria-hidden="true"></i><span> Twitter</span></a>

  <a href="https://www.facebook.com/sharer/sharer.php?u={{ base_path }}{{ page.url }}" class="btn btn--facebook" title="{{ site.data.ui-text[site.locale].share_on_label | default: 'Share on' }} Facebook"><i class="fab fa-facebook" aria-hidden="true"></i><span> Facebook</span></a>

  <a href="https://www.linkedin.com/shareArticle?mini=true&url={{ base_path }}{{ page.url }}" class="btn btn--linkedin" title="{{ site.data.ui-text[site.locale].share_on_label | default: 'Share on' }} LinkedIn"><i class="fab fa-linkedin" aria-hidden="true"></i><span> LinkedIn</span></a>
</section>



