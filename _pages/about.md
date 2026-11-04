---
layout: academic
permalink: /
excerpt: "Adam Umra — research in integrated sensing and communication, machine learning for signal processing, and reconfigurable intelligent surfaces at Ruhr University Bochum."
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

<section class="profile" aria-labelledby="profile-name">
  <h1 id="profile-name">Adam Umra</h1>
  <p class="profile-subtitle">Doctoral Researcher at Ruhr University Bochum</p>
  <div class="profile-intro">
    <div class="profile-copy">
      <p>I am a doctoral researcher at the <a href="https://www.dks.ruhr-uni-bochum.de/">Chair of Digital Communication Systems</a> at <a href="https://www.ruhr-uni-bochum.de/en">Ruhr University Bochum</a>, Germany.</p>
      <p>My research focuses on <strong>integrated sensing and communication (ISAC)</strong>, <strong>machine learning for signal processing</strong>, and <strong>localization and tracking</strong>. I work on cognitive radar, reconfigurable intelligent surfaces, and reliable wireless communication.</p>
      <p>I received my B.Sc. in 2021 and M.Sc. in 2023 in Electrical Engineering and Information Technology from Ruhr University Bochum.</p>
    </div>
    <figure class="profile-photo">
      <img src="{{ '/images/profile.jpg' | relative_url }}" alt="Adam Umra" width="8256" height="5504" fetchpriority="high">
      <figcaption>&copy; RUB, Marquard</figcaption>
    </figure>
  </div>
  <ul class="profile-links" aria-label="Contact and profiles">
    <li><a href="mailto:{{ site.author.email }}">Email</a></li>
    <li><a href="{{ site.author.googlescholar | escape }}">Google Scholar</a></li>
    <li><a href="https://www.linkedin.com/in/{{ site.author.linkedin }}">LinkedIn</a></li>
    <li><a href="https://github.com/{{ site.author.github }}">GitHub</a></li>
    <li><a href="https://www.dks.ruhr-uni-bochum.de/de/profiles/adam-umra/">University profile</a></li>
  </ul>
</section>

<section aria-labelledby="news">
  <h2 id="news" class="section-heading">News</h2>
  <ul class="news-list">
    {% for item in site.data.news %}
    <li><time datetime="{{ item.date }}">{{ item.label }}</time><span>{{ item.text | markdownify | remove: '<p>' | remove: '</p>' }}</span></li>
    {% endfor %}
  </ul>
</section>

<section aria-labelledby="publications">
  <h2 id="publications" class="section-heading">Publications</h2>
  <p class="section-intro">Journal articles, conference papers, and recent preprints. See also my <a href="{{ site.author.googlescholar | escape }}">Google Scholar profile</a>.</p>
  <ol class="publication-list">
    {% assign publications = site.data.publications_generated | default: site.data.publications %}
    {% for paper in publications %}
    <li class="publication">
      <h3>{{ paper.title | escape }}</h3>
      <p class="publication-authors">{{ paper.authors | escape | replace: 'Adam Umra', '<strong>Adam Umra</strong>' }}</p>
      <p class="publication-venue"><em>{{ paper.venue | escape }}</em> · {{ paper.year }}{% if paper.status %} <span class="publication-status">{{ paper.status }}</span>{% endif %}</p>
      <ul class="publication-links" aria-label="Links for {{ paper.title | escape }}">
        {% for link in paper.links %}
        <li><a href="{{ link.url | escape }}">{{ link.label }}</a></li>
        {% endfor %}
      </ul>
    </li>
    {% endfor %}
  </ol>
</section>

<section aria-labelledby="experience">
  <h2 id="experience" class="section-heading">Experience</h2>
  <ul class="experience-list">
    <li>
      <p class="entry-meta">Current · Bochum, Germany</p>
      <h3>Doctoral Researcher, Ruhr University Bochum</h3>
      <p>Chair of Digital Communication Systems. Research on sensing, communication, and learning-based signal processing.</p>
    </li>
    <li>
      <p class="entry-meta">2021–2023 · Ruhr University Bochum</p>
      <h3>M.Sc. in Electrical Engineering and Information Technology</h3>
      <p>Focus on communication technology, radio frequency, and artificial intelligence.</p>
    </li>
    <li>
      <p class="entry-meta">2021 · Ruhr University Bochum</p>
      <h3>B.Sc. in Electrical Engineering and Information Technology</h3>
    </li>
  </ul>
</section>
