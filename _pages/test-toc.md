---
layout: single
title: "Job Market Candidates 2021"
permalink: /test-toc/
toc: true
toc_label: "JM tags"
author_profile: true
---


<style>
HTML SCSSResult Skip Results Iframe
EDIT ON
body {
  padding: 100px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica,
    Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
}

details {
  position: relative;
  display: inline-block;
  cursor: pointer;
  border-radius: 3px;
  transition: 0.15s background linear;
  &:hover {
    background: #d4d1ec;
  }
}

details > summary::-webkit-details-marker {
  display: none;
  float:left;
}

summary {
  padding: 10px;
  list-style: none;
  background: url("https://assets.codepen.io/14179/Info.svg") 11px 11.5px
    no-repeat;
  padding-left: 33px;
}

details p {
  text-align: left;
  cursor: auto;
  background: #eee;
  padding: 15px;
  width: 350px;
  position: absolute;
  left: -150px;
  top: 35px;
  border-radius: 4px;
  right: 100px;

  &:before {
    content: "";
    width: 0;
    height: 0;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-bottom: 12px solid #eee;
    top: -10px;
    position: absolute;
    left: 10px;
  }
}

details div {
  text-align: left;
  cursor: auto;
  background: #eee;
  padding: 15px;
  width: 350px;
  position: absolute;
  left: -150px;
  top: 35px;
  border-radius: 4px;
  right: 100px;

  &:before {
    content: "";
    width: 0;
    height: 0;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-bottom: 12px solid #eee;
    top: -10px;
    position: absolute;
    left: 10px;
  }
}

details[open] p {
  animation: animateDown 0.2s linear forwards;
}

details[open] div {
  animation: animateDown 0.2s linear forwards;
}

@keyframes animateDown {
  0% {
    opacity: 0;
    transform: translatey(-15px);
  }
  100% {
    opacity: 1;
    transform: translatey(0);
  }
}
</style>

<style type="text/css">
  td {
    text-align: center;
    padding: 0 20px;
  }
</style>

Profiles of graduate students in international political economy on the 2021 job market can be found here. You can also see check them out by tag 
<details><summary>here 3.</summary>
<div class="toc">
  {% for tag in site.tags %}
      <ul>
        <li><a href="#{{ tag[0] }}">{{ tag[0] }}</a></li>
      </ul>
  {% endfor %}
</div>
</details>

{% for tag in site.tags %}
  <h1 id="{{ tag[0] }}">{{ tag[0] }}</h1>
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}


